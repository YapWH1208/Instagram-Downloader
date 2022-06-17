from tkinter import *
from tkinter import colorchooser
from PIL import Image, ImageTk

# Function
def colour_picker():
    New_Colour = colorchooser.askcolor(title="Pick your colour")
    Instagram_URL_Entry.config(fg=New_Colour[1])

# Logo
Logo_Open = Image.open("GUI/Instagram.png")
Logo_Resize = Logo_Open.resize((50, 50))
Logo_Resize.save("GUI/Instagram.ico")

# Main Screen
window = Tk()
window['bg'] = '#AA11ED'
window.title("Instagram Downloader")
window.iconbitmap("GUI/Instagram.ico")

# Picture
Picture_Open = Image.open("GUI/picture.png")
Video_Open = Image.open("GUI/video.png")
Color_Open = Image.open("GUI/color.png")

Picture_Resize = Picture_Open.resize((50, 50))
Video_Resize = Video_Open.resize((50, 50))
Color_Resize = Color_Open.resize((17, 17))

Picture_Image = ImageTk.PhotoImage(Picture_Resize)
Video_Image = ImageTk.PhotoImage(Video_Resize)
Color_Image = ImageTk.PhotoImage(Color_Resize)

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
Colour_Picker_Button = Button(Instagram_URL_Frame, command=colour_picker, font=("Delargo DT Black Italic", 10), image=Color_Image)
Colour_Picker_Button.pack(side=RIGHT)

Download_Picture_Button = Button(Button_Frame, text="Download Picture", width=200, image=Picture_Image, compound=TOP,
                               font=("Delargo DT Black Italic", 10), bg="white", fg="#AA11ED")
Download_Picture_Button.pack(side=LEFT)

Download_Video_Button = Button(Button_Frame, text="Download Video", width=200, image=Video_Image, compound=TOP,
                               font=("Delargo DT Black Italic", 10), bg="white", fg="#AA11ED")
Download_Video_Button.pack(side=RIGHT)

window.mainloop()
