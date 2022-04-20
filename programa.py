from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import date
import time


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
        self.history_button = Button(master, text="History", command=self.see_history)
        self.history_button.grid(row=2, column=1)
        self.exit_button = Button(master, text="Exit", command=self.kill)
        self.exit_button.grid(row=3, column=1)

    def new_game(self):
        self.new = Toplevel(self.master)
        self.app = Pre_Game_Window(self.new)

    def see_history(self):
        self.new = Toplevel(self.master)
        self.app = History_Window(self.new)

    def kill(self):
        self.master.destroy()

class Pre_Game_Window:
    def __init__(self, master):
        self.master = master
        self.master['pady'] = 20
        self.master['padx'] = 20
        self.playerbase_label = Label(master, text="Choose players", font=16)
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

class Player_sheet:
    def __init__(self, master, id, name, i):
        self.master = master
        self.name = name
        self.id = id
        self.i = i
        self.var1 = StringVar()
        self.var1.set("0")
        self.var1_2 = StringVar()
        self.var1_2.set("0")
        self.var2 = StringVar()
        self.var2.set("0")
        self.var2_2 = StringVar()
        self.var2_2.set("0")
        self.var3 = StringVar()
        self.var3.set("0")
        self.var3_2 = StringVar()
        self.var3_2.set("0")
        self.var4 = StringVar()
        self.var4.set("0")
        self.var4_2 = StringVar()
        self.var4_2.set("0")
        self.var5 = StringVar()
        self.var5.set("0")
        self.var5_2 = StringVar()
        self.var5_2.set("0")
        self.var6 = StringVar()
        self.var6.set("0")
        self.var6_2 = StringVar()
        self.var6_2.set("0")
        self.var7 = StringVar()
        self.var7.set("0")
        self.var7_2 = StringVar()
        self.var7_2.set("0")
        self.var8 = StringVar()
        self.var8.set("0")
        self.var8_2 = StringVar()
        self.var8_2.set("0")
        self.var9 = StringVar()
        self.var9.set("0")
        self.var9_2 = StringVar()
        self.var9_2.set("0")
        self.var10_1 = StringVar()
        self.var10_1.set("0")
        self.var10_2 = StringVar()
        self.var10_2.set("0")
        self.var10_3 = StringVar()
        self.var10_3.set("0")
        self.player_label = Label(self.master, text=f"{name}", font=12)
        self.player_label.grid(row=i+1, column=0, sticky=W)
        self.entry1 = Entry(self.master, textvariable=self.var1, font=11, width=3, relief="groove")
        self.entry1_2 = Entry(self.master, textvariable=self.var1_2, font=11, width=3, relief="groove")
        self.entry2 = Entry(self.master, textvariable=self.var2, font=11, width=3, relief="groove")
        self.entry2_2 = Entry(self.master, textvariable=self.var2_2, font=11, width=3, relief="groove")
        self.entry3 = Entry(self.master, textvariable=self.var3, font=11, width=3, relief="groove")
        self.entry3_2 = Entry(self.master, textvariable=self.var3_2, font=11, width=3, relief="groove")
        self.entry4 = Entry(self.master, textvariable=self.var4, font=11, width=3, relief="groove")
        self.entry4_2 = Entry(self.master, textvariable=self.var4_2, font=11, width=3, relief="groove")
        self.entry5 = Entry(self.master, textvariable=self.var5, font=11, width=3, relief="groove")
        self.entry5_2 = Entry(self.master, textvariable=self.var5_2, font=11, width=3, relief="groove")
        self.entry6 = Entry(self.master, textvariable=self.var6, font=11, width=3, relief="groove")
        self.entry6_2 = Entry(self.master, textvariable=self.var6_2, font=11, width=3, relief="groove")
        self.entry7 = Entry(self.master, textvariable=self.var7, font=11, width=3, relief="groove")
        self.entry7_2 = Entry(self.master, textvariable=self.var7_2, font=11, width=3, relief="groove")
        self.entry8 = Entry(self.master, textvariable=self.var8, font=11, width=3, relief="groove")
        self.entry8_2 = Entry(self.master, textvariable=self.var8_2, font=11, width=3, relief="groove")
        self.entry9 = Entry(self.master, textvariable=self.var9, font=11, width=3, relief="groove")
        self.entry9_2 = Entry(self.master, textvariable=self.var9_2, font=11, width=3, relief="groove")
        self.entry10_1 = Entry(self.master, textvariable=self.var10_1, font=11, width=3, relief="groove")
        self.entry10_2 = Entry(self.master, textvariable=self.var10_2, font=11, width=3, relief="groove")
        self.entry10_3 = Entry(self.master, textvariable=self.var10_3, font=11, width=3, relief="groove")
        self.player_label = Label(self.master, text=f"{name}", font=12)
        self.player_label.grid(row=i+1, column=0, sticky=W)
        self.entry1.bind("<KeyRelease>", self.check_and_sum)
        self.entry1_2.bind("<KeyRelease>", self.check_and_sum)
        self.entry2.bind("<KeyRelease>", self.check_and_sum)
        self.entry2_2.bind("<KeyRelease>", self.check_and_sum)
        self.entry3.bind("<KeyRelease>", self.check_and_sum)
        self.entry3_2.bind("<KeyRelease>", self.check_and_sum)
        self.entry4.bind("<KeyRelease>", self.check_and_sum)
        self.entry4_2.bind("<KeyRelease>", self.check_and_sum)
        self.entry5.bind("<KeyRelease>", self.check_and_sum)
        self.entry5_2.bind("<KeyRelease>", self.check_and_sum)
        self.entry6.bind("<KeyRelease>", self.check_and_sum)
        self.entry6_2.bind("<KeyRelease>", self.check_and_sum)
        self.entry7.bind("<KeyRelease>", self.check_and_sum)
        self.entry7_2.bind("<KeyRelease>", self.check_and_sum)
        self.entry8.bind("<KeyRelease>", self.check_and_sum)
        self.entry8_2.bind("<KeyRelease>", self.check_and_sum)
        self.entry9.bind("<KeyRelease>", self.check_and_sum)
        self.entry9_2.bind("<KeyRelease>", self.check_and_sum)
        self.entry10_1.bind("<KeyRelease>", self.check_and_sum)
        self.entry10_2.bind("<KeyRelease>", self.check_and_sum)
        self.entry10_3.bind("<KeyRelease>", self.check_and_sum)
        self.entry1.grid(row=i+1, column=1, sticky=W)
        self.entry1_2.grid(row=i+1, column=1, sticky=E)
        self.entry2.grid(row=i+1, column=2, sticky=W)
        self.entry2_2.grid(row=i+1, column=2, sticky=E)
        self.entry3.grid(row=i+1, column=3, sticky=W)
        self.entry3_2.grid(row=i+1, column=3, sticky=E)
        self.entry4.grid(row=i+1, column=4, sticky=W)
        self.entry4_2.grid(row=i+1, column=4, sticky=E)
        self.entry5.grid(row=i+1, column=5, sticky=W)
        self.entry5_2.grid(row=i+1, column=5, sticky=E)
        self.entry6.grid(row=i+1, column=6, sticky=W)
        self.entry6_2.grid(row=i+1, column=6, sticky=E)
        self.entry7.grid(row=i+1, column=7, sticky=W)
        self.entry7_2.grid(row=i+1, column=7, sticky=E)
        self.entry8.grid(row=i+1, column=8, sticky=W)
        self.entry8_2.grid(row=i+1, column=8, sticky=E)
        self.entry9.grid(row=i+1, column=9, sticky=W)
        self.entry9_2.grid(row=i+1, column=9, sticky=E)
        self.entry10_1.grid(row=i+1, column=10, sticky=W)
        self.entry10_2.grid(row=i+1, column=10)
        self.entry10_3.grid(row=i+1, column=10, sticky=E)
        self.sum_var = StringVar()
        self.total_sum = Label(self.master, textvariable=self.sum_var, font=11, width=6)
        self.total_sum.grid(row=i+1, column=11)

    def check_and_sum(self, master):

        entries = [self.var1, self.var1_2, self.var2, self.var2_2, self.var3, self.var3_2, self.var4, self.var4_2, self.var5, self.var5_2, self.var6, self.var6_2, self.var7, self.var7_2, self.var8, self.var8_2, self.var9, self.var9_2, self.var10_1, self.var10_2, self.var10_3]
        
        suma = 0

        for i in range(0,21):
            if entries[i].get() == "/":
                suma += 10
                if i != 18 and i != 19 and i != 20 and entries[i+2].get() == "X":
                    suma += 10
            elif entries[i].get() == "X":
                suma += 10
                if i != 17 and i != 18 and i != 19 and i != 20 and entries[i+2].get() == "X":
                    suma += 20
                elif i != 17 and i != 18 and i != 19 and i != 20 and entries[i+2].get() != "X":
                    suma += int(entries[i+1].get())
                elif i == 18 or i == 19:
                    suma += 10
                elif i == 20:
                    if entries[i-1].get() == "/":
                        suma += 10
            elif entries[i].get() == "10":
                if i == 18 or i == 19 or i == 20:
                    entries[i].set("X")
                else:
                    entries[i].set("0")
                    entries[i+1].set("X")
            elif entries[i].get() != "X" and entries[i].get() != "/":
                suma += int(entries[i].get())
                if entries[i-1].get() != "X" and entries[i-1].get() != "/":
                    if i != 18 and i % 2 != 0:
                        if int(entries[i-1].get()) + int(entries[i].get()) == 10:
                            entries[i].set("/")
                if i == 20 and entries[i-1].get() == "/":
                    suma += int(entries[i].get())
                elif entries[i-1].get() == "/":
                    suma += int(entries[i].get())
                elif i == 18:
                    if entries[i-1].get() == "/" or entries[i-1].get() == "X":
                        suma += int(entries[i].get())
        self.sum_var.set(suma)

    def __str__(self):
        return f"{self.name} {self.sum_var.get()}"

