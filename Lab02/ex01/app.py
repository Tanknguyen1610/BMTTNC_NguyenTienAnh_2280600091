from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

#router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

#router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()

    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#router routes for Vigenere cipher
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain'] # Vigenere key is a string (key)
    Vigenere = VigenereCipher()

    encrypted_text = Vigenere.encrypt_text(text, key)
    return f"Plain text: {text}<br/>Keyword: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher'] # Vigenere key is a string (keyword)
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.decrypt_text(text, key)
    return f"Cipher text: {text}<br/>Keyword: {key}<br/>Decrypted text: {decrypted_text}"


#router routes for Playfair cipher
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeywordPlain'] # Playfair key is a string (keyword)
    Playfair = PlayfairCipher()

    encrypted_text = Playfair.encrypt_text(text, key)
    return f"Plain text: {text}<br/>key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeywordCipher'] # Playfair key is a string (keyword)
    Playfair = PlayfairCipher()
    decrypted_text = Playfair.decrypt_text(text, key)
    return f"Cipher text: {text}<br/>key: {key}<br/>Decrypted text: {decrypted_text}"


#router routes for Transposition cipher
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain'] # Transposition key is typically a string (e.g., "KEY")
    Transposition = TranspositionCipher()

    encrypted_text = Transposition.encrypt_text(text, key)
    return f"Plain text: {text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher'] # Transposition key is typically a string (e.g., "KEY")
    Transposition = TranspositionCipher()
    decrypted_text = Transposition.decrypt_text(text, key)
    return f"Cipher text: {text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"

#router routes for Rail Fence cipher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputRailsPlain']) # Key for Rail Fence is number of rails
    RailFence = RailFenceCipher()

    encrypted_text = RailFence.encrypt_text(text, key)
    return f"Plain text: {text}<br/>Number of Rails: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputRailsCipher']) # Key for Rail Fence is number of rails
    RailFence = RailFenceCipher()
    decrypted_text = RailFence.decrypt_text(text, key)
    return f"Cipher text: {text}<br/>Number of Rails: {key}<br/>Decrypted text: {decrypted_text}"

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)