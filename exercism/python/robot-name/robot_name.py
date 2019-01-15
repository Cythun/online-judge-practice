import random

class Robot(object):
    def __init__(self):
        chars = ('A', 'B', 'C', 'D', 'E', 'F', 'F', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

        nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

        output = ''
        for i in range(2):
            output += random.SystemRandom().choice(chars)

        for i in range(3):
            output += random.SystemRandom().choice(nums)

        self.name = output

    def reset(self):
        chars = ('A', 'B', 'C', 'D', 'E', 'F', 'F', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

        nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

        output = ''
        for i in range(2):
            output += random.SystemRandom().choice(chars)

        for i in range(3):
            output += random.SystemRandom().choice(nums)

        self.name = output

