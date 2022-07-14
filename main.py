import tkinter


class WelcomeWindow(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.newSongDetailsWindow = None
        self.SongDetailsWindow = None
        self.master.title("SongWritingSupportTools")
        self.master.geometry("700x500")
        SongDetailsButton = tkinter.Button(text="新しい歌詞を作る", command=self.onSongDetailsButton)
        SongDetailsButton.pack()

    def onSongDetailsButton(self):
        self.newSongDetailsWindow = tkinter.Toplevel(self)
        self.SongDetailsWindow = SongDetailsWindow(self.newSongDetailsWindow)


class SongDetailsWindow(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("新しい歌詞")
        self.master.geometry("400x200")
        self.SongTitleEntry = tkinter.Entry(width=50)
        self.SongTitleEntry.pack()


if __name__ == "__main__":
    root = tkinter.Tk()
    welcomeWindow = WelcomeWindow(master=root)
    welcomeWindow.mainloop()
