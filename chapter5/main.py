from zip_processor import ZipProcessor
import sys
import os
from PIL import Image


class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string
    def process_files(self):
        '''perform a search and replace on all files in the        temporary directory'''
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
                contents = contents.replace(self.search_string, self.replace_string)
        with filename.open("w") as file:
            file.write(contents)

class ScaleZip(ZipProcessor):
    def process_files(self):
        '''Scale each image of the directory to 640x480'''
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((640,480))
            scaled.save(str(filename))


if __name__ == "__main__":
    #ZipReplace(*sys.argv[1:4]).process_zip()
    ScaleZip(*sys.argv[1:2]).process_zip()
