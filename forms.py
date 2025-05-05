from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    name = StringField(
        label="Name",
        validators=[DataRequired(), Length(min=3)],
        render_kw={
            "style": "width: 60ch",
            "class": "form-control",
        }
    )

    email = EmailField(
        label="Email",
        validators=[DataRequired(), Email()],
        render_kw={
            "style": "width: 60ch",
            "class": "form-control",
        }
    )

    phone_number = StringField(
        label="Phone Number",
        validators=[DataRequired()],
        render_kw={
            "style": "width: 60ch",
            "class": "form-control",
        }
    )

    msg = TextAreaField(
        label="Message",
        validators=[DataRequired()],
        render_kw={
            "placeholder": "Type your message here",
            "style": "width: 60ch",
            "rows": 4,
            "class": "form-control",
        }
    )

    send = SubmitField(
        label="Send Message",
        render_kw={
            "class": "btn btn-dark",
        }
    )

