import os


class DirectoryIndex:

    def __init__(self, dirpath: str, encoding: str = 'utf-8'):
        self.path = dirpath
        self.encoding = encoding
        self.index = dict()

    def index_document(self, directory: str) -> dict:
        dict_of_terms = {}
        if len(os.listdir(directory)) != 0:
            for file in os.listdir(directory):
                if os.stat(directory).st_size != 0:
                    for line in file:
                        for term in line.lower():
                            if term not in dict_of_terms:
                                dict_of_terms[term] = {}  # chose a set, because the fact (!) of appearance matters, not its frequency
                            else:
                                dict_of_terms[term] += file   # appending the name of the file if term appears there

                else:
                    raise Exception("The given file is empty")

        else:
            raise Exception("The given directory is empty.")

        return dict_of_terms

    def find_documents(self, word: str) -> set:    # function for finding the documents where the given term appears
        if word in self.index_document(self.path).keys():
            return self.index_document(self.path)[word]  # returning a set of docs

        else:
            return set()  # else returning an empty set

    def update(self, filepath: str, encoding: str = 'utf-8'):
        self.index.update(self.index_document(filepath))

    @property
    def inverted_index(self):
        return self.index   # returns a dictionary with all the terms and docs where they appear
