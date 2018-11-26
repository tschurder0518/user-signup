from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True  



@app.route("/")
def index():
    return render_template("form.html",
        username_error="",
        password_error="",
        email_error="")


@app.route("/validate", methods=['post'])
def validate():
    username = request.form['username']
    password = request.form['password']
    password_conf = request.form['verifypassword']
    email = request.form['email']

    username_error = ''
    password_error = ''
    email_error = ''

    #username validation
    if username == '':
        username_error = "Please enter a username"
        username = ''
    if len(username) < 3:
        username_error = "Please enter a valid username"
    elif len(username) > 20:
        username_error = "Please enter a valid username"
    for char in username:
        if char == ' ':
            username_error = "Please enter a valid username"
 
    #password validation
    if password == '':
        password_error = "Please enter a valid password"
        password = ''
        password_conf = ''
    if password != password_conf:
        password_error = "Your passwords do not match, please enter matching passwords"
        password = ''
        password_conf = ''
    if len(password) < 3:
        password_error = "Please enter a valid password"
        password = ''
        password_conf = ''
    if len(password) > 20:
        password_error = "Please enter a valid password"
        password = ''
        password_conf = ''

    #email validation
    if len(email) != 0:
        if " " in email:
            email_error = "Please enter a valid email address"
        if "." not in email:
            email_error = "Please enter a valid email address"
        if "@" not in email:
            email_error = "Please enter a valid email address"
        if len(email) < 3:
            email_error = "Please enter a valid email address"
        if len(email) > 20:
            email_error = "Please enter a valid email address"
        
    if len(email_error) == 0 and len(password_error) == 0 and len(username_error) == 0:
        return render_template("welcome.html",
            username=username)
    else:
        return render_template("form.html",
            username_error=username_error,
            password_error=password_error,
            email_error=email_error)

    
app.run()