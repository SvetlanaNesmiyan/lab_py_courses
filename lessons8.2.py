import string
def is_palindrome(text):
    text = text.lower()
    filtered_text = ''.join(ch for ch in text if ch.isalnum())
    return filtered_text == filtered_text[::-1]


result = is_palindrome('A man, a plan, a canal: Panama')
print(result)