#!/bin/bash/python3
"""
This module is responsible for the configuration of the routes to
encrypt and decrypt the data of the user.

Below are some libraries that will be used in this module
"""
from flask import Flask, request, make_response, render_template, send_file, jsonify
#from flask_cors import CORS
import os
import zipfile
import subprocess
import codecs

app = Flask(__name__)
#CORS(app)

@app.route('/encrypt_file', methods=['POST'])
def encrypt():
    """
    #This function will handle the route '/upload' and
    #later encrypt the file uploaded by the user
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

@app.route('/decrypt_file', methods=['POST'])
def decrypt_file():
    """
    This route decrypts the encrypted file uploaded by the user
    """
    if request.method=='POST':
        
        #if 'file' not in request.files:
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



@app.route('/e_text', methods=['POST'])
def encrypt_text():
    """
    Route to encrypt text
    """
    if request.method == 'POST':
        text = request.form['text'].encode('utf-8')
        password = request.form['password']

        salt = b'secure_salt'
        iterations = 100000  


        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  
            salt=salt,
            iterations=iterations,
            backend=default_backend()
        )

        key = base64.urlsafe_b64encode(kdf.derive(password.encode())) 
        
        cypher_suit = Fernet(key)

        cypher_text = cypher_suit.encrypt(text).decode('utf-8')

        data = {'key': cypher_text}
        return jsonify(data)
        #return render_template('index3.html', key=key, result=cypher_text)
    return "ERROr"

@app.route('/d_text', methods=['POST'])
def decrypt_text():
    """
    Route to decrypt text
    """
    if request.method=='POST':
        text = request.form['d_text'].encode('utf-8')
        password = request.form['password']

        salt = b'secure_salt'  
        iterations = 100000  


        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  
            salt=salt,
            iterations=iterations,
            backend=default_backend()
        )

        key = base64.urlsafe_b64encode(kdf.derive(password.encode())) 
        try:
            cipher_suite = Fernet(key)

            normal_text = cipher_suite.decrypt(text).decode('utf-8')

            data = {'key': normal_text}
            return jsonify(data)
            #return render_template('index3.html', result2=normal_text)
        except (ValueError, KeyError):
            return 'Error: Invalid key'
    return 'Error'

if __name__ == '__main__':
    app.run(debug=True)

