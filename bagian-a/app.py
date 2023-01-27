from flask import Flask, flash, request, redirect, url_for, render_template, Markup
import os
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

app = Flask(__name__, static_folder=join(dirname(realpath(__file__)), 'static/'))

# MEMBUAT DIR KALAU BELUM ADA
INPUT_FOLDER = join(dirname(realpath(__file__)), 'static/file/input/')
os.makedirs(INPUT_FOLDER, exist_ok=True)
OUTPUT_FOLDER = join(dirname(realpath(__file__)), 'static/file/output/')
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.secret_key = "afandanliza"
app.config['INPUT_FOLDER'] = INPUT_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['PREFIX_INPUT'] = "input_"
app.config['PREFIX_OUTPUT'] = "output_"
app.config['MAX_CONTENT_LENGTH'] = 120 * 1024 * 1024

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/input/<filename>')
def display_org(filename):
    return redirect(url_for('static', filename='file/input/' + app.config['PREFIX_INPUT'] + filename), code=301)

@app.route('/compressed/<filename>')
def display_comp(filename):
    return redirect(url_for('static', filename='file/output/' + app.config['PREFIX_OUTPUT']+ filename), code=301)

if __name__ == "__main__":
    app.run(debug=True)
