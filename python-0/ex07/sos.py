
import sys


def main():
    morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'}
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")
        encoded_message = ''
        for char in sys.argv[1].upper():
            if char in morse_dict:
                encoded_message += morse_dict[char] + ' '
            elif char not in morse_dict:
                raise AssertionError("AssertionError: the arguments are bad")
        print(encoded_message.strip())
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()