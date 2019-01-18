def abbreviate(words):
    words = words.split(' ')
    result = ''

    for word in words:
        for i in range(len(word)):
            if word[i].isalpha():
                result += word[i]
                if '-' in word:
                    result += word[word.find('-') + 1]
                break

    return result.upper()
