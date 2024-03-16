from flask import Flask, request
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/', methods=["GET"])
def home():
    """Renders the home page."""
    return "Welcome"

@app.route('/search', methods=["GET"])
def search():
    """Renders the search page."""
    context= request.args.get("context")
    category= request.args.get("category")
    threshold= request.args.get("threshold")
    noOfMatches= request.args.get("noOfMatches")
    inputPath= request.args.get("inputPath")
    output_string = context +" "+category+" "+threshold+" "+noOfMatches+" "+inputPath
    return output_string

@app.route('/ping', methods=["GET"])
def ping():
    return "200"
