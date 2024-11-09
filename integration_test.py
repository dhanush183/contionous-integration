# test_wordprocessor.py

import pytest
from word_processor import WordProcessor

def test_integration_replace_and_count_and_palindrome():
    processor = WordProcessor()

    # Replace "world" with "Python"
    modified_text = processor.replace_string("hello world", "world", "Python")
    assert modified_text == "hello Python"

    #  Count the alphabets in modified_text
    alpha_count = processor.count_alphabets(modified_text)
    assert alpha_count == 11  # 'hello' (5) + 'Python' (6) = 11

    #  Check if modified_text is a palindrome
    is_palindrome = processor.is_palindrome(modified_text)
    assert not is_palindrome  # "hello Python" is not a palindrome