class Game_Window:
    def __init__(self, master, players):
        self.master = master
        self.master['pady'] = 20
        self.master['padx'] = 20
        self.players = players
        self.player_list = []
        self.scores = []
        self.playernametitle_label = Label(master, text="Player name", font=12, relief='groove', width=16)
        self.playernametitle_label.grid(row=0, column=0)
        for i in range(1,10):
            label = Label(master, text=f"{i}", font=12, relief='groove', width=6)
            label.grid(row=0, column=f"{i}")
        self.label_10 = Label(master, text="10", font=12, relief='groove', width=9)
        self.label_10.grid(row=0, column=10)
        self.sum_label = Label(master, text="Total", font=12, relief='groove', width=8)
        self.sum_label.grid(row=0, column=11)
        for i in range(len(self.players)):
            self.create_sheet(i)
        self.finish_button = Button(master, text="Finish game", width=12, command=self.finish_game)
        self.finish_button.grid(row=0, column=12)
        self.finish_label = Label(master, text="", font=12)
        self.finish_label.grid(row=1, column=12)

    def create_sheet(self, i):
        player = self.players[i].split('.')
        id = player[0]
        name = player[1]
        self.player_list.append(Player_sheet(self.master, id, name, i))

    def finish_game(self):
        for player in self.player_list:
            score = player.sum_var.get()
            self.scores.append([int(score), str(player.name), int(player.id)])
        self.scores.sort(reverse=True)
        if len(self.scores) > 1:
            if self.scores[0][0] == self.scores[1][0]:
                first = self.scores[0]
                second = self.scores[1]
                self.finish_label['text'] = f"{first[1]} and {second[1]} are sharing the throne with {first[0]} points!"
            else:
                winner = self.scores[0]
                self.finish_label['text'] = f"{winner[1]} destroyed the competition with {winner[0]} points!"
        else:
            winner = self.scores[0]
            self.finish_label['text'] = f"{winner[1]} beat themselves with {winner[0]} points!"

        game = Game()
        for entry in self.scores:
            player_id = entry[2]
            score = entry[0]
            result = Result(player_id=player_id, score=score)
            game.results.append(result)
            session.add(game)
        session.commit()

