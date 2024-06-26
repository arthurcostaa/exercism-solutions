def reverse(text):
    text = list(text)
    return text.pop() + reverse(text) if len(text) > 0 else ''
