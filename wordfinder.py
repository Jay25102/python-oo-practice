"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self, file_dir="words.txt"):
        """
        initializes variables and calls a function to get a word list from a file

        Attributes
        ------------------
        file_dir: str
            directory of file with words. set to words.txt by default
        word_list: []
            empty list to be filled with words from text file
        """
        self.file_dir = file_dir
        self.word_list = []
        # calls function to populate word_list
        self.add_words_to_list()

    def __repr__(self):
        """returns general info and word list"""
        return f"gets a list of words from a file and returns a random word. word_list: {self.word_list}"

    def add_words_to_list(self):
        """adds each word to the word_list while removing the newline escape char"""
        file = open(self.file_dir, "r")
        for word in file:
            self.word_list.append(word.strip())
        file.close()

    def random(self):
        """returns a random word from list"""
        # return self.word_list[random.randint(0, len(self.word_list))]
        # choice() is much easier
        return random.choice(self.word_list)
    


class SpecialWordFinder(WordFinder):
    """
    subclass of WordFinder that utilizes text files with blank lines and octothorpes

    Attributes
        ------------------
        file_dir: str
            directory of file with words. set to words.txt by default
        word_list: []
            empty list to be filled with words from text file
    """

    # is this the proper way to inherit a default value?
    def __init__(self, file_dir="specialwords.txt"):
        super().__init__(file_dir)

    def __repr__(self):
        """returns general info about SpecialWordFinder and word list"""
        return f"gets a list from words of files containing spaces and octothorpes. word_list: {self.word_list}"
    
    def add_words_to_list(self):
        """reads files with spaces and octothorpes and adds them to word_list"""
        file = open(self.file_dir, "r")
        for word in file:
            if not word.isspace():
                self.word_list.append(word.strip().lstrip("#").lstrip(" "))
        file.close()

    def random(self):
        return super().random()