
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, DateTimeField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

#User comment
class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')

# Create Music Show Form
class MusicShowForm(FlaskForm):
    name = StringField("Enter show name...", validators=[InputRequired()])
    description = TextAreaField("Enter show's description", validators = [InputRequired()])
    image = FileField('Show Image', validators=[FileRequired(message='Image cannot be empty'), FileAllowed(ALLOWED_FILE, message='Only supports pnj, jpg, JPG, PNG')])
    genre = StringField('Genre', validators=[InputRequired()])
    status = StringField('Status', validators=[InputRequired()])
    start_date = DateTimeField('Show Start Date', validators=[InputRequired()])
    end_date = DateTimeField('Show End Date', validators=[InputRequired()])
    artists = StringField('Show Artists', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    num_tickets_avaliable = IntegerField('Number of Tickets Avaliable', validators=[InputRequired()])
    promocode = IntegerField('Promocode', validators=[InputRequired()])
    submit = SubmitField("Create")