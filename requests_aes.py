#!/bin/bash/python3
"""
This module is responsible for the configuration of the routes to
encrypt and decrypt the data of the user.

Below are some libraries that will be used in this module
"""
from flask import Flask, request, make_response, render_template, send_file
import os
import zipfile
import subprocess
import codecs

app = Flask(__name__)

@app.route('/')
def index():
    """
    Defining a function to render the landing page
    """
    return render_template('index2.html')

@app.route('/process', methods=['POST'])
def process():
    """
    Route to test the flask app
    """
    if request.method == 'POST':
        user_name = request.form['fname']
        return render_template('results.html', user_name=user_name)
    
    return render_template('error.html')


@app.route('/upload', methods=['POST'])
def encrypt():
    """
    This function will handle the route '/upload' and
    later encrypt the file uploaded by the user
    """
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No files"
        
        file = request.files['file']

        if file.filename == '':
            return "No file selected"
        
        file_path = file.filename
        file.save(file_path)  # Save the uploaded file

        password = request.form['password']
        
        encrypt_cmd = [
                "openssl", "enc", "-aes-256-cbc", "-salt",
                "-in", file_path, "-pass", f"pass:{password}"
                ]

        try:
            encrypted = subprocess.check_output(encrypt_cmd)
            #encrypted_text = encrypted.decode('utf-8')

            encrypted_file_path = "encrypted_file.enc"
            with open(encrypted_file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

            return send_file(encrypted_file_path, as_attachment=True)

        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
       
    return render_template('error.html')


@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    """
    This route decrypts the encrypted file uploaded by the user
    """
    if request.method=='POST':
        
        #if 'file' not in request.files['encrypted']:
         #   return "No files"

        encrypted_file = request.files['encrypted']
        password = request.form['password']

        encrypted_file_path = encrypted_file.filename
        encrypted_file.save(encrypted_file_path)

        decrypt = [
                "openssl", "enc", "-d", "-aes-256-cbc",
                "-in", encrypted_file_path, "-pass", f"pass:{password}"
                ]
        try:
            decrypted_output = subprocess.check_output(decrypt)

            # Encode the decrypted output as UTF-8
            decrypted_text = decrypted_output.decode('utf-8')

            # Write the UTF-8 encoded content to a new file
            decrypted_file_path = "decrypted_file.txt"
            with open(decrypted_file_path, 'w', encoding='utf-8') as decrypted_file:
                decrypted_file.write(decrypted_text)

            return send_file(decrypted_file_path, as_attachment=True)
        
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"


    return render_template("error.html")


if __name__ == '__main__':
    app.run(debug=True)

