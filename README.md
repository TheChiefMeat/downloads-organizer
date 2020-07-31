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
* Download paths with spaces in them don't work for now.
* Use the dictionary.txt file to add/remove files to the filter.
* The filter will continue to run in the background, use a cronjob or similar to run at startup for constant file sorting.

Feedback or suggestions welcome!
