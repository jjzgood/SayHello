from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length


class MessageForm(FlaskForm):
    name = StringField('名称',validators=[DataRequired(),Length(min=1,max=20)])
    body = TextAreaField('说点什么',validators=[DataRequired(),Length(min=1,max=200)])
    submit = SubmitField('发送')


