import pyphen

dic = pyphen.Pyphen(lang='pl')


def is_anagram(first, second):
    return sorted(get_syllabes(first)) == sorted(get_syllabes(second))


def get_syllabes(word):
    word = dic.inserted(word.lower()).split('-')
    word = map(str.strip, word)
    return word


print(is_anagram("good food", "good food"))
print(is_anagram("KOMINIARZE", "KORZENIAMI"))
