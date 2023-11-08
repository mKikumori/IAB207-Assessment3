
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, DateTimeField, IntegerField, SelectField
from wtforms.validators import InputRequired, Regexp, Email, EqualTo, Length
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

# creates the login information


class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[
                            InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[
                             InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form


class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[
                           Email("Please enter a valid email")])
    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    # submit button
    submit = SubmitField("Register")

# User comment


class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')

# Create Music Show Form


class MusicShowForm(FlaskForm):
    name = StringField("Enter show name...", validators=[InputRequired()])
    description = TextAreaField(
        "Enter show's description", validators=[InputRequired()])
    image = FileField('Show Image', validators=[FileRequired(message='Image cannot be empty'), FileAllowed(
        ALLOWED_FILE, message='Only supports pnj, jpg, JPG, PNG')])
    genre = StringField('Genre', validators=[InputRequired()])
    status = StringField('Status', validators=[InputRequired()])
    start_date = DateTimeField(
        'Show Start Date', format="%d/%m/%Y %H:%M %p", validators=[InputRequired()])
    end_date = DateTimeField(
        'Show End Date', format="%d/%m/%Y %H:%M %p", validators=[InputRequired()])
    artists = StringField('Show Artists', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    num_tickets_avaliable = IntegerField(
        'Number of Tickets Avaliable', validators=[InputRequired()])
    promocode = IntegerField('Promocode', validators=[InputRequired()])
    submit = SubmitField("Create")


class BookingForm(FlaskForm):
    name = StringField("Enter the show's name:",
                       validators=[InputRequired()])
    ticket_type = SelectField(choices=[1, 2, 3])
    ticket_type_selection = SelectField(choices=[1, 2, 3])
    ticket_number = IntegerField(
        "Enter the number of tickets wanted:", validators=[InputRequired()])
    card_number = StringField(
        "Enter card number:", validators=[InputRequired(), Regexp("^(?:4[0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}|[25][1-7][0-9]{2}-[0-9]{4}-[0-9]{4}-[0-9]{4}|6(?:011|5[0-9][0-9])-[0-9]{4}-[0-9]{4}-[0-9]{4}|3[47][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}|3(?:0[0-5]|[68][0-9])-[0-9]{4}-[0-9]{4}-[0-9]{4}|(?:2131|1800|35\d{3})-[0-9]{4}-[0-9]{4}-[0-9]{4})$",
        "Enter card number: (Expected ####-####-####-####)", validators=[InputRequired(), Regexp("^(?:4[0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}|[25][1-7][0-9]{2}-[0-9]{4}-[0-9]{4}-[0-9]{4}|6(?:011|5[0-9][0-9])-[0-9]{4}-[0-9]{4}-[0-9]{4}|3[47][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}|3(?:0[0-5]|[68][0-9])-[0-9]{4}-[0-9]{4}-[0-9]{4}|(?:2131|1800|35\d{3})-[0-9]{4}-[0-9]{4}-[0-9]{4})$",
                                                                  message="Not valid card number")])
    CVS = IntegerField("Enter card's VCS:", validators=[InputRequired()])
    CVS = IntegerField("Enter card's CVS: (Expected ####)", validators=[InputRequired()])
    expiry_date = DateTimeField(
        "Enter card's expiry date (mm/YYYY):", validators=[InputRequired()], format="%m/%Y")
    emailid = StringField("Enter your email:", validators=[
