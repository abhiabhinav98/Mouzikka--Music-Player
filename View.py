
import sys
import tkinter as tk
import tkinter.ttk as ttk
import musicplayer_support
import random
import sys
import threading
import time
from tkinter import filedialog, messagebox
from cx_Oracle import DatabaseError
from pygame import mixer
import player
import MyExceptions


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = View (root)
    musicplayer_support.init(root, top)
    root.mainloop()

class View:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font11 = "-family {Avenir Next Cyr Medium} -size 23 -weight "  \
            "normal -slant roman -underline 0 -overstrike 0"
        font12 = "-family {Avenir Next Cyr} -size 9 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {Vivaldi} -size 22 -weight " \
                 "bold -slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("687x526+558+155")
        top.title("New Toplevel")
        top.configure(background="#fff")
        self.top=top
        self.songName = tk.Label(top)
        self.songName.place(relx=0.437, rely=0.038, height=44, width=281)
        self.songName.configure(background="#fff")
        self.songName.configure(disabledforeground="#a3a3a3")
        self.songName.configure(font=font13)
        self.songName.configure(foreground="#000000")
        self.songName.configure(text='''Ladki Aankh Maare''')

        self.songProgress = ttk.Progressbar(top)
        self.songProgress.place(relx=0.393, rely=0.209, relwidth=0.495
                , relheight=0.0, height=7)


        self.songTotalDuration = ttk.Label(top)
        self.songTotalDuration.place(relx=0.844, rely=0.171, height=19, width=29)

        self.songTotalDuration.configure(background="#fff")
        self.songTotalDuration.configure(foreground="#3399ff")
        self.songTotalDuration.configure(font=font12)
        self.songTotalDuration.configure(relief='flat')


        self.songTimePassed = ttk.Label(top)
        self.songTimePassed.place(relx=0.393, rely=0.171, height=19, width=29)
        self.songTimePassed.configure(background="#ffffff")
        self.songTimePassed.configure(foreground="#000000")
        self.songTimePassed.configure(font=font12)
        self.songTimePassed.configure(relief='flat')


        self.pauseButton = tk.Button(top)
        self.pauseButton.place(relx=0.568, rely=0.266, height=34, width=34)
        self.pauseButton.configure(activebackground="#ececec")
        self.pauseButton.configure(activeforeground="#000000")
        self.pauseButton.configure(background="#fff")
        self.pauseButton.configure(borderwidth="0")
        self.pauseButton.configure(disabledforeground="#a3a3a3")
        self.pauseButton.configure(foreground="#000000")
        self.pauseButton.configure(highlightbackground="#d9d9d9")
        self.pauseButton.configure(highlightcolor="black")
        self._img1 = tk.PhotoImage(file="./icons/pause.png")
        self.pauseButton.configure(image=self._img1)
        self.pauseButton.configure(pady="0")
        self.pauseButton.configure(text='''Button''')

        self.playButton = tk.Button(top)
        self.playButton.place(relx=0.64, rely=0.266, height=34, width=34)
        self.playButton.configure(activebackground="#ececec")
        self.playButton.configure(activeforeground="#000000")
        self.playButton.configure(background="#fff")
        self.playButton.configure(borderwidth="0")
        self.playButton.configure(disabledforeground="#a3a3a3")
        self.playButton.configure(foreground="#000000")
        self.playButton.configure(highlightbackground="#d9d9d9")
        self.playButton.configure(highlightcolor="black")
        self._img2 = tk.PhotoImage(file="./icons/play.png")
        self.playButton.configure(image=self._img2)
        self.playButton.configure(pady="0")
        self.playButton.configure(text='''Button''')

        self.stopButton = tk.Button(top)
        self.stopButton.place(relx=0.713, rely=0.266, height=34, width=34)
        self.stopButton.configure(activebackground="#ececec")
        self.stopButton.configure(activeforeground="#000000")
        self.stopButton.configure(background="#fff")
        self.stopButton.configure(borderwidth="0")
        self.stopButton.configure(disabledforeground="#a3a3a3")
        self.stopButton.configure(foreground="#000000")
        self.stopButton.configure(highlightbackground="#d9d9d9")
        self.stopButton.configure(highlightcolor="black")
        self._img3 = tk.PhotoImage(file="./icons/stop.png")
        self.stopButton.configure(image=self._img3)
        self.stopButton.configure(pady="0")
        self.stopButton.configure(text='''Button''')

        self.vinylRecordImage = tk.Label(top)
        self.vinylRecordImage.place(relx=0.0, rely=0.0, height=204, width=204)
        self.vinylRecordImage.configure(background="#d9d9d9")
        self.vinylRecordImage.configure(disabledforeground="#a3a3a3")
        self.vinylRecordImage.configure(foreground="#000000")
        self._img4 = tk.PhotoImage(file="./icons/vinylrecord.png")
        self.vinylRecordImage.configure(image=self._img4)
        self.vinylRecordImage.configure(text='''Label''')

        self.playList = ScrolledListBox(top)
        self.playList.place(relx=0.0, rely=0.38, relheight=0.532, relwidth=0.999)

        self.playList.configure(background="white")
        self.playList.configure(disabledforeground="#a3a3a3")
        self.playList.configure(font="TkFixedFont")
        self.playList.configure(foreground="black")
        self.playList.configure(highlightbackground="#d9d9d9")
        self.playList.configure(highlightcolor="#d9d9d9")
        self.playList.configure(selectbackground="#c4c4c4")
        self.playList.configure(selectforeground="black")
        self.playList.configure(width=10)

        self.previousButton = tk.Label(top)
        self.previousButton.place(relx=0.509, rely=0.285, height=16, width=16)
        self.previousButton.configure(background="#fff")
        self.previousButton.configure(borderwidth="0")
        self.previousButton.configure(disabledforeground="#a3a3a3")
        self.previousButton.configure(foreground="#000000")
        self._img5 = tk.PhotoImage(file="./icons/previous.png")
        self.previousButton.configure(image=self._img5)
        self.previousButton.configure(text='''Label''')

        self.bottomBar = ttk.Label(top)
        self.bottomBar.place(relx=0.0, rely=0.913, height=49, width=686)
        self.bottomBar.configure(background="#d9d9d9")
        self.bottomBar.configure(foreground="#000000")
        self.bottomBar.configure(font="TkDefaultFont")
        self.bottomBar.configure(relief='flat')
        self.bottomBar.configure(width=686)
        self.bottomBar.configure(state='disabled')

        self.vol_scale = ttk.Scale(top)
        self.vol_scale.place(relx=0.015, rely=0.932, relwidth=0.146, relheight=0.0
                , height=26, bordermode='ignore')
        self.vol_scale.configure(takefocus="")

        self.addSongsToPlayListButton = tk.Button(top)
        self.addSongsToPlayListButton.place(relx=0.961, rely=0.323, height=17
                , width=17)
        self.addSongsToPlayListButton.configure(activebackground="#ececec")
        self.addSongsToPlayListButton.configure(activeforeground="#d9d9d9")
        self.addSongsToPlayListButton.configure(background="#fff")
        self.addSongsToPlayListButton.configure(borderwidth="0")
        self.addSongsToPlayListButton.configure(disabledforeground="#a3a3a3")
        self.addSongsToPlayListButton.configure(foreground="#000000")
        self.addSongsToPlayListButton.configure(highlightbackground="#d9d9d9")
        self.addSongsToPlayListButton.configure(highlightcolor="black")
        self._img6 = tk.PhotoImage(file="./icons/add.png")
        self.addSongsToPlayListButton.configure(image=self._img6)
        self.addSongsToPlayListButton.configure(pady="0")
        self.addSongsToPlayListButton.configure(text='''Button''')

        self.deleteSongsFromPlaylistButton = tk.Button(top)
        self.deleteSongsFromPlaylistButton.place(relx=0.917, rely=0.323
                , height=18, width=18)
        self.deleteSongsFromPlaylistButton.configure(activebackground="#ececec")
        self.deleteSongsFromPlaylistButton.configure(activeforeground="#000000")
        self.deleteSongsFromPlaylistButton.configure(background="#fff")
        self.deleteSongsFromPlaylistButton.configure(borderwidth="0")
        self.deleteSongsFromPlaylistButton.configure(disabledforeground="#a3a3a3")
        self.deleteSongsFromPlaylistButton.configure(foreground="#000000")
        self.deleteSongsFromPlaylistButton.configure(highlightbackground="#d9d9d9")
        self.deleteSongsFromPlaylistButton.configure(highlightcolor="black")
        self._img7 = tk.PhotoImage(file="./icons/delete.png")
        self.deleteSongsFromPlaylistButton.configure(image=self._img7)
        self.deleteSongsFromPlaylistButton.configure(pady="0")
        self.deleteSongsFromPlaylistButton.configure(text='''Button''')

        self.Button9 = tk.Button(top)
        self.Button9.place(relx=0.932, rely=0.913, height=42, width=42)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(borderwidth="0")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self._img8 = tk.PhotoImage(file="./icons/like.png")
        self.Button9.configure(image=self._img8)
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''Button''')
        self.Button9.configure(width=42)

        self.Button10 = tk.Button(top)
        self.Button10.place(relx=0.873, rely=0.913, height=42, width=42)
        self.Button10.configure(activebackground="#ececec")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(borderwidth="0")
        self.Button10.configure(disabledforeground="#a3a3a3")
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self._img9 = tk.PhotoImage(file="./icons/broken-heart.png")
        self.Button10.configure(image=self._img9)
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''Button''')
        self.Button10.configure(width=48)

        self.Button11 = tk.Button(top)
        self.Button11.place(relx=0.83, rely=0.932, height=26, width=26)
        self.Button11.configure(activebackground="#ececec")
        self.Button11.configure(activeforeground="#000000")
        self.Button11.configure(background="#d9d9d9")
        self.Button11.configure(borderwidth="0")
        self.Button11.configure(disabledforeground="#a3a3a3")
        self.Button11.configure(foreground="#000000")
        self.Button11.configure(highlightbackground="#d9d9d9")
        self.Button11.configure(highlightcolor="black")
        self._img10 = tk.PhotoImage(file="./icons/refresh.png")
        self.Button11.configure(image=self._img10)
        self.Button11.configure(pady="0")
        self.Button11.configure(text='''Button''')
        self.setup_player()

    def setup_player(self):
        try:
            self.my_player= player.Player()
            if self.my_player.get_db_status():
                messagebox.showinfo("Success!","Connected successfully to the DB.")
            else:
                raise Exception("Sorry! You cannot save or load favourites.")


        except Exception as e:
            print("DB Error",e)
            messagebox.showerror("DB Error", e)
            self.Button9.configure(state="disabled")
            self.Button10.configure(state="disabled")
            self.Button11.configure(state="disabled")

        self.vol_scale.configure(from_=0, to = 100, command=self.change_volume)
        self.vol_scale.set(50)
        self.addSongsToPlayListButton.configure(command=self.add_song)
        self.deleteSongsFromPlaylistButton.configure(command=self.remove_song)
        self.playButton.configure(command=self.play_song)
        self.stopButton.configure(command=self.stop_song)
        self.pauseButton.configure(command=self.pause_song)
        self.playList.configure(font="Vivaldi 12")
        self.playList.bind("<Double-1>", self.list_double_click)
        img = tk.PhotoImage(file="./icons/like.png")
        self.top.iconphoto(self.top,img)
        self.top.title("MOUZIKKA- Dance to the rythm of your heart!")
        self.top.protocol("WM_DELETE_WINDOW",self.closewindow)
        self.isPaused = False
        self.isPlaying = False
        self.previousButton.bind("<Button-1>", self.load_previous_song)
        self.Button9.configure(command=self.add_song_to_favourites)
        self.Button11.configure(command=self.load_songs_from_favourites)
        self.Button10.configure(command=self.remove_song_from_favourites)
        self.isThreadRunning=False

    def load_previous_song(self,e):
        try:
            if hasattr(self,"selected_song")==False:
                raise MyExceptions.NoSongSelectedError("Please select a song first")
            self.prev_song_index = self.selected_song[0] - 1
            if self.prev_song_index == -1:
                self.prev_song_index = self.playList.count() - 1
            self.playList.select_clear(0,tk.END)
            self.playList.selection_set(self.prev_song_index)
            self.play_song()
        except(MyExceptions.NoSongSelectedError) as ex1:
            messagebox.showerror("Error!", ex1)


    def previous_song(self):
        self.selected_song = self.playList.curselection()
        print(self.selected_song)

    def change_volume(self,x):
        volume_scale = float(x)
        volume_scale = volume_scale / 100
        self.my_player.set_volume(volume_scale)

    def add_song(self):
        song_name = self.my_player.add_song()
        if song_name is "":
            return
        self.playList.insert(tk.END, song_name)
        rcolor = lambda : random.randint(0,255)
        red = hex(rcolor())
        blue = hex(rcolor())
        green = hex(rcolor())
        red = red[2:]
        blue = blue[2:]
        green = green[2:]
        if len(red) == 1:
            red = "0"+red
        if len(blue) == 1:
            blue = "0"+blue
        if len(green) == 1:
            green = "0"+green
        mycolor = "#" + red + green + blue
        print(red,green,blue)
        print(mycolor)
        self.playList.configure(fg=mycolor)

    def show_song_details(self):
        self.song_length = self.my_player.get_song_length(self.song_name)

        '''if self.song_length <= 60:
            self.songTotalDuration.configure(text="0:"+self.song_length)
        elif self.song_length > 60:
            self.song_length = time.strftime("%M:%S", (self.song_length))
            print(self.song_length)
            self.songTotalDuration.configure(text=self.song_length)'''

        min,sec = divmod(self.song_length, 60)
        min = round(min)
        sec = round(sec)
        self.songTotalDuration.configure(text=str(min)+':'+str(sec))
        self.songTimePassed.configure(text="0:0")
        ext_index = self.song_name.rfind(".")
        song_name_str = self.song_name[0:ext_index]

        if len(self.song_name) > 14:
            song_name_str = song_name_str[:14] + "..."
        self.songName.configure(text=song_name_str)


    def stop_song(self):
        if self.isPlaying == True or self.isPaused == True:
            self.my_player.stop_song()
            self.isPlaying = False
            self.isPaused = False


    def play_song(self):
        self.selected_song = self.playList.curselection()
        try:
            if len(self.selected_song) == 0:
                raise MyExceptions.NoSongSelectedError("Please Select a song to play.")
            self.song_name = self.playList.get(self.selected_song[0])
            self.show_song_details()
            if (self.isThreadRunning == False):
                self.isThreadRunning = True
            else:
                self.my_player.stop_song()
                time.sleep(1)

            self.my_player.play_song()
            self.change_volume(self.vol_scale.get())
            self.setup_thread()
            self.isPlaying = True

        except (MyExceptions.NoSongSelectedError)as ex1:
            messagebox.showerror("Error!", ex1)

    def pause_song(self):
        if self.isPlaying == True:
            self.my_player.pause_song()
            self.isPaused = True
            self.isPlaying = False
        else:
            self.my_player.unpause_song()
            self.isPaused = False
            self.isPlaying = True

    def closewindow(self):
        str = messagebox.askyesno("Quitting?", "Are you sure you want to quit")
        print(str)
        if str == True:
            messagebox.showinfo("MOUZIKKA","Thank You!")
            self.my_player.close_player()
            sys.exit()
        else:
            return

    def list_double_click(self,e):
        self.play_song()

    def remove_song(self):
        self.selected_song = self.playList.curselection()
        try:
            if len(self.selected_song) == 0:
                raise MyExceptions.NoSongSelectedError("Please Select a song to remove.")
            self.song_name = self.playList.get(self.selected_song[0])
            self.playList.delete(self.selected_song[0])
            self.my_player.remove_song(self.song_name)
            
        except (MyExceptions.NoSongSelectedError)as ex1:
            messagebox.showerror("Error!", ex1)

    def add_song_to_favourites(self):
        selected_song = self.playList.curselection()
        try:
            if len(selected_song) == 0:
                raise MyExceptions.NoSongSelectedError("Please Select a song to favourites.")
            song_name = self.playList.get(selected_song[0])
            result = self.my_player.add_song_to_favourites(song_name)
            messagebox.showinfo("Success!", result)
        except (MyExceptions.NoSongSelectedError)as ex1:
            messagebox.showerror("Error!", ex1)
        except (DatabaseError) as ex2:
            messagebox.showerror("DB Error!","Song cannot be added")

    def load_songs_from_favourites(self):
        try:
            load_result = self.my_player.load_songs_from_favourites()
            result = load_result[0]
            if result.find("No songs present")!=-1:
                messagebox.showinfo("Favoutires Empty!","No songs present in your favourites")
                return
            song_dict = load_result[1]
            self.playList.delete(0,tk.END)
            for song_name in song_dict:
                self.playList.insert(tk.END,song_name)
            rcolor = lambda: random.randint(0,255)
            red = hex(rcolor())
            green = hex(rcolor())
            blue = hex(rcolor())
            mycolor = "#"+red[2:3]+green[2:3]+blue[2:3]
            self.playList.configure(fg=mycolor)
        except(DatabaseError) as ex1:
            messagebox.showerror("DB error!", "Sorry! songs cannot be loaded")

    def remove_song_from_favourites(self):
        selected_song = self.playList.curselection()
        try:
            if len(selected_song) == 0:
                raise MyExceptions.NoSongSelectedError("Please Select a song to remove.")
            song_name = self.playList.get(selected_song[0])
            result = self.my_player.remove_song_from_favourites(song_name)
            if result.find("Song not present") != -1:
                messagebox.showinfo("Favoutires Empty!", "No songs present in your favourites")
                return
            self.playList.delete(selected_song)
            messagebox.showinfo("Removed!", "Song Removed from your favourites")
        except (MyExceptions.NoSongSelectedError)as ex1:
            messagebox.showerror("Error!", ex1)
        except(DatabaseError) as ex1:
            messagebox.showerror("DB error!", "Sorry! songs cannot be loaded")

    def setup_thread(self):

        self.my_thread = threading.Thread(target=self.show_timer, args=(self.song_length,))
        self.my_thread.start()

    def show_timer(self, total_sec):
        curr_sec = 0
        prev_perc_incr = 0
        self.songProgress.stop()
        while curr_sec <= total_sec and mixer.music.get_busy():
            if (self.isPaused):
                continue

            min, sec = divmod(curr_sec, 60)
            min = round(min)
            sec = round(sec)
            self.songTimePassed.configure(text=str(min) + ":" + str(sec))
            curr_sec += 1
            percent_incr = curr_sec * 100 / total_sec
            # print(percent_incr)
            if int(percent_incr) - int(prev_perc_incr) >= 1:
                self.songProgress.step(percent_incr-prev_perc_incr)
                prev_perc_incr = percent_incr

            time.sleep(1)
        # print("curr_sec:",curr_sec,"total_sec:",total_sec)
        if abs(curr_sec - int(total_sec)) == 0 or abs(curr_sec - int(total_sec)) == 1:
            self.load_next_song()

    def load_next_song(self):
        try:
            if hasattr(self, "selected_song") == False:
                raise MyExceptions.NoSongSelectedError("Please select a song first")
            self.next_song_index = self.selected_song[0] + 1
            if self.next_song_index == self.playList.count():
                self.next_song_index = 0
            self.playList.select_clear(0, tk.END)
            self.playList.selection_set(self.next_song_index)
            self.play_song()
        except(MyExceptions.NoSongSelectedError) as ex1:
            messagebox.showerror("Error!", ex1)


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def count(self):
        return tk.Listbox.size(self)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





