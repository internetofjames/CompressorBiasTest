import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db
bp = Blueprint('register', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        db = get_db()
        error = None

        if not firstName:
            error = 'First name is required.'
        elif not lastName:
            error = 'Last name is required.'
        elif not email:
            error = 'Email is required.'
        elif db.execute(
            'SELECT id FROM subject WHERE email = ?', (email,)
        ).fetchone() is not None:
            error = 'Email {} is already registered. Please use a different one'.format(email)

        if error is None:
            db.execute(
                'INSERT INTO subject (lastName, firstName, email) VALUES (?, ?, ?)',
                (lastName, firstName, email)
            )
            db.commit()
            subject = db.execute(
            'SELECT * FROM subject WHERE email = ?', (email,)
            ).fetchone()
            session.clear()
            session['subject_id'] = subject['id']
            return redirect(url_for('register.survey_info'))

        flash(error)

    return render_template('register/index.html')

@bp.route('/survey', methods=('GET','POST'))
def survey_info():
    if request.method == 'POST':
        return redirect(url_for('question.question'))
    return render_template('register/survey.html')

@bp.route('/thankyou', methods=('GET', 'POST'))
def thankyou():
    if request.method == 'POST':
        return redirect(url_for('register.logout'))
    return render_template('register/thankyou.html')

@bp.before_app_request
def load_subject():
    subject_id = session.get('subject_id')

    if subject_id is None:
        g.subject = None
    else:
        g.subject = get_db().execute(
            'SELECT * FROM subject WHERE id = ?', (subject_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def register_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.subject is None:
            return redirect(url_for('index'))

        return view(**kwargs)

    return wrapped_view
