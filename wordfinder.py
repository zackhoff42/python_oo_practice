"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """Class that accepts a .txt file with words spaced line by line and randomly selects one from the file to display."""
    
    def __init__(self, file_name):
        self.file = open(file_name, "r")
        self.words = self.read_file()
        self.length = len(self.words)
        print(f"{self.length} words read.")

    def read_file(self):
        """Converts the word file into a list"""
        return [line.strip() for line in self.file]

    def random(self):
        """Selects a random index in the words list and returns its value"""
        return self.words[randint(0, self.length - 1)]
    
class SpecialWordFinder(WordFinder):
    """Converts the word file to a list with conditional (values cannot be empty nor can they be a comment)"""
    def read_file(self):
        return [line.strip() for line in self.file if line.strip() and not line.startswith('#')]