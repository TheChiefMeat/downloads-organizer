import os
import ast

USERNAME = os.getlogin()

dir_path = os.path.dirname(os.path.realpath(__file__))

config_Path = open(dir_path + "/path.config","r")
dictionary_Path = open(dir_path + "/dictionary.txt","r")
DOWNLOADS_DIRECTORY = config_Path.read()

dictionary_contents = dictionary_Path.read()
EXTENSIONS_DICT = ast.literal_eval(dictionary_contents)