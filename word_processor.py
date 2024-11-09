class WordProcessor:
    """A class to process text strings with various utility methods."""

    def count_alphabets(self, text):
        """Counts alphabetic characters in a given string."""
        return sum(1 for char in text if char.isalpha())

    def count_numbers(self, text):
        """Counts numeric characters in a given string."""
        return sum(1 for char in text if char.isdigit())

    def is_palindrome(self, text):
        """Checks if the given string is a palindrome."""
        return text == text[::-1]

    def replace_string(self, text, old, new):
        """Replaces all occurrences of 'old' substring with 'new' in the text."""
        return text.replace(old, new)