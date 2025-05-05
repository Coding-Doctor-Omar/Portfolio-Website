from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from datetime import datetime
from forms import ContactForm
from smtplib import SMTP
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("APP_SECRET_KEY")


bootstrap = Bootstrap5(app)

def send_mail(name, mail, phone_num, message):
    """Sends user's message to the website owner."""
    sender_email = os.environ.get("sender_email")
    password = os.environ.get("gmail_app_pass")

    try:
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=sender_email,
                msg=f"Subject:Client Contact Message\n\nName: {name}\nEmail: {mail}\nPhone Number: {phone_num}\n\nMessage:\n{message}"
            )
    except:
        return False
    else:
        return True


@app.route("/")
def home():
    now = datetime.today()
    return render_template("index.html", page_name="Home", year=now.year)

@app.route("/projects")
def projects():
    now = datetime.today()
    return render_template("projects.html", page_name="Projects", year=now.year)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    now = datetime.today()
    submission_status = False
    contact_form = ContactForm()

    if contact_form.validate_on_submit():
        name = contact_form.name.data
        email = contact_form.email.data
        phone_number = contact_form.phone_number.data
        message = contact_form.msg.data

        if send_mail(name=name, mail=email, phone_num=phone_number, message=message):
            submission_status = True
        else:
            submission_status = False

        contact_form.name.data = ""
        contact_form.email.data = ""
        contact_form.phone_number.data = ""
        contact_form.msg.data = ""



    return render_template("contact.html", page_name="Contact", year=now.year, form=contact_form, submitted=submission_status)


if __name__ == "__main__":
    app.run(debug=True)
