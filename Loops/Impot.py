import pyperclip

messages = {
    "greet": "Hello, how are you?",
    "bye": "Goodbye!",
    "thanks": "Thank you!"
}

key = input("Enter key: ")

if key in messages:
    pyperclip.copy(messages[key])
    print("Copied!")
