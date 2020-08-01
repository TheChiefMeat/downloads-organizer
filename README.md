This is a script to organize the files in your downloads folder into subfolders like IMAGES, AUDIO, VIDEO, EBOOKS, etc. 

To use this script:
1. Make sure you are running Python version later than 3.5.
2. Clone this repository. 
3. ```cd downloads-organizer```
4. ```cd downloadsorganizer```
5. ```python main_script.py```

Notes: 

* This has been tested:
    * Kubuntu 20.04.1
    * Windows 10
* Use the path.config file to specify where your download folder is.
* Use the dictionary.txt file to add/remove files to the filter.
* The filter will continue to run in the background, use a cronjob or similar to run at startup for constant file sorting.
* Known Issues:
    * Download paths with spaces in them don't work for now.
    * Download Organizer will continue to monitor sub-folders, so clean up any sub-folders so you don't run into the below issue.
    * Linux users will run into a inotify limit if the downloads folder has more files than inotify allows. To check your inotify limit run:

```cat /proc/sys/fs/inotify/max_user_watches```
    
 * To modify your max_user_watches run:
    
```echo 16384 | sudo tee /proc/sys/fs/inotify/max_user_watches```

* The above issue only happens once you go over max_user_watches(usually 8192 files).

Feedback or suggestions welcome!
