import flask
from flask import request, Flask
from ga_1508_textsummerize import FindSummary
import json

app = Flask(__name__)

@app.route('/home',methods=['GET'])
def checkApiStatus():
    return "Yay!! Its all good"

@app.route('/get_summary',methods=['GET'])
def summarise():
    summaryObj = FindSummary('../GA_1508/config')
    summaryText = summaryObj.summarise()
    return summaryText

if __name__=="__main__":
    app.run(host='127.0.0.1',port=8080,debug=True)