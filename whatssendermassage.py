# Import the modules
import webbrowser
import pyautogui
from time import sleep

# Define the function to send a message
def send(text, phone):
    # Open the WhatsApp Web URL with the message and phone number
    webbrowser.get("google-chrome").open("whatsapp://send?text=" + text.replace('\n', '%0A') + "&phone=" + phone.replace('+', ''))
    # Wait for 10 seconds for the page to load
    sleep(10)
    # Click on the send button
    pyautogui.click(x=1787, y=978)
    # Wait for 0.2 seconds
    sleep(0.2)
    # Press the enter key
    pyautogui.hotkey('enter')
    # Wait for 1 second
    sleep(1)
    # Close the browser window
    pyautogui.hotkey('alt', "f4")

# Call the function with the message and phone number
send("Hello from Python!", "+962791837885")