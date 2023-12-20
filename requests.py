#!/bin/bash/python3
from flask import Flask, request, render_template, send_file
import os
import zipfile
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        user_name = request.form['fname']
        return render_template('results.html', user_name=user_name)
    
    return render_template('error.html')


@app.route('/upload', methods=['POST'])
def encrypt():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No files"
        
        file = request.files['file']

        if file.filename == '':
            return "No file selected"
        
        file.save(file.filename)  # Save the uploaded file

        password = request.form['password']
        subprocess.run(
            [
                "openssl", "genpkey", "-algorithm", "RSA", "-out", "private.pem",
                "-pass", f"pass:{password}"
            ]
        )
        subprocess.run(
            [
                "openssl", "rsa", "-in", "./private.pem", "-pubout", "-out", "public.pem",
                "-passin", f"pass:{password}"
            ]
        )

        with open(file.filename, 'rb') as f:
            file_content = f.read()

        with open('encrypted_file.enc', 'wb') as encrypted_file:
            subprocess.run(
                [
                    "openssl", "pkeyutl", "-encrypt", "-in", "-", "-out", "-", "-pubin", "-inkey", "./public.pem"
                ],
                input=file_content,
                stdout=encrypted_file
            )
        os.remove(f'{file.filename}')

        return render_template('index2.html')
    
    return render_template('error.html')

@app.route('/download')
def encrypted_download():
    files = ['./private.pem', './public.pem', './encrypted_file.enc']
    zip_file = 'encrypted_data.zip'

    with zipfile.ZipFile(zip_file, 'w') as zipf:
        for file_path in files:
            zipf.write(file_path)

    os.remove('private.pem')
    os.remove('public.pem')
    os.remove('encrypted_file.enc')
    

    return send_file(zip_file, as_attachment=True, download_name='encrypted_file.zip')

@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No files"
        
        encrypted_file = request.files['encrypted']
        private_key = request.files['private']
        password = request.form['password']

        if encrypted_file.filename == '':
            return "No file selected"
        if private_key.filename == '':
            return "No file selected"
        
        encrypted_file.save(encrypted_file.filename)
        private_key.save(private_key.filename)

        with open(encrypted_file.filename, 'rb') as f:
          file_content = f.read()

        with open(private_key.filename, 'rb') as f:
          key_content = f.read()

        
        with open('decrypted_file', 'wd') as d:

            subprocess.run(
                ["openssl", "-pkeyutl", "-decrypt", "-in", "-", "-out", "-",
                "-inkey", f"{key_content}", "-pass", f"pass:{password}"],
                input=file_content,
                stdout=d
            )
        
        return render_template('index2.html')
    
    return render_template("error.html")

@app.route('/decrypt/download')
def d_download():
    file = './decrypted_file'

    return send_file(file, as_attachment=True, download_name="Decrypted file")


if __name__ == '__main__':
    app.run(debug=True)
