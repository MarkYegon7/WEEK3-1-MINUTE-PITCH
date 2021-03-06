from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
    title = StringField('Title',validators=[InputRequired()])
    description = TextAreaField("What would you like to pitch ?",validators=[InputRequired()])
    category = RadioField('Label',choices=[ ('pickupline','pickupline'),('interviewpitch','interviewpitch'),('productpitch','productpitch'),('promotionpitch','promotionpitch')],validators=[InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    description = TextAreaField('Add comment',validators=[InputRequired()])
    submit = SubmitField()

class UpvoteForm(FlaskForm):
    submit = SubmitField()

class Downvote(FlaskForm):
    submit = SubmitField()