from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        # Check for name change
        if session.get('name') != name:
            flash('Looks like you have changed your name!')
            session['name'] = name  # Update session with the new name

        # Check for email change
        if session.get('email') != email:
            flash('Looks like you have changed your email!')
            session['email'] = email  # Update session with the new email

        # Check if email is UofT email
        if not email.endswith('@mail.utoronto.ca'):
            flash('Please use your UofT email.')
            return render_template('index_activity1.4.html', form=form, name=name, email=email)  # Re-render the form

        # Redirect to result page to prevent form resubmission on reload
        return redirect(url_for('index'))

    return render_template('index_activity1.4.html', form=form, name=session.get('name', ''), email=session.get('email', ''))

if __name__ == '__main__':
    app.run(debug=True)
