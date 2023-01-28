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
        print(operation)
        print(input_method)
        print(msg)
        print(key)
        print(type)
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
        key_m = request.form['key_m']
        key_b = request.form['key_b']
        type_char = request.form['type_char']
        print(operation)
        print(input_method)
        print(msg)
        print(key_m)
        print(key_b)
        print(type_char)
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
        print(operation)
        print(input_method)
        print(msg)
        print(key)
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
        size = request.form['size']
        print(operation)
        print(input_method)
        print(msg)
        print(key)
        print(size)
    else:
        print("2")
    
    return render_template("hill.html")
    


if __name__ == "__main__":
    app.run(debug=True)
