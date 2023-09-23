import numpy as np
from flask import Flask , render_template , request , jsonify
import json
import pickle
app = Flask(__name__)


#Load the pickle model 
#model = pickle.load(open("C:\Codes\SIH\project\model.pkl" , "rb"))


@app.route("/predict", methods = ['POST'])
def get_result():
    data = request.get_json()
    #print(data)
    return json.dumps({"result": data['array']})



if __name__ == "__main__":
    app.run(port=5000)
