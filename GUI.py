from tkinter import *
from PIL import Image, ImageTk
import requests  # Using this library to access HTTP/HTTPs through python, receive our images/videos from the web,
# pretty much anything that has to do with python and the internet relies on this library!
import re  # Using this mainly to verify user input URLs or correct them to get the perfect input to match the request function
from datetime import datetime  # The program names files by generating timestamps of downloading the file! Hence this
# is needed to obtain a date and time for the file naming purposes
from tqdm import tqdm  # Just added as a base/outline to help make the loading bar in the actual GUI, as both of them
# use a similar library anyway (tqdm for code progress bars and tqdm.gui for gui progress bars)
# Progress bars help because they can 1- Let the user know if they're really downloading something or stuck
# 2- Let them know how long they'll wait for, especially if it's a video file that can be large
import instaloader
from instaloader import Post  # This establishes a connection with Instagram API, because if you access
# instagram as a bot, they have bot detection measures and block you out, hence we use the API provided!
L = instaloader.Instaloader()

# Code Intro
print(''' 

            XMUM AIT102 22/04 Python Group 3 Present:
                        InstaGrab V1.0
    Omar Mahmoud ~ Yap Wei Herng ~ Wong Zhan Song ~ Chia Xiu Xiang

''')
USER = input("Enter your username: ")
PASSWORD = input("Enter your password: ")
L.login(USER, PASSWORD)        # (login)
print("Logged in successfully!")

# This function is just to test if internet works for user, if doesnt work we close the program.
# (Running the program with no internet connection can lead to disaster)
def connection(url='http://www.youtube.com',
  timeout=5):  # Using youtube.com as the test website, as almost never goes down
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        print("Internet Connection successful!\n")
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
            e.response.status_code))
    except requests.ConnectionError:
        print("You aren't connected to the internet!")
    return False

