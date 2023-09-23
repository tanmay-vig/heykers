const express=require('express');
const ejs=require('ejs');
const request = require('request-promise');
const app = express();
app.set('view engine', 'ejs');

app.use(express.urlencoded({extended: true}));
app.use(express.static("public"));
let isBot=0;
let result;
const messages = [
    { id: 1, text: "Hi there!", sender: "bot" },
    { id: 2, text: "Hello!", sender: "user" },
    { id: 3, text: "How can I assist you today?", sender: "bot" },
    { id: 4, text: "I have some problems!", sender: "user" },
    { id: 5, text: "Woah, What kind of problems?", sender: "bot" },
    { id: 6, text: "Medical ones!", sender: "user" },
    { id: 7, text: "So, what do you wanna tell?", sender: "bot" }
  ];
app.get('/',(req,res)=>{
    const option={
        messages:messages
    }
    //console.log(messages);
    res.render('home',option);
});

app.post('/chat',(req,res)=>{
    const text=req.body.text;
    const newid=messages[messages.length-1].id+1;
    messages.push({id:newid,text:text,sender:isBot?"bot":"user"});
    isBot=!isBot;
    console.log("CHat request done",isBot);
    res.redirect('/');
});

app.post('/', async (req, res) => {
    // Access the form data including checkbox values
    // Checkbox values will be in checkboxData
    const checkboxData = req.body;
    const array=Object.values(checkboxData);
    //delete first element with empty value
    array.shift();
    const data={
        array: array
        
    };

    const options={
        method: 'POST',
        url: 'http://127.0.0.1:5000/predict',
        body:data,
        json: true
    };

   await request(options).then(function (parsedBody) {
        //console.log(parsedBody);
        result = parsedBody['result'];
        console.log("results ", result);
        const str=result.join(",");
        const text="Got your disease! You are going to die in 2 seconds."+str;
        const newid=messages[messages.length-1].id+1;
        messages.push({id:newid,text: text,sender:isBot?"bot":"user"});
        isBot=!isBot;
        res.redirect('/');
    })
    .catch(function (err) {
        console.log(err);
    });




    //for syncronisation, had to use timeout
    /* setTimeout(() => {
        console.log(array);
    }, 20); */
  
    // Handle the form data, e.g., store it in a database, process it, etc.
    // ...
  
    // Redirect or render a response
// Redirect back to home page
  });









app.listen(3000, function() {
    console.log("Server started on port 3000");
  });