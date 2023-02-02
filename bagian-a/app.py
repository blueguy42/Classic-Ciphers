from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
import datetime

from ciphers.vigenere import cipher as vigenere_cipher
from ciphers.affine import cipher as affine_cipher
from ciphers.playfair import cipher as playfair_cipher
from ciphers.hill import cipher as hill_cipher
import ciphers.stringparser as sp

app = Flask(__name__, static_folder=join(dirname(realpath(__file__)), 'static/'))

# MEMBUAT DIR KALAU BELUM ADA
INPUT_FOLDER = join(dirname(realpath(__file__)), 'static/file/input/')
os.makedirs(INPUT_FOLDER, exist_ok=True)
OUTPUT_FOLDER = join(dirname(realpath(__file__)), 'static/file/output/')
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.secret_key = "afandanliza"
app.config['INPUT_FOLDER'] = INPUT_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 120 * 1024 * 1024

@app.route("/")
def home():
    return redirect(url_for('vigenere'))

@app.route('/input/<filename>')
def display_input(filename):
    return redirect(url_for('static', filename='file/input/' + filename), code=301)

@app.route('/compressed/<filename>')
def display_output(filename):
    return redirect(url_for('static', filename='file/output/' + filename), code=301)

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    if request.method == 'POST':
        try:
            operation = request.form['operation']
            type = request.form['type']
            input_method = request.form['input_method'] 
            key = request.form['key']

            if input_method == "file":
                file = request.files['msg']
                if file.filename and operation and type and input_method and key:
                    filename = secure_filename(file.filename)

                    if (type == "standard" or type == "autokey") and not filename.lower().endswith(".txt"):
                        flash("Please input a .txt file!")
                        return render_template("vigenere.html")

                    extension = ""
                    if '.' in filename:
                        extension = "." + filename.split('.')[-1]

                    date = datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S%f')[:-3]
                    nameFile = f"vigenere_{operation}_{type}_{input_method}_{date}{extension}"
                    saved_filename = os.path.join(app.config['INPUT_FOLDER'], nameFile)
                    file.save(saved_filename)
                    msg = ''
                    if (type == "standard" or type == "autokey"):
                        f = open(saved_filename, "r")
                        msg = f.read()
                        f.close()
                    else:
                        f = open(saved_filename, "rb")
                        msg = f.read()
                        f.close()

                    result = vigenere_cipher(msg, key, operation, type)
                    saved_output = os.path.join(app.config['OUTPUT_FOLDER'], nameFile)
                    if (type == "standard" or type == "autokey"):
                        f = open(saved_output, "w")
                        f.write(result['result'])
                        f.close()
                    else:
                        f = open(saved_output, "wb")
                        f.write(result['result'])
                        f.close()

                    return render_template("vigenere.html", result=result['result'], type=type, filename=nameFile)
                else:
                    flash("Please fill all the fields!")
                    return render_template("vigenere.html")
            elif input_method == "manual":
                msg = request.form['msg']
                if operation and type and input_method and msg and key:
                    date = datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S%f')[:-3]
                    nameFile = f"vigenere_{operation}_{type}_{input_method}_{date}.txt"
                    saved_filename = os.path.join(app.config['INPUT_FOLDER'], nameFile)
                    f = open(saved_filename, "w")
                    f.write(msg)
                    f.close()

                    saved_output = os.path.join(app.config['OUTPUT_FOLDER'], nameFile)
                    if type=="extended":
                        msg = bytes(sp.stringToASCII(msg))
                        result = vigenere_cipher(msg, key, operation, type)
                        f = open(saved_output, "wb")
                        f.write(result['result'])
                        f.close()
                        result['result'] = sp.ASCIItoString(result['result'])
                    else:
                        result = vigenere_cipher(msg, key, operation, type)
                        f = open(saved_output, "w")
                        f.write(result['result'])
                        f.close()

                    return render_template("vigenere.html", result=result['result'], type=type, filename=nameFile)
                else:
                    flash("Please fill all the fields!")
                    return render_template("vigenere.html")
        except Exception as e:
            flash(f"Error: {repr(e)}")
            return render_template("vigenere.html")
    else:
        return render_template("vigenere.html")
    return render_template("vigenere.html")


