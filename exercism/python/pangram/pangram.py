def is_pangram(sentence):
    sentence = sentence.lower()
    temp = set()
    for char in sentence:
        if char.isalpha() and not(char in temp):
            temp.add(char)
    
    if len(temp) == 26:
        return True
    
    return False

