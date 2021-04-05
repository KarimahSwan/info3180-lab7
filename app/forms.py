from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    description=StringField('Description', widget=TextArea(), validators=[DataRequired()])
    image=FileField('Image',validators=[FileRequired(), FileAllowed(['jpg','png'], 'Please Upload Images Only!')])
   
