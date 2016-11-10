## Description
This is a program that can be used to download videos in a YouTube playlist given the URL of the playlist. A playlist URL is of the form `https://www.youtube.com/playlist?list=playlist_id_here`. The project consists mainly of two files `setup.sh` and `main.py`<br>
`setup.sh` is an installation script that installs packages and modules that are required by `main.py`<br>
`main.py` is the python program which accepts command line options and arguments and performs the task of downloading the videos present in the YouTube playlist.<br>
The user needs to run `setup.sh` only once and run `main.py` each time a playlist has to be downloaded.<br>
The program has the ability to resume downloads if interrupted. To resume an interrupted playlist download, the user has to run `main.py` with the same playlist page url and ensure that the download is now occurring in the same directory the interrupted program was downloading videos to, and ensure same video format.
To be able to use this program the user needs to have a Google API key with YouTube Data API v3 enabled. 

## Options
`main.py` accepts command line arguments and options. Information about these can be found with the help of<br> 
`python3 main.py -h`, however, they are listed below.
 ```
usage: main.py [-h] [-o DIR] [-u FILE] [-f FORMAT] URL

positional arguments:
  URL                           URL is the url of the playlist page

optional arguments:
  -h, --help                    show this help message and exit

  -o DIR, --output DIR          DIR is the path to the directory where the videos must
                                be downloaded. Directory will be created if not
                                present.

  -u FILE, --urls-file FILE     FILE is the path to the file in which the url of each
		                        video must be written. Last component of the path must
		                        be the name of the file. If file is already present it
		                        will be overwritten. Directory and file will be
		                        created if the directory is not present.

  -f FORMAT, --format FORMAT    FORMAT is the format in which each of the videos in
                                the playlist must be downloaded and can be either
                                'best' or 'worst'. If not specified it is set to
                                'best'.


 ```
 - If the `-o` / `--output` option is not used then videos will be downloaded in the current working directory.
 - If the `-u` / `--urls-file` option is not used then url of each video will be written to a file `playlist_vid_urls.txt` in the current working directory.If such a file already exists it will be overwritten.
 - If the `-f` / `--format` option is not used then the videos will be downloaded in `best` format.

## Usage Instructions
- Download the files 'main.py' and 'setup.sh' into a directory and make this directory your current working directory.
- Allow execution of the script `setup.sh` by changing its permissions with the help of the following<br>
    `chmod a+x setup.sh` 
- Run `setup.sh` with the help of the following<br>
    `./setup.sh`
- Execute the python program with appropriate options<br>
	`python3 main.py -o path_to_dir -u path_to_file -f format_of_videos url_of_playlist_page`
- Enter a Google API key with YouTube Data API v3 enabled