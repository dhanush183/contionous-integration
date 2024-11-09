from word_processor import WordProcessor

# Instantiate the WordProcessor class
word_processor = WordProcessor()

def test_count_alphabets():
    text = "Hello World 123"  # Input text for count_alphabets testing
    exp_result = 10           # Expected alphabetic character count
    result = word_processor.count_alphabets(text)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"

def test_count_numbers():
    text = "Hello World 123"  # Input text for count_numbers testing
    exp_result = 3            # Expected numeric character count
    result = word_processor.count_numbers(text)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"

def test_is_palindrome():
    text = "Hello World 123"  # Input text for is_palindrome testing
    exp_result = False        # Expected result for palindrome check
    result = word_processor.is_palindrome(text)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"

def test_replace_string():
    text = "Hello World 123"  # Original text for replace_string testing
    old_str = 'H'             # Substring to replace
    new_str = 'W'             # New substring
    exp_result = "Wello World 123"  # Expected result after replacement
    result = word_processor.replace_string(text, old_str, new_str)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"