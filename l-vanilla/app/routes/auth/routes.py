

from flask import (render_template, flash, redirect, url_for,
                   request, session)

from mongoengine.errors import DoesNotExist

from app.routes.auth import auth

from app.forms.auth import LoginForm, RegistrationForm
from app.models.user import User, Role
from app.utils.decorators import login_required


@auth.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Login'

    if session.get('user') and session['user']['username'] is not None:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():

            user = User.objects.filter(email=form.email.data.lower()).first()

            if user is None or not user.check_password(form.password.data):
                flash(u'Invalid email or password', 'danger')
                return redirect(url_for('auth.login'))

            if user is not None:
                if session.get('user'):
                    session['user'] = {'id': str(user.id),
                                       'username': user.username,
                                       'email': user.email,
                                       'slug': user.slug}

    return render_template('auth/login.html',
                           title=title,
                           form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    title = 'Register'

    if session.get('user') and session['user']['username'] is not None:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User()
            user.set_username(form.username.data)
            user.set_email(form.email.data)
            user.set_password(form.password.data)
            user.set_slug(user.username)
            user.role = Role.objects.filter(name='USER').first()
            user.save()

            flash('Congratulations, you are now a registered user!', 'primary')

            return redirect(url_for('auth.login'))

    return render_template('auth/register.html',
                           title=title,
                           form=form)


@auth.route('/logout')
@login_required
def logout():
    if 'user' in session:
        session.pop('user', None)

    return redirect(url_for('main.index'))
