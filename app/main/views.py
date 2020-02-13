from flask import render_template, flash, redirect, url_for, request, jsonify, render_template, abort
from . import main_bp as bp
from .form import LoginForm, ServiceForm
from ..models import User, AuthLog, db, Service
from flask_login import current_user, login_user, login_required, logout_user


@bp.route('/', methods=['GET'])
def index():
    services = Service.query.all()
    filtered = []
    for service in services:
        if current_user.is_authenticated is False and service.admin:
            pass
        else:
            filtered.append(service)
    return render_template('index.html', services=filtered)


@bp.route('/auth_log', methods=['GET'])
@login_required
def authentication_log():
    auth_log = AuthLog.query.all()
    return render_template('auth_log.html', auths=auth_log)


@bp.route('/delete_log_activity', methods=['GET'])
@login_required
def delete_log_entry():
    del_id = request.args.get('id')
    AuthLog.query.filter_by(id=del_id).delete()
    db.session.commit()
    return redirect(url_for('main.authentication_log'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.compare_hashes(form.password.data):
            flash('Invalid username or password')
            log_activity("Failure", form.username.data)
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        log_activity("Success", form.username.data)
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Sign In', form=form)


@bp.route('/service', methods=['GET', 'POST'])
@login_required
def add_service():
    """ TODO ERROR MESSAGES"""
    form = ServiceForm()
    if form.validate_on_submit():
        user = Service(name=form.name.data, description=form.description.data, github=form.github.data, status=int(form.status.data),
                       port=form.port.data, admin=int(form.admin.data))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_service.html', title='Add service', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


def log_activity(status, username, ip=None,):
    auth = AuthLog(status, username, ip)
    db.session.add(auth)
    db.session.commit()
