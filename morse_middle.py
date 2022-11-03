MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', '!':'-.-.--',
                    '&':'.-...', '$': '...-..-', ':': '---...'}

MORSE_CODE = {value:key for key,value in MORSE_CODE_DICT.items()}


def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    """
    >>> decode_bits('111111111000000000000000000000111111111')
    '-   -'
    >>> decode_bits('111111111111')
    '.'
    >>> decode_bits('1111110011')
    '-.'
    """
    return bits.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')

def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    """
    >>> decode_morse('...   ---   ...')
    'S O S'
    >>> decode_morse('- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-')
    'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'
    """
    pass
