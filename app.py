import numpy as np
from flask import Flask , render_template , request , jsonify
import pickle
app = Flask(__name__)


#Load the pickle model 
model = pickle.load(open("C:\Codes\SIH\project\model.pkl" , "rb"))


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/predict" ,  method = "POST")
def predict():
    float_features = [float(x) for x in request.form.values ()]
    features = [np.array(float_features)]
    prediction = model.predict (features)
    return render_template("index.html", prediction_text = "Disease is {}".format(prediction))


if __name__ == "__main__":
    app.run()