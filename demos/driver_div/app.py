# author:wufei
import os
from flask import Flask, render_template,redirect

app=Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY','123456')

@app.route('/')
def index():
    messages={'all':['PG_AL_DM_PLY_NO','PG_AL_DM_PLY_NO2','PG_AL_DM_PLY_NO3','PG_AL_DM_PLY_NO4'],
        'ITS': ['PG_ITS_DM_PLY_NO', 'PG_ITS_DM_PLY_NO2', 'PG_ITS_DM_PLY_NO3', 'PG_ITS_DM_PLY_NO4']}
    return render_template('index.html',messages=messages)

