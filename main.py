from spotifyHelper import getPlaylistTracks
from colorama import Fore
from ytScraper import search_first_video
from ytDownloader import converter
import time

#CHANGE THESE
YOUTUBEKEY = "" #GOOGLE CLOUD CONSOLE
SPOTIFYCLIENT=""
SPOTIFYSECRET=""

ascii_art="""""\n\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⢤⢤⣠⢤⣤⣤⣤⣄⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣶⣿⡿⣿⣟⣿⣻⣯⣟⣿⣞⣿⣾⣽⣾⣽⣯⣟⣿⣻⡿⣿⣷⣶⣴⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣯⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⣪⣴⠚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣤⣑⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⣮⣿⣿⡿⣜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢿⡿⣿⢿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⣟⣿⣿⣷⣥⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡰⢁⣾⣿⣿⣿⣹⢷⣿⣿⣿⡿⣿⢹⠉⣇⠹⠰⢆⠱⠈⠆⠱⠀⠇⠰⠁⠎⠰⢀⠇⢉⡸⢉⠹⢏⡿⢿⣿⣿⣿⣿⣷⣏⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠄⣰⣿⡿⣯⢿⣿⡿⢛⠏⠓⠌⠒⠄⠃⠉⠀⠈⠁⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠘⠠⠉⡙⠛⠿⣿⣿⣿⣿⣻⣽⡿⣿⣦⡑⢄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠠⢂⣼⣿⢿⡽⣽⡿⢓⡘⠄⠂⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠘⡹⢿⣿⣷⣯⣟⣿⣿⣿⣄⠠⠀⠀⠀⠀
⠀⠀⠀⢀⢇⣾⣿⢯⣿⡽⢏⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⡝⢿⣿⣿⣞⣿⣿⣿⣆⠀⠀⠀⠀
⠀⠀⠀⡎⣾⣿⡽⣾⢟⡱⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠣⡹⢿⣿⣾⣻⣿⣿⡆⢠⠀⠀
⠀⠀⠸⢸⣩⡻⣽⠟⣌⢦⣿⠒⡱⣢⣀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠄⠀⠀⠀⠀⢠⣾⡿⣏⣱⣻⣯⠻⣷⠻⡷⣿⠀⠀⠀
⠀⣀⣷⣾⣤⣭⣿⡸⣼⣿⣤⢼⠧⣱⣿⣦⠀⠙⠠⣀⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⠀⠀⢨⣿⡿⣭⠄⣩⣿⡧⢘⡿⠟⣿⣿⠑⠀
⣰⣿⣿⣿⠿⣽⣯⢷⣿⡿⠖⡿⣘⠶⡟⠃⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠈⠅⠡⠀⢕⠀⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠀⢘⣿⣻⢷⣎⡳⢿⣿⢏⣷⡀⠰⣭⢃⠧
⣾⣿⣿⣏⡿⣿⣾⢼⣿⡿⡥⢳⠥⣾⣅⣤⡔⠂⠈⠐⠁⠀⠀⠀⢀⢀⢀⠀⠠⠐⢆⡀⢠⠈⠠⡀⠀⠀⢄⠈⠀⠀⠀⠁⠈⠢⠈⠀⢨⡄⢉⣿⣯⢿⡬⣙⣿⣿⢮⣾⣿⣟⢂⢮⣱
⣿⣯⣿⣧⢿⣿⣿⢾⣿⣿⡳⣭⢲⣹⣿⠋⢀⠀⠀⠔⠀⠀⠄⠀⠀⠀⠈⠐⠊⠅⡀⢄⠐⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⣶⣺⣿⣯⣟⡞⢷⣾⣿⣎⣿⡟⡆⣞⡲⡍
⢿⣿⣞⣿⣿⣿⣾⣻⣿⣟⡷⣩⢖⣻⣷⠤⠃⡀⠀⣰⠄⠐⠄⡁⠀⠌⠂⠈⡠⠄⡑⢢⠀⠂⠀⠠⠄⠒⢄⣢⠀⠈⡀⠐⢄⠀⠀⠀⠀⢺⣿⣿⢷⣯⢟⡺⣼⣿⣞⡿⢉⠴⣣⠿⣵
⠸⣿⣾⣹⡾⣿⣿⣹⣿⣿⢷⡹⣎⣹⣿⡆⠁⠆⠎⠁⠆⡀⠰⡈⠱⠸⠆⢆⠀⢈⠁⠀⠁⣆⠹⡁⠀⠆⡆⠀⠁⡰⠆⠁⠀⠀⠀⠀⠀⢸⣿⣿⣿⣏⡏⣷⢿⣿⡾⣿⣀⡇⢷⢹⣹
⠀⣿⣿⣷⣻⢿⣿⣿⣿⣿⢯⣳⡝⣾⡿⣑⡈⢉⣥⣷⣿⣆⣷⠹⡄⡀⢎⡜⣄⠢⡌⡞⢸⠐⢧⢈⢀⡬⠢⡈⠄⡀⠀⣶⣦⣤⠀⠀⠀⢀⣿⣿⣷⢯⣿⣼⣻⣿⣽⣿⣿⠶⠋⢼⣹
⠀⣹⣿⣷⣻⣦⣿⣿⣿⣿⣯⢷⣹⢾⣿⡤⠘⢹⣿⣿⣿⣿⡌⢧⠑⠱⠘⡳⣍⢣⣄⣧⣷⣴⢌⠂⢄⠰⣂⢐⠀⠁⢸⣿⣿⣿⡆⠀⠧⣺⣿⣿⣿⣻⣎⢿⣿⣟⡾⣿⣿⣿⣧⠰⠌
⠀⢼⣯⢟⡿⣿⣿⣿⣿⣿⣯⣟⡧⣿⣿⡕⢋⡙⠻⡿⠿⠋⢸⣲⢈⢇⣆⠽⣙⢹⡞⠻⠟⠋⢁⡈⠌⠈⡀⢃⠁⠈⠂⠘⡛⠛⠁⢀⠀⠘⣿⣿⣯⢷⣫⢿⣿⣯⢿⣿⣿⣿⡟⠃⡇
⠀⢸⣿⢮⣝⣿⣿⣿⣾⣿⣿⡾⣽⣻⣿⣆⠛⢩⡀⠼⠀⢖⡺⢉⠚⡄⡾⠐⣨⠎⡆⡌⠀⢂⠱⡈⠊⢂⠓⠌⢖⠌⠀⢠⠀⠀⠀⢑⢂⠸⣿⣿⣟⣯⣽⣿⣿⢾⣼⣿⢯⣿⠇⢀⠁
⠀⠌⣿⣻⣿⣿⣿⣯⣿⣿⣿⣽⣳⢿⣏⣿⠲⣃⣁⢦⡎⠐⠬⠛⠐⠀⠐⢀⢯⠃⢀⠱⡀⠨⠀⢁⠀⢆⠈⠑⠈⠀⠁⠀⠁⠀⠀⠀⠈⢹⣿⣿⣻⢮⣽⣿⣟⣦⣿⣿⣷⡿⠀⡈⠀
⠀⠂⠼⣟⣿⣿⣿⣿⣿⣻⣿⣿⣽⣻⣿⡟⢴⠂⣼⠀⢂⢌⠀⢀⠀⠀⢀⠈⣃⠈⡅⡆⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⢯⣟⣻⣿⠾⣼⣿⣷⣾⠇⠠⠁⠀
⠀⠀⢀⢹⣞⡿⣿⡿⣽⣿⣿⣿⡷⣿⣿⡾⣸⣋⡥⠐⡉⠀⠈⠀⠀⠀⡀⠀⡀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣻⢾⣿⣯⡟⣾⣳⣿⣞⢣⠂⠀⠀
⠀⠀⢀⢊⢻⣾⣱⣻⣼⣻⣿⣿⣿⣿⣿⡷⠅⣹⠀⡀⠁⠀⠐⡀⠀⠐⠀⡘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡷⣏⣿⣿⠻⠼⣗⢻⢟⣣⠃⠀⠀⠀
⠀⠀⠀⠂⢆⠹⢷⣿⣾⣽⣿⣿⣿⣿⣿⣟⡱⢩⡄⠰⠀⢮⠐⢄⡂⡄⢂⣶⣌⣧⡐⣨⡤⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣽⣿⠧⠿⠙⢾⠓⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠡⢈⢂⠣⡜⡽⣫⢿⡿⣿⣿⣿⣿⣳⣲⣅⣳⣯⣬⣓⣶⣽⣾⠟⣏⠾⠌⠝⠙⠑⠋⠉⠉⠉⠁⠈⠐⠀⢀⣤⣤⣤⣄⣄⡄⣀⣾⣿⠿⡉⠁⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠰⠀⠎⡰⢱⠸⣁⢿⡸⣏⣿⣹⣿⣿⡿⢿⠉⡉⣿⣿⣿⠿⢀⡸⢀⠉⠀⠁⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠹⣿⣿⠉⠇⠏⠉⠉⢿⣏⢱⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢁⠘⠄⢣⠑⡍⠶⣙⠞⣶⠻⢎⡑⡈⠆⡁⠒⣤⣏⡅⠲⠈⠥⢀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠻⢆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠂⡈⠌⢢⠑⡌⢣⠝⡪⠔⣉⠠⠔⣁⠂⡐⢣⡽⠌⠀⠀⠀⠀⠒⠀⠄⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡐⠠⠑⠢⡑⢌⡱⠎⢋⠺⡣⠂⡐⠄⢣⣱⠓⠈⣁⡀⡴⢨⠂⠐⣄⠰⢀⡀⠀⠄⠀⠀⠄⠀⠈⠦⠄⠀⠀⠀⢳⣀⠀⠄⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠄⡁⢊⠅⠸⠄⠁⠀⡄⠛⠁⡜⠡⣈⠳⠥⠂⠀⠈⠁⡠⠄⢠⠈⣀⠀⢆⠘⡄⠀⡀⠀⠒⠢⠀⠀⠂⠀⠀⠀⠀⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠂⠐⠄⠊⠁⠀⠀⢉⠀⢂⠭⢰⣱⠋⠀⠀⡘⠀⠀⠀⠤⢀⢨⢣⠞⢣⠸⢎⠢⡐⡱⠌⡤⡠⠠⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

print(Fore.GREEN+ascii_art)
print("\n\nWelcome to SP2YT\n\n[*] Please Enter a valid Spotify link\n[*] Please Enter a your spotify ID and YOUTUBE ID and Secret IN THE SOURCE CODE\n[*] Your ID and Secret can be done and found here, once found copy it into the code: https://developer.spotify.com/dashboard/\n\n[!!!!!]DO not use large playlist otherwise your IP might be blocked\n")
link= str(input("Please enter the link to your spotify playlist:\t"))
try:
    playlist_id = link.split("/playlist/")[1].split("?")[0]
    print("Track id is:\t" + playlist_id)
except Exception as e:
    print(f"Please enter a valid spotify Playlist link:\n{e}")
  

print("Retrieving Playlists...\n\n")
tracks = getPlaylistTracks(f"{playlist_id}",SPOTIFYCLIENT,SPOTIFYSECRET)
print(Fore.YELLOW+"\n\nSong:\t\t\t\t\t\tArtist:")
for track in tracks:
    print(Fore.CYAN+f"{track[0]}\t\t\t\t\t\t{track[1]}\n")
    try:
        converter(str(search_first_video(f"{track[0]} {track[1]}",YOUTUBEKEY)))
    except:
        print("Failed")
    time.sleep(1)
    


