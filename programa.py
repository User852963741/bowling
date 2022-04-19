from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from tkinter import *
from PIL import ImageTk, Image

engine = create_engine("sqlite:///db.db")
session = sessionmaker(bind=engine)()

class root:
    def __init__(self, master):
        self.master = master
        self.banner_img = ImageTk.PhotoImage(Image.open("banner.jpg"))
        self.banner = Label(master, image=self.banner_img)
        self.banner.grid(row=0, columnspan=3)
        self.newgame_button = Button(master, text="New game", command=self.new_game)
        self.newgame_button.grid(row=1, column=1)
        self.load_button = Button(master, text="Load game", command=self.load_game)
        self.load_button.grid(row=2, column=1)
        self.history_button = Button(master, text="History", command=self.see_history)
        self.history_button.grid(row=3, column=1)
        self.exit_button = Button(master, text="Exit", command=self.kill)
        self.exit_button.grid(row=4, column=1)

    def new_game(self, master):
        self.new = Toplevel(self.master)
        self.app = New_Game_Window(self.new)

    def load_game(self, master):
        self.new = Toplevel(self.master)
        self.app = Load_Window(self.new)

    def see_history(self, master):
        self.new = Toplevel(self.master)
        self.app = History_Window(self.new)

    def kill(self):
        self.master.destroy()

class New_Game_Window:
    def __init__(self):
        pass

class Load_Window:
    def __init__(self):
        pass

class History_Window:
    def __init__(self):
        pass

def main():
    master = Tk()
    app = root(master)
    master.mainloop()

if __name__ == '__main__':
    main()