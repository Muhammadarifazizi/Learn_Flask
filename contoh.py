from flask import Flask

app = Flask(__name__)

@app.route("/wellcome")
def wellcome():
    return "Hello There"

@app.route("/hiring")
def hiring():
    return " Hiring a Job"

if __name__=="__main__":
    app.run(debug=True)
