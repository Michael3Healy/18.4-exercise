"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("words.txt")
    235886 words read
    """
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.words_list = []

        self.read_file()

        print(f'{len(self.words_list)} words read')
        
    def read_file(self):
        file = open(self.file_path, 'r')
        for line in file:
            self.words_list.append(line.strip())

        file.close()

    def random(self):
        rand_index = randint(0, len(self.words_list) - 1)

        return self.words_list[rand_index]

class SpecialWordFinder(WordFinder):
    
    def read_file(self):
        file = open(self.file_path, 'r')

        for line in file:
            if line.strip() and not line.startswith('#'):
                self.words_list.append(line.strip())

        file.close()





