from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required



class PitchForm(FlaskForm):
    pitch_title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('your pitch', validators=[Required()])
    category = SelectField('Pitch Category', choices = [('pickup','Pickup Lines'), ('interview', 'Interview'), ('promotion','Promotion'), ('product', 'Product')], validators=[Required()])
    submit = SubmitField('Submit Pitch')


class updateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave your comment here:',validators=[Required()])
    submit = SubmitField('Submit')    