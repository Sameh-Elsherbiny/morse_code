MORSE_CODE = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
    "--..--": ", ",
    ".-.-.-": ".",
    "..--..": "?",
    "-..-.": "/",
    "-....-": "-",
    "-.--.": "(",
    "-.--.-": ")",
}

import re


def decodeBits(bits):
    # Remove leading and trailing 0s
    bits = bits.strip("0")
    # Return empty string if bits is empty
    if not bits:
        return ""
    # Find the minimum time unit by finding the minimum length of 1s and 0s
    min_time_unit = min(len(m) for m in re.findall(r"1+|0+", bits))

    return (
        bits.replace("0000000" * min_time_unit, "   ")
        .replace("000" * min_time_unit, " ")
        .replace("111" * min_time_unit, "-")
        .replace("1" * min_time_unit, ".")
        .replace("0" * min_time_unit, "")
    )


def decodeMorse(morseCode):

    # Function to decode morse code letter and join it to form a word
    def decodeMorseLetter(word):
        return "".join(MORSE_CODE[letter] for letter in word.split())

    # Split the morse code by 3 spaces to get words and decode each word to form a sentence
    return " ".join(decodeMorseLetter(word) for word in morseCode.split("   "))


def main():
    bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"
    message = decodeBits(bits)
    print("decoded bits : " + message)

    result = decodeMorse(message)
    print("decoded morse code : " + result)


# Executes the main function
if __name__ == "__main__":
    main()
