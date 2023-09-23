import numpy as np
from flask import Flask , render_template , request , jsonify
import pickle
app = Flask(__name__)


#Load the pickle model 
model = pickle.load(open("C:\Codes\SIH\project\model.pkl" , "rb"))


@app.route("/")
def hello_world():
    return render_template("index.html")



if __name__ == "__main__":
    app.run()
