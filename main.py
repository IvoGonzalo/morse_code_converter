morse_code_alphabet = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': '/'}

message = input("-------Morse Code Converter-------\nType your message: ")


def morse(text=message):
    text = list(text.lower())
    code_morse = [morse_code_alphabet[letter] + " " for letter in text if letter in morse_code_alphabet.keys()]
    message_in_morse = "".join(code_morse)
    print(code_morse)
    print(f"Your message: {message}\nIn morse code is: \n{message_in_morse}")
    return code_morse


def decrypt(code):
    code = [i.strip(" ") for i in code]
    key_list = list(morse_code_alphabet.keys())
    val_list = list(morse_code_alphabet.values())
    text_message = ""
    for letters in code:
        text_message += key_list[val_list.index(letters)]
    print(f"Your morse code decrypted:\n{text_message}")


code_morse_list = morse()
print(code_morse_list)

question = input("If you want to decrypt your message type 'y': ").lower()

if question == "y":
    decrypt(code_morse_list)
else:
    print("Program ends")