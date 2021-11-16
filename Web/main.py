from flask import Flask, render_template, flash, redirect, url_for, request
from forms import SubmitForm
from options import Options
from formater import CustomFormatter
import sys
import random
import pickle
import joblib
import numpy as np

app = Flask(__name__)

app.config["SECRET_KEY"] = "12345"

# model = joblib.load("../finalized_model.pkl")

# def predict(form):
#    form_formatted = CustomFormatter(form)
#    return round(np.log(model.predict(form_formatted.df))[0], 2)

@app.route("/",  methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    form = SubmitForm(request.form)
    options = Options()
    if request.form:
        if form.validate_on_submit():
            return render_template('home.html', title="Home", form=SubmitForm(), prediksjon=predict(form), options=options)
        else:
            return render_template('home.html', title="Home", form=form, invalid=True, options=options)
    return render_template('home.html', title="Home", form=form, options=options)


if __name__ == "__main__":
    app.run(debug=True)