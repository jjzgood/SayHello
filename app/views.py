from app import app,db,limiter
from flask import render_template,redirect,url_for
from app.forms import MessageForm
from app.models import Message
from datetime import timedelta


@app.template_filter('format_time')
def timedelta_time(date):
    date = date + timedelta(hours=8)
    return date.strftime('%Y-%m-%d %H:%M:%S')


# @limiter.limit("5 per day")
@app.route('/',methods=['GET','POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name,body=body)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html',form=form,messages=messages)


@app.errorhandler(404)
def error404(msg):
    print(msg)
    return render_template('404.html')


@app.errorhandler(429)
def error429(msg):
    print(msg)
    return render_template('429.html')


