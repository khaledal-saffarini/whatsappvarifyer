# Import requests library
import requests

# Define the phone number to check
phone_number = "+962791837555885"

# Use the wa.me short URL
# Create the URL
wa_url = f"https://wa.me/{phone_number}"
# Send the request and get the response
response = requests.get(wa_url)
# Check the response status code
if response.status_code == 200:
    # The phone number has a WhatsApp account
    print(f"{phone_number} has a WhatsApp account.")
elif response.status_code == 404:
    # The phone number does not have a WhatsApp account
    print(f"{phone_number} does not have a WhatsApp account.")
else:
    # There was an error with the request
    print(f"An error occurred: {response.status_code}")
