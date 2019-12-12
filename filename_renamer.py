# File Name Renamer
# James Lovie 2019
# Quick search & rename of all files with a matching extension in the current directory.

import os

# Class names should follow the UpperCaseCamelCase convention.
class FilenameRenamer:

    # Constructor: Instance variable names should be all lower case.
    def __init__(self, current_word, new_word):
        self.current_word = current_word
        self.new_word = new_word

    # Method names should be all lower case, words in an method name should be separated by an underscore.
    def rename_files_in_current_folder(self):
        dirpath = os.getcwd()
        folder = dirpath
        for filename in os.listdir(folder):
            infilename = os.path.join(folder,filename)
            if not os.path.isfile(infilename): continue
            oldbase = os.path.splitext(filename)
            newname = infilename.replace(self.current_word, self.new_word)
            output = os.rename(infilename, newname)

def main():
    # Instantiating the class:
    filenamerenamer = FilenameRenamer('October', 'November')

    # Call the function rename.
    rename_files_in_current_folder = filenamerenamer.rename_files_in_current_folder()
    print(f'Have completed the update of word {filenamerenamer.current_word} with {filenamerenamer.new_word} for all files in current directory.')

if __name__ == '__main__':
    main()
