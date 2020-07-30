import os
import ast

USERNAME = os.getlogin()

config_Path = open("path.config","r")
dictionary_Path = open("dictionary.txt","r")

DOWNLOADS_DIRECTORY = config_Path.read()

dictionary_contents = dictionary_Path.read()
EXTENSIONS_DICT = ast.literal_eval(dictionary_contents)