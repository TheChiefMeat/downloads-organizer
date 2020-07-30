import os

USERNAME = os.getlogin()

config_Path = open("path.config","r")

DOWNLOADS_DIRECTORY = config_Path.read()

EXTENSIONS_DICT = {
    'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'video': ['.mp4', '.webm', '.flv', '.avi', '.mov', '.qt', '.m4v'],
    'audio': ['.mp3', '.wav', '.m4a'],
    'torrent': ['.torrent'],
    'archive': ['.zip', '.rar', '.tar', ],
    'web': ['.html', '.webarchive'],
    'docs': ['.xlsx', '.pdf', '.csv', '.json', '.ppt', '.docx', '.txt'],
    'ebook': ['.epub', '.mobi'],
    'software': ['.dmg', '.pkg', '.app'],
}