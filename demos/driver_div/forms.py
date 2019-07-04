# author:wufei
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required, length


class login_form(FlaskForm):
    username = StringField('用户名：', validators=[data_required(),length(5,10)])
    password = PasswordField('密码:', validators=[data_required(),length(4,10)])
    remember = BooleanField('记住')
    submit = SubmitField('提交')
