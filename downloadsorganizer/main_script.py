from attributes import DOWNLOADS_DIRECTORY
from funcs import print_os_info, change_working_directory, list_all_files, sort_files_by_type, \
    move_files_to_folders
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import time

dl_dir = DOWNLOADS_DIRECTORY

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print_os_info()
        print(f'DOWNLOADS DIRECTORY: {dl_dir}')
        change_working_directory(dl_dir)
        download_files = list_all_files(dl_dir)
        files_sorted = sort_files_by_type(download_files)
        move_files_to_folders(files_sorted)
        print('DONE!')

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, dl_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
