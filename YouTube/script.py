import setupp
modules_used = ["pytube","cowsay"]
setupp.inp(modules_used)

import pytube
import cowsay as cs

def get_choice():
    return(int(input("\n1. Only Video \n2. Only Audio \n3. Only audio and Only video(High Quality) \n4. Both Audio and Video \n5. Show All \nEnter Choice \n-> ")))

def get_link():
    return(input("Enter link \n-> "))

def get_id():
    return(int(input("\nEnter stream itag \n-> ")))

try:
    link = get_link()
    video = pytube.YouTube(link,use_oauth=True, allow_oauth_cache=True)
    print(f"Video Selected : {video.title}\n")
    list = video.streams.filter(file_extension='mp4')
except:
    print(Exception)

try:
    choice = get_choice()
except:
    print(Exception)
    choice = get_choice()

if choice==1:
    list = video.streams.filter(file_extension='mp4')
    for i in list:
        print(i)

elif choice==2:
    list = video.streams.filter(only_audio=True)
    for i in list:
        print(i)

elif choice==3:
    list = video.streams.filter(adaptive=True)
    for i in list:
        print(i)

elif choice==4:
    list = video.streams.filter(progressive=True)
    for i in list:
        print(i)

elif choice==5:
    list = video.streams
    for i in list:
        print(i)

else:
    print("Enter a valid choice")
    get_choice()

try:
    id = get_id()
except:
    print(Exception)
    get_id()

try:
    stream = video.streams.get_by_itag(id)
    size = video.streams.get_by_itag(id).filesize
except:
    print(Exception)
    get_id()

try:    
    cs.cow("Video is downloading")
except:
    print()
try:
    a = stream.download()    
    print(f'\nVideo Downloaded \n-> {video.title}\n')
    print(f"File Location \n-> {a}")
    print('\nThanks 💗')
except:
    print(Exception)