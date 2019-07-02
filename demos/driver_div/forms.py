# author:wufei
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required, length


class login_form(FlaskForm):
    username = StringField('用户名：', validators=[data_required(), length(1, 8)])
    password = PasswordField('密码:', validators=[data_required(), length(8, 20)])
    remember = BooleanField()
    submit = SubmitField('提交')
