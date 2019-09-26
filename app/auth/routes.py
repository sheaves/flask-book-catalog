from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at
from app.auth.models import User

@at.route('/register', methods = ['GET', 'POST'])   # default method is GET
def register_user():
    if current_user.is_authenticated:
        flash('you are already logged in')
        return redirect(url_for('main.display_books'))

    form = RegistrationForm()

    if form.validate_on_submit():
        # POST request, and validates data
        User.create_user(   # capture data
            user = form.name.data,
            email = form.email.data,
            password = form.password.data)
        flash('Registration successful')    # flashes a temporary message
        return redirect(url_for('authentication.do_the_login'))    # sends User to login page as soon as registation is successful

    return render_template('registration.html', form = form)  # Only served if it is a GET request

@at.route('/login', methods = ['GET', 'POST'])
def do_the_login(): # login_user clashes with an inbuilt method
    if current_user.is_authenticated:
        flash('you are already logged in')
        return redirect(url_for('main.display_books'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(user_email = form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentials. Please try again.')
            return redirect(url_for('authentication.do_the_login'))

        login_user(user, form.stay_loggedin.data) #inbuilt method that writes user credentials to the session
        return redirect(url_for('main.display_books'))

    return render_template('login.html', form = form)

@at.route('/logout')
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('main.display_books'))

@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404