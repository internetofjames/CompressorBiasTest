import functools
import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db
from flaskr.register import load_subject, register_required

bp = Blueprint('question', __name__, url_prefix='/survey/question')

questions = os.listdir('flaskr/static/audio')

# Lots of redundant code because all 45 questions have the same method minus the question count
# Could not figure out how to pass question_count parameter to create subroutes

@bp.route('/1', methods=('GET', 'POST'))
@register_required
def question1():
    question_count = 1
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question2'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/2', methods=('GET', 'POST'))
@register_required
def question2():
    question_count = 2
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question3'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/3', methods=('GET', 'POST'))
@register_required
def question3():
    question_count = 3
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question4'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/4', methods=('GET', 'POST'))
@register_required
def question4():
    question_count = 4
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question5'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/5', methods=('GET', 'POST'))
@register_required
def question5():
    question_count = 5
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question6'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/6', methods=('GET', 'POST'))
@register_required
def question6():
    question_count = 6
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question7'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/7', methods=('GET', 'POST'))
@register_required
def question7():
    question_count = 7
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question8'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/8', methods=('GET', 'POST'))
@register_required
def question8():
    question_count = 8
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question9'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/9', methods=('GET', 'POST'))
@register_required
def question9():
    question_count = 9
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question10'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/10', methods=('GET', 'POST'))
@register_required
def question10():
    question_count = 10
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question11'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/11', methods=('GET', 'POST'))
@register_required
def question11():
    question_count = 11
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question12'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/12', methods=('GET', 'POST'))
@register_required
def question12():
    question_count = 12
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question13'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/13', methods=('GET', 'POST'))
@register_required
def question13():
    question_count = 13
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question14'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/14', methods=('GET', 'POST'))
@register_required
def question14():
    question_count = 14
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question15'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/15', methods=('GET', 'POST'))
@register_required
def question15():
    question_count = 15
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question16'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/16', methods=('GET', 'POST'))
@register_required
def question16():
    question_count = 16
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question17'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/17', methods=('GET', 'POST'))
@register_required
def question17():
    question_count = 17
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question18'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/18', methods=('GET', 'POST'))
@register_required
def question18():
    question_count = 18
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question19'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/19', methods=('GET', 'POST'))
@register_required
def question19():
    question_count = 19
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question20'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/20', methods=('GET', 'POST'))
@register_required
def question20():
    question_count = 20
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question21'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/21', methods=('GET', 'POST'))
@register_required
def question21():
    question_count = 21
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question22'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/22', methods=('GET', 'POST'))
@register_required
def question22():
    question_count = 22
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question23'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/23', methods=('GET', 'POST'))
@register_required
def question23():
    question_count = 23
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question24'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/24', methods=('GET', 'POST'))
@register_required
def question24():
    question_count = 24
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question25'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/25', methods=('GET', 'POST'))
@register_required
def question25():
    question_count = 25
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question26'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/26', methods=('GET', 'POST'))
@register_required
def question26():
    question_count = 26
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question27'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/27', methods=('GET', 'POST'))
@register_required
def question27():
    question_count = 27
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question28'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/28', methods=('GET', 'POST'))
@register_required
def question28():
    question_count = 28
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question29'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/29', methods=('GET', 'POST'))
@register_required
def question29():
    question_count = 29
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question30'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/30', methods=('GET', 'POST'))
@register_required
def question30():
    question_count = 30
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question31'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/31', methods=('GET', 'POST'))
@register_required
def question31():
    question_count = 31
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question32'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/32', methods=('GET', 'POST'))
@register_required
def question32():
    question_count = 32
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question33'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/33', methods=('GET', 'POST'))
@register_required
def question33():
    question_count = 33
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question34'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/34', methods=('GET', 'POST'))
@register_required
def question34():
    question_count = 34
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question35'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/35', methods=('GET', 'POST'))
@register_required
def question35():
    question_count = 35
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question36'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/36', methods=('GET', 'POST'))
@register_required
def question36():
    question_count = 36
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question37'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/37', methods=('GET', 'POST'))
@register_required
def question37():
    question_count = 37
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question38'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/38', methods=('GET', 'POST'))
@register_required
def question38():
    question_count = 38
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question39'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/39', methods=('GET', 'POST'))
@register_required
def question39():
    question_count = 39
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question40'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/40', methods=('GET', 'POST'))
@register_required
def question40():
    question_count = 40
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question41'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/41', methods=('GET', 'POST'))
@register_required
def question41():
    question_count = 41
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question42'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/42', methods=('GET', 'POST'))
@register_required
def question42():
    question_count = 42
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question43'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/43', methods=('GET', 'POST'))
@register_required
def question43():
    question_count = 43
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question44'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/44', methods=('GET', 'POST'))
@register_required
def question44():
    question_count = 44
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('question.question45'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)

@bp.route('/45', methods=('GET', 'POST'))
@register_required
def question45():
    question_count = 45
    db = get_db()
    current_question = db.execute(
        'SELECT * FROM survey WHERE question_name = ?', (questions[question_count],)
    ).fetchone()
    currentQuestion = current_question['question_name']
    unprocessedSample = current_question['unprocessedSample']
    sampleA = current_question['sampleA']
    sampleB = current_question['sampleB']

    if request.method == 'POST':
        answer = request.form['answer']
        error = None

        if not answer:
            error = 'Please select an answer'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            db.execute(
                'INSERT INTO question (question_id, answer, subject_id) VALUES (?, ?, ?)',
                (currentQuestion, answer, g.subject['id'])
            )
            db.commit()
            return redirect(url_for('register.thankyou'))

    return render_template('question/question_page.html', question_count=question_count, currentQuestion=currentQuestion, unprocessedSample=unprocessedSample, sampleA=sampleA, sampleB=sampleB)
