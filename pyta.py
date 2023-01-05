import pyautogui

# Set the delay between actions (in seconds)
pyautogui.PAUSE = 1

# Set the messages to send
messages = ['Hello!', 'How are you doing?', 'I hope you are having a good day.']

# Open WhatsApp
pyautogui.hotkey('win', '1  ')  # Open the Run dialog
pyautogui.typewrite('WhatsAp'
                    'Hello!'
                    'How are you doing?'
                    'I hope you are having a good day.'
                    'p')  # Type "whatsapp"
pyautogui.press('enter')  # Press Enter

# Wait for WhatsApp to load
pyautogui.sleep(5)

# Select the first contact
pyautogui.press('tab')  # Move focus to the contact list
pyautogui.press('down')  # Select the first contact
pyautogui.press('enter')  # Open the chat with the selected contact

# Send the messages
for message in messages:
    pyautogui.typewrite(message)  # Type the message
    pyautogui.press('enter')  # Send the message

# Close WhatsApp
pyautogui.hotkey('alt', 'f4')  # Close the active window
