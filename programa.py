from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

engine = create_engine("sqlite:///db.db")
session = sessionmaker(bind=engine)()

class root:
    def __init__(self, master):
        self.master = master
        self.master['padx'] = 5
        self.master['pady'] = 5
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

    def new_game(self):
        self.new = Toplevel(self.master)
        self.app = Pre_Game_Window(self.new)

    def load_game(self):
        self.new = Toplevel(self.master)
        self.app = Load_Window(self.new)

    def see_history(self):
        self.new = Toplevel(self.master)
        self.app = History_Window(self.new)

    def kill(self):
        self.master.destroy()

class Pre_Game_Window:
    def __init__(self, master):
        self.master = master
        self.master['padx'] = 5
        self.master['pady'] = 5
        self.playerbase_label = Label(master, text="Choose players")
        self.playerbase_label.grid(row=0, column=1)
        self.playerbase_listbox = Listbox(master)
        self.playerbase_listbox.grid(row=1, column=0)
        self.create_btn = Button(master, text="New player", command=self.new_player)
        self.create_btn.grid(row=2, column=0)
        self.chosenplayers_listbox = Listbox(master)
        self.chosenplayers_listbox.grid(row=1, column=2)
        self.start_btn = Button(master, text="Start game", command=self.start_game)
        self.start_btn.grid(row=2, column=1)
        self.add_btn = Button(master, text="Add", command=self.add_player)
        self.add_btn.grid(row=1, column=1)
        self.remove_btn = Button(master, text="Remove", command=self.remove_player)
        self.remove_btn.grid(row=2, column=2)
        self.refresh_btn = Button(master, text="⟲", width=2, command=self.load_playerbase)
        self.refresh_btn.grid(row=0, column=0, sticky=W)
        self.load_playerbase()

    def load_playerbase(self):
        self.playerbase_listbox.delete(0, self.playerbase_listbox.size())
        list = session.query(Player).all()
        [self.playerbase_listbox.insert(END, i) for i in list]

    def new_player(self):
        self.new = Toplevel(self.master)
        self.app = New_Player_Window(self.new)

    def add_player(self):
        self.chosenplayers_listbox.insert(END, self.playerbase_listbox.get(ANCHOR))

    def remove_player(self):
        self.chosenplayers_listbox.delete(self.chosenplayers_listbox.curselection())

    def start_game(self):
        players = self.chosenplayers_listbox.get(0, END)
        self.new = Toplevel(self.master)
        self.app = Game_Window(self.new, players)

class New_Player_Window:
    def __init__(self, master):
        self.master = master
        self.fname_label = Label(master, text="First name")
        self.fname_label.grid(row=0, column=0)
        self.fname_entry = Entry(master)
        self.fname_entry.grid(row=0, column=1)
        self.fname_entry.bind("<Return>", lambda event: self.create_new())
        self.lname_label = Label(master, text="Last name")
        self.lname_label.grid(row=1, column=0)
        self.lname_entry = Entry(master)
        self.lname_entry.grid(row=1, column=1)
        self.lname_entry.bind("<Return>", lambda event: self.create_new())
        self.age_label = Label(master, text="Age")
        self.age_label.grid(row=2, column=0)
        self.age_entry = Entry(master)
        self.age_entry.grid(row=2, column=1)
        self.age_entry.bind("<Return>", lambda event: self.create_new())
        self.submit_btn = Button(master, text="Submit", command=self.create_new)
        self.submit_btn.grid(row=3, column=1)

    def create_new(self):
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        age = self.age_entry.get()
        player = Player(fname, lname, age)
        session.add(player)
        session.commit()
        self.master.destroy()
        messagebox.showinfo('Success', 'Player created successfully!')
    
class Game_Window:
    def __init__(self, master, players):
        self.master = master
        self.players = players
        self.playernametitle_label = Label(master, text="Player name", font=12, relief='groove', width=16)
        self.playernametitle_label.grid(row=0, column=0)
        for i in range(1,10):
            label = Label(master, text=f"{i}", font=12, relief='groove', width=6)
            label.grid(row=0, column=f"{i}")
        self.label_10 = Label(master, text="10", font=12, relief='groove', width=9)
        self.label_10.grid(row=0, column=10)
        self.sum_label = Label(master, text="Total", font=12, relief='groove', width=8)
        self.sum_label.grid(row=0, column=11)
        self.create_sheet()

    def create_sheet(self):
        for i in range(len(self.players)):
            player = self.players[i].split('.')
            self.player_label = Label(self.master, text=f"{player[1]}", font=12)
            self.player_label.grid(row=i+1, column=0, sticky=W)
            for j in range(1,10):
                entry1 = Entry(self.master, font=11, width=3, relief="groove")
                entry2 = Entry(self.master, font=11, width=3, relief="groove")
                entry1.grid(row=i+1, column=f"{j}", sticky=W)
                entry2.grid(row=i+1, column=f"{j}", sticky=E)
            self.entry10_1 = Entry(self.master, font=11, width=3, relief="groove")
            self.entry10_2 = Entry(self.master, font=11, width=3, relief="groove")
            self.entry10_3 = Entry(self.master, font=11, width=3, relief="groove")
            self.entry10_1.grid(row=i+1, column=10, sticky=W)
            self.entry10_2.grid(row=i+1, column=10)
            self.entry10_3.grid(row=i+1, column=10, sticky=E)
            self.sum = Button(self.master, text="", font=11, width=6, relief='flat', command=self.total_sum)

    def total_sum(self):
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