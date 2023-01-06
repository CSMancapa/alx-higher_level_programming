#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for ch in text:
        if ch in ['.', '?', ':']:
            print(ch, end='\n\n')
        else:
            print(ch, end='')
