from flask import Flask, request, jsonify
from service import getBestMatch
app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page."""
    return "Welcome"

@app.route('/search', methods=["GET"])
def searchGet():
    """Renders the search page."""
    output_string = "Get search invoked"
    return output_string

@app.route('/search', methods=["POST"])
def searchPost():
    context= request.json['context']
    category= request.json['category']
    threshold= request.json['threshold']
    noOfMatches= request.json['noOfMatches']
    inputPath= request.json['inputPath']
       
    return jsonify(getBestMatch(context,category,threshold,noOfMatches,inputPath))

@app.route('/ping', methods=["GET"])
def ping():
    return "200"

if __name__ == '__main__':
    app.run(debug=True)