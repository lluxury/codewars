
MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F','--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L','--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R','...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X','-.--': 'Y', '--..': 'Z','-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4','.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9','.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!','-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':','-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_','.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS', '_': ' '
}


def decodeMorse(morseCode):
    """
    >>> decodeMorse('.... . -.--   .--- ..- -.. .')
    'HEY JUDE'
    """ 
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))


# doc只能放在函数下第一行
# python -m doctest -v test.py
        