# Function
def download_video(url):
    x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com',
                 url)  # makes sure URL is truly an instagram link, in the media format as image or video.
    #  If instagram ever updates their media link format we need to change this accordingly
    shortcode = re.search('(?:https?:\/\/)?(?:www.)?instagram.com\/?([a-zA-Z0-9\.\_\-]+)?\/([p]+)?([reel]+)?([tv]+)?([stories]+)?\/([a-zA-Z0-9\-\_\.]+)\/?([0-9]+)?',url)
    shortcode = shortcode.group(6)
    post = Post.from_shortcode(L.context, shortcode)


    try:
        if x:  # x is the verified/correctly formatted URL
            request_image = requests.get(url)
            src = request_image.content.decode('utf-8')  # page source obtaining function2
            msg = input("You are trying to download a video. Do you want to continue? (Yes or No): ".lower())
            if msg == "yes":
                print("Downloading the video...")
                L.download_post(post, target="Downloads")
                extract_video_link = re.search(r'<video class="_ab1d"*src="()"', src) # Scans for video link
                video_link = extract_video_link.group(1) # Captures whats in the parenthesis
                final = re.sub('<video class="_ab1d"*src="', '', video_link) # Puts video link into proper format
                _response = requests.get(final).content
                file_size_request = requests.get(final, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()

                print("Video downloaded successfully")

            if msg == "no":
                exit()
        else:
            print("Entered URL is not an instagram.com URL.")
    except:
            print("Done!")
            Download_Completion_Label.config(text="Done")

def download_image(url):
    x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)
    # makes sure URL is truly an instagram link, in the
    # media format as image or video. If instagram ever updates their media link format we need to change this accordingly
    shortcode = re.search('(?:https?:\/\/)?(?:www.)?instagram.com\/?([a-zA-Z0-9\.\_\-]+)?\/([p]+)?([reel]+)?([tv]+)?([stories]+)?\/([a-zA-Z0-9\-\_\.]+)\/?([0-9]+)?',url)
    shortcode = shortcode.group(6)
    post = Post.from_shortcode(L.context, shortcode)

    try:
        if x:  # x is the verified/correctly formatted URL
            request_image = requests.get(url)
            src = request_image.content.decode('utf-8')  # page source obtaining function2
            msg = input("You are trying to download an image. Do you want to continue? (Yes or No): ".lower())
            if msg == "yes":
                print("\nDownloading the image...")
                L.download_post(post, target="Downloads")
                extract_image_link = re.search(r'<img alt=*src="()"', src)
                image_link = extract_image_link.group()
                final = re.sub('<img alt=*src="()', '', image_link)
                _response = requests.get(final).content
                file_size_request = requests.get(final, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H:%M:%S')
                t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.jpg', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                print("Image downloaded successfully")

            if msg == "no":
                exit()
        else:
            print("Entered URL is not an instagram.com URL.")
    except:
        print("Done!")
        Download_Completion_Label.config(text="Done")

if connection() == True:  # This is the main function of the program, uses both connection test and instagrab function to make it work.
    # Logo
    Logo_Open = Image.open("GUI/Instagram.png")
    Logo_Resize = Logo_Open.resize((50, 50))
    Logo_Resize.save("GUI/Instagram.ico")

    # Main Screen
    window = Tk()
    window['bg'] = '#AA11ED'
    window.title("Instagrab")
    window.iconbitmap("GUI/Instagram.ico")

    # Picture
    Picture_Open = Image.open("GUI/picture.png")
    Video_Open = Image.open("GUI/video.png")

    Picture_Resize = Picture_Open.resize((50, 50))
    Video_Resize = Video_Open.resize((50, 50))

    Picture_Image = ImageTk.PhotoImage(Picture_Resize)
    Video_Image = ImageTk.PhotoImage(Video_Resize)

    # Frame
    Dummy_Frame_5 = Frame(window)
    Dummy_Frame_5.pack(side=TOP)

    Title_Frame = Frame(window)
    Title_Frame.pack(side=TOP)

    Dummy_Frame_1 = Frame(window)
    Dummy_Frame_1.pack(side=TOP)

    Instagram_URL_Frame = Frame(window, bg="#AA11ED")
    Instagram_URL_Frame.pack(side=TOP)

    Dummy_Frame_2 = Frame(window)
    Dummy_Frame_2.pack(side=TOP)

    Button_Frame = Frame(window)
    Button_Frame.pack(side=TOP)

    Picture_Frame = Frame(window)
    Picture_Frame.pack(side=TOP)

    Dummy_Frame_4 = Frame(window)
    Dummy_Frame_4.pack(side=TOP)

    Download_Completion_Frame = Frame(window)
    Download_Completion_Frame.pack(side=TOP)

    Dummy_Frame_3 = Frame(window)
    Dummy_Frame_3.pack(side=BOTTOM)

    # Label
    Title_Label = Label(Title_Frame, text="Instagram Downloader", font=("Delargo DT Black Italic", 30, "bold"), padx=20,
                        bg="#AA11ED", fg="white")
    Title_Label.pack(side=TOP)

    Instagram_URL_Label = Label(Instagram_URL_Frame, text="Enter the instagram URL below", font=("Delargo DT Black Italic", 14),
                                bg="#AA11ED", fg="white")
    Instagram_URL_Label.pack(side=TOP)

    Download_Completion_Label = Label(Download_Completion_Frame, bg="#AA11ED", fg="white", font=("Delargo DT Black Italic", 14))
    Download_Completion_Label.pack(side=BOTTOM)

    # Dummy Label
    Dummy_Label_1 = Label(Dummy_Frame_1, bg="#AA11ED", fg="white")
    Dummy_Label_1.pack(side=TOP)

    Dummy_Label_2 = Label(Dummy_Frame_2, bg="#AA11ED", fg="white")
    Dummy_Label_2.pack(side=TOP)

    Dummy_Label_3 = Label(Dummy_Frame_3, bg="#AA11ED", fg="white")
    Dummy_Label_3.pack(side=BOTTOM)

    Dummy_Label_4 = Label(Dummy_Frame_4, bg="#AA11ED", fg="white")
    Dummy_Label_4.pack(side=TOP)

    Dummy_Label_5 = Label(Dummy_Frame_5, bg="#AA11ED", fg="white")
    Dummy_Label_5.pack(side=TOP)

    # Entry
    Instagram_URl = StringVar()
    Instagram_URL_Entry = Entry(Instagram_URL_Frame, textvariable=Instagram_URl, width=40, font=("Delargo DT Black Italic", 12))
    Instagram_URL_Entry.pack(side=LEFT)

    # Button
    Download_Image_Button = Button(Button_Frame, text="Download Image", width=200, image=Picture_Image, compound=TOP,
                                   font=("Delargo DT Black Italic", 10), bg="white", fg="#AA11ED", command=lambda: download_image(Instagram_URl.get()))
    Download_Image_Button.pack(side=LEFT)

    Download_Video_Button = Button(Button_Frame, text="Download Video", width=200, image=Video_Image, compound=TOP,
                                   font=("Delargo DT Black Italic", 10), bg="white", fg="#AA11ED", command=lambda: download_video(Instagram_URl.get()))
    Download_Video_Button.pack(side=RIGHT)

    window.mainloop()
else:
    quit()
