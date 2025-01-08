import string

text = input("Введіть рядок: ")

cleaned_words = text.translate(str.maketrans('', '', string.punctuation)).split()

capitalized_words = [word.capitalize() for word in cleaned_words]

hashtag = '#' + ''.join(capitalized_words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)