class History_Window:   
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x300')
        self.master['pady'] = 20
        self.master['padx'] = 20
        self.left_frame = Frame(master)
        self.right_frame = Frame(master)
        self.left_frame.pack(side=LEFT)
        self.right_frame.pack(side=RIGHT)
        self.title_label = Label(master, text="Game history", font=16)
        self.title_label.pack()
        self.search_listbox = Listbox(self.left_frame, width=35)
        self.search_listbox.pack()
        self.search_by_player_button = Button(self.left_frame, text="Load players", command=self.load_players)
        self.search_by_player_button.pack(anchor='s', side=LEFT)
        self.search_by_game_button = Button(self.left_frame, text="Load games", command=self.load_games)
        self.search_by_game_button.pack(anchor='s', side=RIGHT)
        self.search_button = Button(self.left_frame, text="Search", command=self.search)
        self.search_button.pack(side=BOTTOM)

    def load_players(self):
        self.search_listbox.delete(0, self.search_listbox.size())
        list = session.query(Player).all()
        [self.search_listbox.insert(END, f"{i.id} | {i.fname}") for i in list]
        self.master.results_label.destroy()

    def load_games(self):
        self.search_listbox.delete(0, self.search_listbox.size())
        list = session.query(Game).all()
        [self.search_listbox.insert(END, f"{i.id} | {i.date}") for i in list]

    def search(self):
        choice = self.search_listbox.get(ANCHOR)
        if choice[-3] == "-":
            list = choice.split("|")
            id = int(list[0])
            date = list[1]
            search = session.query(Result).filter(
                Result.game_id==id
            ).all()
            for entry in search:
                self.results_label = Label(self.right_frame, text="")
                self.results_label.pack(anchor='w')
                self.results_label['text'] = entry
        else:
            list = choice.split("|")
            id = int(list[0])
            print(id)
            fname = str(list[1])
            search = session.query(Game).filter(
                Game.players==id
            ).all()
            for entry in search:
                self.results_label = Label(self.right_frame, text="")
                self.results_label.pack(anchor='w')
                self.results_label['text'] = entry
        
def main():
    master = Tk()
    app = root(master)
    master.mainloop()

if __name__ == '__main__':
    main()