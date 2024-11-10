# METHODS IMPORTATION 
import tkinter
from turtle import title
import customtkinter
from pytube import YouTube

# START-DOWNLOADING FUNCTION as Video
def startVideoDownload():
    try:
        youtubeLink = link.get()
        ytbObject = YouTube(youtubeLink, on_progress_callback=on_progress)
        video = ytbObject.streams.get_highest_resolution()

        title.configure(text=ytbObject.title, text_color="black") 
        DownloadDone.configure(text="")
        video.download()
        DownloadDone.configure(text="Video Downloaded Successfully!", text_color="green")
    except:
        DownloadDone.configure(text="Youtube Link Not Working!", text_color="red")


# START-DOWNLOADING FUNCTION as audio
def startAudioDownload():
    try:
        youtubeLink = link.get()
        ytbObject = YouTube(youtubeLink, on_progress_callback=on_progress)
        audio = ytbObject.streams.get_audio_only()
        
        title.configure(text=ytbObject.title, text_color="black")
        DownloadDone.configure(text="")
        audio.download()
        DownloadDone.configure(text="Audio Downloaded Successfully!", text_color="green")
    except :
        DownloadDone.configure(text="Youtube Link Not Working!", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_process = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_process))
    pPercentage.configure(text=per + "%")
    pPercentage.update()
    # progBar Updates
    progBar.set(percentage_of_process / 100)  

# UI Options
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")  

# frame Setting
app = customtkinter.CTk()
app.geometry("680x400")
app.title("HakooDev_ | MP3/MP4 Downloader")

# MP4 Download Section
title_video = customtkinter.CTkLabel(app, text="Download it as MP4")
title_video.pack(padx=10, pady=10)

url_var_video = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=30, textvariable=url_var_video)
link.pack()

download_video = customtkinter.CTkButton(app, text="Download Video", command=startVideoDownload)
download_video.pack(padx=10, pady=10)

# MP3 Download Section
title_audio = customtkinter.CTkLabel(app, text="Download it as MP3")
title_audio.pack(padx=10, pady=10)

url_var_audio = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=30, textvariable=url_var_audio)
link.pack()

download_audio = customtkinter.CTkButton(app, text="Download Audio", command=startAudioDownload)
download_audio.pack(padx=10, pady=10)

# Progress Bar
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progBar = customtkinter.CTkProgressBar(app, width=500)
progBar.set(0)
progBar.pack(padx=10, pady=10)

# Download Done
DownloadDone = customtkinter.CTkLabel(app, text="")
DownloadDone.pack()

# Launching App
app.mainloop()
