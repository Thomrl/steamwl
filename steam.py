#! python3.5
import os, sys, pyperclip

sys.argv

if len(sys.argv) > 1:
    uInput = " ".join(sys.argv[1:]) 
else:
    uInput = pyperclip.paste()

File = open("E:\\SteamWatchlist.txt", "a")
File.write("\n"+uInput)
File.close()
