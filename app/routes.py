from flask import render_template, flash, redirect, request, session, url_for
from flask_admin.contrib.sqla import ModelView
from app import app, db, admin
from .models import User, Competition, Event
from datetime import datetime

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Competition, db.session))
admin.add_view(ModelView(Event, db.session))

from functools import wraps

from project.users.views import users_blueprint, login_required
from project.host.views import host_blueprint
from project.manage.views import manage_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(host_blueprint)
app.register_blueprint(manage_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile-layout.html')

@app.route('/learnmore')
def learnmore():
    return render_template('learnmore.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/announcements')
def announcements():
    return render_template('announcements.html')

@app.route('/comp-competitors')
def competitors():
    return render_template('competitors.html')

@app.route('/comp-schedule')
def schedule():
    return render_template('schedule.html')

#@app.errorhandler(404)
#def page_not_found(e):
#  return render_template('404.html'), 404

@app.route('/404')
def error():
    return render_template('404.html')


def postAnnouncement():
    # Code for posting announcement

    # render template / reload page
    eventAnnouncements()
