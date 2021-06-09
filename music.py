def resumemusic():
    root.PauseButton.grid()
    root.ResumeButton.grid_remove()
    mixer.music.unpause()

def volumeUp():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1) 
def volumeDown():
    
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1) 
def stopMusic():
    mixer.music.stop()
def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()

def pausemusic():
    mixer.music.pause()
    root.ResumeButton.grid()
    root.PauseButton.grid_remove()
def musicurl():
    dd= filedialog.askopenfilename()
    audiotrack.set(dd)
def createwidthes():
    pass





    ################################## Labels
    TrackLabel = Label(root, text='Select Audio Track:', background='lightskyblue', font=('ariel', 15, 'italic bold'))
    TrackLabel.grid(row=0, column=0, padx=20, pady=20)
    ##################################Entry box
    TrackLabelEntry = Entry(root, font=('ariel', 16, 'italic bold'), width=35,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0, column=1, padx=20, pady=20)
    #######################################################################Buttons
    BrowseButton = Button(root, text='Search', bg='deeppink', font=('ariel', 13, 'italic bold'), width=20, bd=5,
                          activebackground='purple4',command=musicurl)
    BrowseButton.grid(row=0, column=2, padx=20, pady=20)

    PlayButton = Button(root, text='Play', bg='green2', font=('ariel', 13, 'italic bold'), width=20, bd=5,
                        activebackground='purple4',command=playmusic)
    PlayButton.grid(row=1, column=0, padx=20, pady=20)

    root.PauseButton = Button(root, text='Pause', bg='Yellow', font=('ariel', 13, 'italic bold'), width=20, bd=5,
                         activebackground='purple4',command=pausemusic)
    root.PauseButton.grid(row=1, column=1, padx=20, pady=20)
    root.ResumeButton = Button(root, text='Resume', bg='Yellow', font=('ariel', 13, 'italic bold'), width=20, bd=5,
                         activebackground='purple4',command=resumemusic)
    root.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
    root.ResumeButton.grid_remove()
    root.mutebutton=Button(root,text='Mute',width=100,bg='orange',activebackground='purple4',bd=5)
    root.mutebutton.grid(row=3,column=3)

    VolumeupButton = Button(root, text='Volumeup', bg='Blue', font=('ariel', 13, 'italic bold'), width=20, bd=5,
                            activebackground='purple4',command=volumeUp)
    VolumeupButton.grid(row=1, column=2, padx=20, pady=20)


    StopButton = Button(root, text='Stop', bg='Red', font=('ariel', 13, 'italic bold'), width=20, bd=5,
                        activebackground='purple4',command=stopMusic)
    StopButton.grid(row=2, column=0, padx=20, pady=20)

    VolumedownButton = Button(root, text='Volumedown', bg='Blue', font=('ariel', 13, 'italic bold'), width=20, bd=5,
                              activebackground='purple4',command=volumeDown)
    VolumedownButton.grid(row=2, column=2, padx=20, pady=20)


#################################################################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer




root = Tk()
root.geometry('1100x500+200+50')
root.title("sandy music player")
root.resizable(False, False)
root.configure(bg='lightskyblue')
#########################################################################################Global variable
audiotrack = StringVar()
###########################################################################################Create slider
ss = 'Devloped By Sandy'
count = 0
text = ''
SliderLabel = Label(root, text=ss, bg='lightskyblue', font=('ariel', 40, 'italic bold'))
SliderLabel.grid(row=3, column=0, padx=20, pady=20, columnspan=3)


def IntroLabelTRick():
    global count, text
    if (count >= len(ss)):
        count = -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text + ss[count]
        SliderLabel.configure(text=text)
    count += 1
    SliderLabel.after(200, IntroLabelTRick)


IntroLabelTRick()
mixer.init()

createwidthes()

root.mainloop()

