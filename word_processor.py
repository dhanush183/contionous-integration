class WordProcessor:
    """A class to process text strings with various methods"""
    def count_alphabets(self, text):
        return sum(1 for char in text if char.isalpha())