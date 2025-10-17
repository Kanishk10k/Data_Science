from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask App"

@app.route("/about")
def about_us():
    return "This is the About Us page"

@app.route("/index")
def index():
    return "This is the Index page"

@app.route("/contact")
def contact_us():
    return "This is the Contact Us page"

if __name__=="__main__":
    app.run(host="192.168.18.1",debug=True,port=90)