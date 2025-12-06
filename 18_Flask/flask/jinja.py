from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return "<html><H1>Welcome to the Home page of Flask App</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about_us():
    return render_template('about.html')
    
@app.route("/submit",methods=['GET','POST'])
def sub():
    if request.method=='POST':
        name=request.form['name']
        return f'<html><H1>Hello {name}!</H1></html>'
    return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:res="PASSED"
    else:res="FAILED"

    return render_template('result.html',res=res)

@app.route('/res/<int:score>')
def res(score):
    res=""
    if score>=50:res="PASSED"
    else:res="FAILED"
    
    exp={'score':score,'res':res}

    return render_template('result1.html',res=exp)

@app.route('/if/<int:score>')
def ifsuccess(score):
    return render_template('result2.html',score=score)

@app.route('/avg',methods=['GET','POST'])
def avg():
    ts=0
    if request.method=='POST':
        sc=float(request.form['science'])
        math=float(request.form['math'])
        c=float(request.form['c'])
        ds=float(request.form['ds'])
        ts=(sc+math+c+ds)/4
    else: return render_template('getresult.html')
    return redirect(url_for('res',score=ts))

if __name__=="__main__":
    app.run(debug=True,port=90)