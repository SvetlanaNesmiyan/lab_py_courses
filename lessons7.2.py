def correct_sentence(text):
    text = text.strip()

    text = text[0].upper() + text[1:]

    if not text.endswith('.'):
        text += '.'

    return text

result = correct_sentence("greetings, friends")
print(result)