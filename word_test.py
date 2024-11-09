from word_processor import WordProcessor
word_processor = WordProcessor()

def test_count_alphabets():
    text = "Hello World 123" #input text for count_alphabets
    exp_result = 10
    result = word_processor.count_alphabets(text)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"