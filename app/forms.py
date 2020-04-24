from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, NumberRange
from app.models import List, Spell


class SpellForm(FlaskForm):
    sname = StringField('Spell name', validators=[DataRequired()])
    slevel = IntegerField('Spell Level', validators=[DataRequired(),NumberRange(0,9) ])
    verbal = BooleanField('Verbal')
    somatic = BooleanField('Somatic')
    material = BooleanField('Material')
    concentration = BooleanField('Concentration')
    ritual = BooleanField('Ritual')
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ListForm(FlaskForm):
    spells = SelectMultipleField('Spells', coerce=int)
    submit = SubmitField('Submit')
