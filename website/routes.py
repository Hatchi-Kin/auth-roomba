from website.forms import LoginForm, RegisterForm  
from website.models import User, db 
from website.utils import get_events_by_weekday, compare_dicts#, save_events_to_json

from flask import render_template, url_for, redirect, request  
from flask_login import login_user, login_required, logout_user, current_user
import bcrypt


def home():
    return render_template("home.html")


def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.checkpw(form.password.data.encode("utf-8"), user.password):  
                login_user(user)
                return redirect(url_for("dashboard"))
    return render_template("login.html", form=form)


@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.hashpw(form.password.data.encode("utf-8"), bcrypt.gensalt())
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@login_required
def dashboard():
    if request.method == 'POST':
        isen_url = request.form.get('ics_url')
        current_user.set_ics_url(isen_url)
        events_by_weekday = get_events_by_weekday(isen_url)
        # save_events_to_json(events_by_weekday)
        current_user.set_checkpoint(events_by_weekday)
        return redirect(url_for('dashboard'))
    
    isen_url = current_user.get_ics_url()
    events_by_weekday = None
    if isen_url is not None:
        checkpoint = current_user.get_checkpoint()
        events_by_weekday = get_events_by_weekday(isen_url)
        events_by_weekday = compare_dicts(checkpoint, events_by_weekday)
    return render_template("dashboard.html", events_by_weekday=events_by_weekday)
