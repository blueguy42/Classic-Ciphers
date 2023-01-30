from flask import Flask, flash, request, redirect, url_for, render_template, Markup
import os
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

from ciphers.vigenere import cipher as vigenere_cipher
from ciphers.affine import cipher as affine_cipher
from ciphers.playfair import cipher as playfair_cipher
from ciphers.hill import cipher as hill_cipher

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
    return render_template("home.html")

@app.route('/input/<filename>')
def display_org(filename):
    return redirect(url_for('static', filename='file/input/' + app.config['PREFIX_INPUT'] + filename), code=301)

@app.route('/compressed/<filename>')
def display_comp(filename):
    return redirect(url_for('static', filename='file/output/' + app.config['PREFIX_OUTPUT']+ filename), code=301)

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    if request.method == 'POST':
        print("1")
        operation = request.form['operation']
        input_method = request.form['input_method'] 
        msg = request.form['msg']
        key = request.form['key']
        type = request.form['type']

        result = vigenere_cipher(msg, key, operation, type)
        print(result)
        return render_template("vigenere.html", result=result)
    else:
        print("2")
        return render_template("vigenere.html")


@app.route('/affine', methods=['GET', 'POST'])
def affine():
    if request.method == 'POST':
        print("1")
        operation = request.form['operation']
        input_method = request.form['input_method'] 
        msg = request.form['msg']
        key_m = int(request.form['key_m'])
        key_b = int(request.form['key_b'])
        n_char = int(request.form['n_char'])

        result = affine_cipher(msg, key_m, key_b, operation, n_char)
        print(result)
        return render_template("affine.html", result=result)
    else:
        print("2")
        return render_template("affine.html")

@app.route('/playfair', methods=['GET', 'POST'])
def playfair(): 
    if request.method == 'POST':
        print("1")
        operation = request.form['operation']
        input_method = request.form['input_method']
        msg = request.form['msg']
        key = request.form['key']

        result = playfair_cipher(msg, key, operation)
        print(result)
        return render_template("playfair.html", result=result)
    else:
        print("2")
        return render_template("playfair.html")

@app.route('/hill', methods=['GET', 'POST'])
def hill():
    if request.method == 'POST':
        print("1")
        operation = request.form['operation']
        input_method = request.form['input_method'] 
        msg = request.form['msg']
        key= request.form['key']
        size = int(request.form['size'])

        result = hill_cipher(msg, key, size, operation)
        print(result)
        return render_template("hill.html", result=result)
    else:
        print("2")
    return render_template("hill.html")
    


if __name__ == "__main__":
    app.run(debug=True)
