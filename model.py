import cx_Oracle
class Model:
    def __init__(self):
        self.song_dict={}
        self.db_status=True
        self.conn= None
        self.cur= None
        try:
            self.conn= cx_Oracle.connect("mouzikka/music@127.0.0.1/xe")
            self.cur=self.conn.cursor()

        except cx_Oracle.DatabaseError:
            self.db_status=False

    def get_db_status(self):
        return self.db_status


    def close_db_connection(self):
            if self.cur is not None:
                self.cur.close()
                print("Connection and cur closed succesfully")
            if self.conn is not None:
                self.conn.close()
                print("Connection and cur closed succesfully")

    def add_song(self, song_name, song_path):
        self.song_dict[song_name]=song_path
        print("song added:", song_path)

    def get_song_path(self, song_name):
        return self.song_dict[song_name]

    def remove_song(self, song_name):
        self.song_dict.pop(song_name)

    def search_song_in_favourite(self, song_name):
        self.cur.execute("select song_name from my_favourites where song_name=:1",(song_name,))
        song_tuple = self.cur.fetchone()
        if song_tuple is None:
            return False
        else:
            return True

    def add_song_to_fav(self,song_name,song_path):
        self.search_song = self.search_song_in_favourite(song_name)
        if self.search_song == True:
            return "Song already present in your favourites"
        else:
            self.cur.execute("select max(song_id) from my_favourites")
            last_song_id = self.cur.fetchone()[0]
            next_song_id = 1
            if last_song_id is not None:
                next_song_id = last_song_id + 1
            self.cur.execute("insert into my_favourites values(:1,:2,:3)",(next_song_id,song_name,song_path))
            self.conn.commit()
            return "Song added to your favourites"


    def load_songs_from_favourite(self):
        self.cur.execute("select song_name,song_path from my_favourites")
        songs_present = False
        for x,y in self.cur:
            self.song_dict[x] = y
            songs_present = True
        if songs_present == True:
            return "List populated from favourites"
        else:
            return "No songs present in your favourites"

    def remove_song_from_favourite(self,song_name):
        self.cur.execute("delete from my_favourites where song_name=:1",(song_name,))
        if self.cur.rowcount == 0:
            return "Song not present"
        else:
            self.conn.commit()
            self.song_dict.pop(song_name)
            return "Song removed successfully"