@app.route('/affine', methods=['GET', 'POST'])
def affine():
    if request.method == 'POST':
        try:
            operation = request.form['operation']
            input_method = request.form['input_method']
            key_m = request.form['key_m']
            key_b = request.form['key_b']
            n_char = request.form['n_char']

            if input_method == "file":
                file = request.files['msg']
                if file.filename and operation and input_method and key_m and key_b and n_char:
                    filename = secure_filename(file.filename)
                    key_m = int(key_m)
                    key_b = int(key_b)
                    n_char = int(n_char)

                    if n_char == 26 and not filename.lower().endswith(".txt"):
                        flash("Please input a .txt file!")
                        return render_template("affine.html")

                    extension = ""
                    if '.' in filename:
                        extension = "." + filename.split('.')[-1]

                    date = datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S%f')[:-3]
                    nameFile = f"affine_{operation}_{n_char}_{input_method}_{date}{extension}"
                    saved_filename = os.path.join(app.config['INPUT_FOLDER'], nameFile)
                    file.save(saved_filename)
                    msg = ''
                    if n_char == 26:
                        f = open(saved_filename, "r")
                        msg = f.read()
                        f.close()
                    else:
                        f = open(saved_filename, "rb")
                        msg = f.read()
                        f.close()

                    result = affine_cipher(msg, key_m, key_b, operation, n_char)
                    if 'error' in result:
                        flash(result['error'])
                        return render_template("affine.html")
                    saved_output = os.path.join(app.config['OUTPUT_FOLDER'], nameFile)
                    if n_char == 26:
                        f = open(saved_output, "w")
                        f.write(result['result'])
                        f.close()
                    else:
                        f = open(saved_output, "wb")
                        f.write(result['result'])
                        f.close()

                    return render_template("affine.html", result=result['result'], n_char=n_char, filename=nameFile)
                else:
                    flash("Please fill all the fields!")
                    return render_template("affine.html")
            elif input_method == "manual":
                msg = request.form['msg']
                if msg and operation and input_method and key_m and key_b and n_char:
                    key_m = int(key_m)
                    key_b = int(key_b)
                    n_char = int(n_char)

                    date = datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S%f')[:-3]
                    nameFile = f"affine_{operation}_{n_char}_{input_method}_{date}.txt"
                    saved_filename = os.path.join(app.config['INPUT_FOLDER'], nameFile)
                    f = open(saved_filename, "w")
                    f.write(msg)
                    f.close()

                    saved_output = os.path.join(app.config['OUTPUT_FOLDER'], nameFile)
                    if n_char == 256:
                        msg = bytes(sp.stringToASCII(msg))
                        result = affine_cipher(msg, key_m, key_b, operation, n_char)
                        if 'error' in result:
                            flash(result['error'])
                            return render_template("affine.html")
                        f = open(saved_output, "wb")
                        f.write(result['result'])
                        f.close()
                        result['result'] = sp.ASCIItoString(result['result'])
                    else:
                        result = affine_cipher(msg, key_m, key_b, operation, n_char)
                        if 'error' in result:
                            flash(result['error'])
                            return render_template("affine.html")
                        f = open(saved_output, "w")
                        f.write(result['result'])
                        f.close()

                    return render_template("affine.html", result=result['result'], n_char=n_char, filename=nameFile)
                else:
                    flash("Please fill all the fields!")
                    return render_template("affine.html")    
        except Exception as e:
            flash(f"Error: {repr(e)}")
            return render_template("affine.html")
    else:
        return render_template("affine.html")
    return render_template("affine.html")

