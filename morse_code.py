MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


def decodeBits(bits):
    bits = bits.strip("0")

    if not bits:
        return ""

    min_one_sequence = float("inf")
    current_one_count = 0

    for bit in bits:
        if bit == "1":
            current_one_count += 1
        elif current_one_count > 0:
            min_one_sequence = min(min_one_sequence, current_one_count)
            current_one_count = 0

    if current_one_count > 0:
        min_one_sequence = min(min_one_sequence, current_one_count)

    dot = "1" * min_one_sequence
    dash = "1" * (min_one_sequence * 3)
    space = "0" * (min_one_sequence * 3)
    word_space = "0" * (min_one_sequence * 7)

    decoded_message = ""
    temp_word = ""

    i = 0
    while i < len(bits):
        if bits[i : i + len(dash)] == dash:
            temp_word += "-"
            i += len(dash)
        # Identify dots, dashes, or spaces
        elif bits[i : i + len(dot)] == dot:
            temp_word += "."
            i += len(dot)
        elif bits[i : i + len(word_space)] == word_space:
            if temp_word:
                decoded_message += temp_word + " "
                temp_word = ""
            decoded_message = decoded_message.strip() + "   "
            i += len(word_space)
        elif bits[i : i + len(space)] == space:
            if temp_word:
                decoded_message += temp_word + " "
                temp_word = ""
            i += len(space)

        else:
            i += 1

    if temp_word:
        decoded_message += temp_word

    return decoded_message.strip()


def decodeMorse(message):

    message += " "

    decipher = ""
    citext = ""
    for letter in message:

        if letter != " ":
            i = 0

            citext += letter

        else:
            i += 1

            if i == 3:

                decipher += " "
            else:
                if citext == "":
                    continue
                else:
                    decipher += list(MORSE_CODE_DICT.keys())[
                        list(MORSE_CODE_DICT.values()).index(citext)
                    ]
                    citext = ""

    return decipher


def main():
    bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"
    print(decodeBits(bits))
    message = decodeBits(bits)

    result = decodeMorse(message)
    print(result)


# Executes the main function
if __name__ == "__main__":
    main()