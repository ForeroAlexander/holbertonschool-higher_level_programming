#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    s = "".join([word if word not in ".?:"
                 else word + "\n\n" for word in text])
    print("\n".join([l.strip() for l in s.split("\n")]), end="")
