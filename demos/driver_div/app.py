# author:wufei
import os
from flask import Flask, render_template, redirect, url_for, request, session
from forms import login_form

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '123456')


@app.route('/', methods=['GET', 'POST'])
def index():
    logined=False
    if 'username' in session:
        logined=True
    messages = {'all': ['PG_AL_DM_PLY_NO', 'PG_AL_DM_PLY_NO2', 'PG_AL_DM_PLY_NO3', 'PG_AL_DM_PLY_NO4'],
                'ITS': ['PG_ITS_DM_PLY_NO', 'PG_ITS_DM_PLY_NO2', 'PG_ITS_DM_PLY_NO3', 'PG_ITS_DM_PLY_NO4']}
    return render_template('index.html', messages=messages,logined=logined)


@app.route('/login', methods=['POST', 'GET'])
def login():
    f_login = login_form()
    logined = False
    if f_login.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        if 'username' not in session:
            session['username'] = username
            logined = True
        return redirect('/')
    return render_template('login.html', f_login=f_login, logined=logined)
