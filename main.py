#AIzaSyCxVRqztJej5NYJZCnVFDCA5UuEoC7HfiY
#https://www.youtube.com/playlist?list=PLonJJ3BVjZW6_q8gh7XoLUIhRIyBcYJLP
import requests
import os
import youtube_dl
import argparse
import sys

# Set up command line options for this program
parser=argparse.ArgumentParser()
parser.add_argument("url",help="URL is the url of the playlist page",metavar="URL")
parser.add_argument("-o","--output",help="DIR is the path to the directory where the videos must be downloaded. Directory will be created if not present.",metavar="DIR")
parser.add_argument("-u","--urls-file",help="FILE is the path to the file in which the url of each video must be written. Last component of the path must be the name of the file. If file is already present it will be overwritten. Directory and file will be created if the directory is not present.",metavar="FILE")
parser.add_argument("-f","--format",help="FORMAT is the format in which each of the videos in the playlist must be downloaded and can be either 'best' or 'worst'. If not specified it is set to 'best'.",choices=["best","worst"],default="best",metavar="FORMAT")
arguments=parser.parse_args()

playlist_id=(arguments.url.split("="))[1]# Get the playlist ID
maxresults_per_page=50
api_key=input("Please enter a Google API key with YouTube Data API v3 enabled\n")
playlist_vid_urls_file=""
if arguments.urls_file:
	# Check whether the directory in which a file is supposed to store the URL's of videos in the playlist exists.(check whether the directory exists)
	# If directory does not exist create the directory
	playlist_vid_urls_file=os.path.abspath(os.path.expanduser(arguments.urls_file))
	temp=os.path.split(playlist_vid_urls_file)
	if not os.path.isdir(temp[0]):
		os.makedirs(temp[0])
else:
	playlist_vid_urls_file=os.path.abspath("playlist_vid_urls.txt")
n=0
with open(playlist_vid_urls_file,"w") as f: 
	# Get URL
	# Use YouTube Data API to get info about the playlist. Details of a maximum of 'maxresults_per_page' videos in the playlist are 
	# present in the first response. Use 'nextPageToken' to get details of other videos
	req_param={"playlistId":playlist_id,"maxResults":maxresults_per_page,"part":"snippet","key":api_key}
	while True:
		#make the request
		try:
			response=requests.get("https://www.googleapis.com/youtube/v3/playlistItems",params=req_param)
		except requests.exceptions.ConnectionError:
			print("Connection Error")
			sys.exit()
		except requests.exceptions.Timeout:
			print("Timeout")
			sys.exit()
		except requests.exceptions.TooManyRedirects:
			print("Too many redirects")
			sys.exit()
		except requests.exceptions.HTTPError:
			print("HTTP error")
			sys.exit()
		json_response=response.json()	
		#write data
		for i in json_response["items"]:
			f.write("https://www.youtube.com/watch?v=")
			f.write(i["snippet"]["resourceId"]["videoId"])
			f.write("\n")
			n=n+1
		#check if next page exists
		if "nextPageToken" in json_response:
			req_param["pageToken"]=json_response["nextPageToken"]
		else:
			break

	print("\nThere are ",n,"non private videos in the playlist\nURL of each video in the playlist has been successfully written to ",playlist_vid_urls_file)

# Download Videos
vid_download_dir=""
if arguments.output:
	vid_download_dir=os.path.abspath(os.path.expanduser(arguments.output))
else:
	vid_download_dir=os.path.abspath("")
outtmpl_arg=vid_download_dir+"/%(title)s.%(ext)s"
n=1
with open(playlist_vid_urls_file,"r") as f:
	ydl_options={
		"outtmpl":outtmpl_arg,
		"format":arguments.format
	}
	with youtube_dl.YoutubeDL(ydl_options) as ydl:
		for URL in f:
			print("Download of video",n,"started")
			ydl.download([URL])
			print(n,"video(s) downloaded")
			n=n+1
	print("All the videos have been successfully downloaded")