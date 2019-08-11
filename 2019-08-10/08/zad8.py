def is_palindrome(sentence):
    sentence = sentence.strip(' .?!').lower()

    reversed_sentence = sentence[::-1]

    return sentence == reversed_sentence

print(is_palindrome('rac ecar'))
