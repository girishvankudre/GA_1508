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

@app.route('/get_Post_summary',methods=['POST'])
def summarise_post():
    article = json.loads(request.data.decode())['article']
    summaryObjPost = FindSummary('../GA_1508/config')
    summaryTextPost = summaryObjPost.summarise_post(article)
    return summaryTextPost

@app.route('/about_us',methods=['POST'])
def dummyReq():
    article = json.loads(request.data.decode())['article']
    print('Printing data:\n',article)
    return "Ok request works"

if __name__=="__main__":
    app.run(host='127.0.0.1',port=8080,debug=True)
