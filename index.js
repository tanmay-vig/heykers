const express=require('express');
const ejs=require('ejs');
const app = express();
app.set('view engine', 'ejs');

app.use(express.urlencoded({extended: true}));
app.use(express.static("public"));
let isBot=0;
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
    res.render('home',option);
});
app.post('/',(req,res)=>{
    const text=req.body.text;
    const newid=messages[messages.length-1].id+1;
    messages.push({id:newid,text:text,sender:isBot?"bot":"user"});
    isBot=!isBot;
    /* console.log(isBot); */
    res.redirect('/');
});









app.listen(3000, function() {
    console.log("Server started on port 3000");
  });