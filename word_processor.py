class WordProcessor:
    def count_alphabets(self, text):
        return sum(1 for char in text if char.isalpha())