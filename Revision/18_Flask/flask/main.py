from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return "<html><H1>Welcome to the Home page of Flask App</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about_us():
    return render_template('about.html')
    
if __name__=="__main__":
    app.run(debug=True,port=90)