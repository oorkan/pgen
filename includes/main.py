import random
import string

class Password:
    def __init__(self):
        pass

    def generate(self, options = {
            'lowercase' : True,
            'uppercase' : True,
            'numbers' : True,
            'special_chars' : True,
            'length' : 12
        }):
        # string.ascii_letters
        # string.digits
        # string.punctuation
        letters = string.ascii_letters
        digits = string.digits
        punctuation = string.punctuation

        if(not options['lowercase'] and options['uppercase']):
            letters = string.ascii_uppercase
        elif(options['lowercase'] and not options['uppercase']):
            letters = string.ascii_lowercase
        elif(not options['lowercase'] and not options['uppercase']):
            letters = ''

        if(not options['numbers']):
            digits = ''

        if(not options['special_chars']):
            punctuation = ''

        chars = letters + digits + punctuation
        password = ''.join(random.choice(chars) for i in range(options['length']))
        
        return password