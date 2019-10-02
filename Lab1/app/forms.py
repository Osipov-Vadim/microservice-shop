from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class PaymentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    status = SelectField('Card Authorization Info', 
        choices=[('AUTHORIZED',"AUTHORIZED"), ('UNAUTHORIZED',"UNAUTHORIZED")])
    submit = SubmitField('Sign In')
