from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key for session handling

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        name = form.name.data
        email = form.email.data

        # Check if the email is a valid UofT email
        if not email.endswith('@mail.utoronto.ca'):
            flash('Please enter a valid UofT email address ending with @mail.utoronto.ca.')
        else:
            # If email is correct but name has changed
            if old_name and old_name != name:
                flash('Looks like you have changed your name!')
            session['name'] = name
            session['email'] = email
            return redirect(url_for('index'))

    return render_template('index_activity1.4.html', form=form, name=session.get('name'), email=session.get('email'))

if __name__ == '__main__':
    app.run(debug=True)
