import unidecode

morse_dict = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '?': '..--..',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    ' ': '/',
}


def morse_to_text():
    """Decodes a string input of morse code and returns the decoded text as a string"""
    morse_input = input("Type your morse code in here to decode it\n"
                        "(letters devided by spaces, words divided by '/' between spaces):\n").split(" ")

    print(morse_input)

    text_output = ""

    for code in morse_input:
        for dict_letter in morse_dict:
            if morse_dict[dict_letter] == code:
                text_output += dict_letter

    if not text_output.split(" ") or text_output == "":
        print("Did you even provide valuable morse code? Try again!")
        return

    return print(f"The decoded text is:\n'{text_output}'")


def text_to_morse():
    """Encodes a string input to morse code and filters out accents and also converts mutated vowels"""
    text_input = input("Type your text in here to encode it:\n").upper()
    print(text_input)

    message = ""

    for letter in text_input:
        if letter == "Ä":
            letter = "AE"
        elif letter == "Ö":
            letter = "OE"
        elif letter == "Ü":
            letter = "UE"
        elif letter == "ß":
            letter = "SS"
        elif letter == "@":
            letter = "AT"
        letter = unidecode.unidecode(letter)
        message += letter

    morse_output_list = [morse_dict[letter] for letter in message]

    morse_output = ""

    for code in morse_output_list:
        morse_output += f"{code} "

    if morse_output == "":
        print("Did you even provide any text? Try again!")
        return

    return print(f"Your encoded morse code is:\n'{morse_output}'")


go_on = True

while go_on:
    answered = False

    while not answered:
        encode_or_decode = input("Do you want to encode text in to morse code or do you want to decode morse code? "
                                 "Type 'encode' or 'decode':\n").lower()
        if encode_or_decode == "encode":
            text_to_morse()
            answered = True
        elif encode_or_decode == "decode":
            morse_to_text()
            answered = True
        else:
            print("You did not type in 'encode' or 'decode'.\n")

    answered = False

    while not answered:
        start_again = input("Do you want to encode or decode another text? Type Y/N\n").lower()
        if start_again == "n":
            go_on = False
            answered = True
        elif start_again == "y":
            go_on = True
            answered = True
        else:
            print("You did not type Y or N.\n")