@app.route('/playfair', methods=['GET', 'POST'])
def playfair(): 
    if request.method == 'POST':
        try:
            operation = request.form['operation']
            input_method = request.form['input_method']
            key = request.form['key']

            if input_method == "file":
                file = request.files['msg']
                if file.filename and operation and input_method and key:
                    filename = secure_filename(file.filename)

                    if not filename.lower().endswith(".txt"):
                        flash("Please input a .txt file!")
                        return render_template("playfair.html")

                    extension = ""
                    if '.' in filename:
                        extension = "." + filename.split('.')[-1]

                    date = datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S%f')[:-3]
                    nameFile = f"playfair_{operation}_{input_method}_{date}{extension}"
                    saved_filename = os.path.join(app.config['INPUT_FOLDER'], nameFile)
                    file.save(saved_filename)
                    msg = ''

                    f = open(saved_filename, "r")
                    msg = f.read()
                    f.close()

                    result = playfair_cipher(msg, key, operation)
                    saved_output = os.path.join(app.config['OUTPUT_FOLDER'], nameFile)

                    f = open(saved_output, "w")
                    f.write(result['result'])
                    f.close()

                    return render_template("playfair.html", result=result['result'], filename=nameFile)
                else:
                    flash("Please fill all the fields!")
                    return render_template("playfair.html")
            elif input_method == "manual":
                msg = request.form['msg']
                if msg and operation and input_method and key:
                    date = datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S%f')[:-3]
                    nameFile = f"playfair_{operation}_{input_method}_{date}.txt"
                    saved_filename = os.path.join(app.config['INPUT_FOLDER'], nameFile)
                    f = open(saved_filename, "w")
                    f.write(msg)
                    f.close()

                    saved_output = os.path.join(app.config['OUTPUT_FOLDER'], nameFile)
                    result = playfair_cipher(msg, key, operation)
                    saved_output = os.path.join(app.config['OUTPUT_FOLDER'], nameFile)

                    f = open(saved_output, "w")
                    f.write(result['result'])
                    f.close()

                    return render_template("playfair.html", result=result['result'], filename=nameFile)
                else:
                    flash("Please fill all the fields!")
                    return render_template("playfair.html")    
        except Exception as e:
            flash(f"Error: {repr(e)}")
            return render_template("playfair.html")
    else:
        return render_template("playfair.html")
    return render_template("playfair.html")

@app.route('/hill', methods=['GET', 'POST'])
def hill():
    if request.method == 'POST':
        try:
            operation = request.form['operation']
            input_method = request.form['input_method']
            key = request.form['key']
            size = request.form['size']

            if input_method == "file":
                file = request.files['msg']
                if file.filename and operation and input_method and key and size:
                    filename = secure_filename(file.filename)
                    size = int(size)

                    if not filename.lower().endswith(".txt"):
                        flash("Please input a .txt file!")
                        return render_template("hill.html")

                    extension = ""
                    if '.' in filename:
                        extension = "." + filename.split('.')[-1]

                    date = datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S%f')[:-3]
                    nameFile = f"hill_{operation}_{input_method}_{date}{extension}"
                    saved_filename = os.path.join(app.config['INPUT_FOLDER'], nameFile)
                    file.save(saved_filename)
                    msg = ''
                    
                    f = open(saved_filename, "r")
                    msg = f.read()
                    f.close()

                    result = hill_cipher(msg, key, size, operation)
                    if 'error' in result:
                        flash(result['error'])
                        return render_template("hill.html")
                    saved_output = os.path.join(app.config['OUTPUT_FOLDER'], nameFile)

                    f = open(saved_output, "w")
                    f.write(result['result'])
                    f.close()

                    return render_template("hill.html", result=result['result'], filename=nameFile)
                else:
                    flash("Please fill all the fields!")
                    return render_template("hill.html")
            elif input_method == "manual":
                msg = request.form['msg']
                if msg and operation and input_method and key and size:
                    size = int(size)

                    date = datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S%f')[:-3]
                    nameFile = f"hill_{operation}_{input_method}_{date}.txt"
                    saved_filename = os.path.join(app.config['INPUT_FOLDER'], nameFile)
                    f = open(saved_filename, "w")
                    f.write(msg)
                    f.close()

                    saved_output = os.path.join(app.config['OUTPUT_FOLDER'], nameFile)

                    result = hill_cipher(msg, key, size, operation)
                    if 'error' in result:
                        flash(result['error'])
                        return render_template("hill.html")
                    f = open(saved_output, "w")
                    f.write(result['result'])
                    f.close()

                    return render_template("hill.html", result=result['result'], filename=nameFile)
                else:
                    flash("Please fill all the fields!")
                    return render_template("hill.html")    
        except Exception as e:
            flash(f"Error: {repr(e)}")
            return render_template("hill.html")
    else:
        return render_template("hill.html")
    return render_template("hill.html")
    


if __name__ == "__main__":
    app.run(debug=True)
