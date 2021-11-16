from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SubmitForm(FlaskForm):
    device_browser               = StringField("device_browser", validators=[DataRequired(), Length(min=2,max=50)])
    device_operatingSystem       = StringField("device_operatingSystem", validators=[DataRequired(), Length(min=2,max=50)])
    device_isMobile              = StringField("device_isMobile", validators=[DataRequired(), Length(min=2,max=50)])
    geoNetwork_continent         = StringField("geoNetwork_continent", validators=[DataRequired(), Length(min=2,max=50)])
    geoNetwork_country           = StringField("geoNetwork_country", validators=[DataRequired(), Length(min=2,max=50)])

    submit = SubmitField("Predict")