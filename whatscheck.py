from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def has_whatsapp(phone_number):
    url = f"https://wa.me/{phone_number}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if 'Join WhatsApp' in soup.get_text():
            return False
        else:
            return True
    else:
        return False

def is_valid_phone(phone_number):
    # Add your own phone number validation logic if needed
    return True

@app.route('/check-whatsapp', methods=['GET'])
def check_whatsapp():
    phone_number = request.args.get('phone', '')

    if phone_number:
        if is_valid_phone(phone_number):
            is_whatsapp = has_whatsapp(phone_number)
            return jsonify({'has_whatsapp': is_whatsapp, 'phone': phone_number})
        else:
            return jsonify({'error': 'Invalid phone number format'}), 400
    else:
        return jsonify({'error': 'Phone number not provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)

