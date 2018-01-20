class Catalog(object):

    def __init__(self, songs):
        self.songs = songs

    def start_song(self, index):
        asong = self.songs[index]
        for i in asong:
            print(asong[i])

    def store(self, name, lines):
        filename = "%s.txt" % name
        target = open(filename, 'w+')
        for i in lines:
            target.write("%s\n" % i)
        target.close()

    def read(self, name):
        filename = "%s.txt" % name
        text = open(filename, 'r')
        print(text.read())
        text.close()

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

#this is the main method--defines main variables, objects, etc.
def init_funcs():
    playlist = []
    catalog = Catalog(playlist)
    prompt = "> "

    def begin_entry():
    #these are nested methods; flow control begins below
        def enter_lines():
            lines = []
            print("enter title\n")
            lines.append(input(prompt))
            print("enter line by line\n")
            i = 1
            lines.append(input(prompt))
            while lines[i] != "end":
                i += 1
                lines.append(input(prompt))
                if lines[i] == "end":
                    print(lines)
                    next_song = Song(lines)
                    catalog.songs.append(lines)
                    catalog.store(lines[0], lines)
                    begin_entry()

        def search_by_title(thistitle, erase):
            titlefound = False
            count = -1;
            for i in catalog.songs:
                count += 1
                if i[0] == thistitle:
                    titlefound = True
                    if erase == "D":
                        i[0] = "erased
                        print("song deleted\n")
                        begin_entry()
                    catalog.read(thistitle)
                    #print(catalog.songs,"\n")
                    #catalog.start_song(count)
                    begin_entry()
            if titlefound == False:
                print("no matches found for '%s'\n" % thistitle)
                begin_entry()

        def get_title(toast):
            print("enter song title\n")
            searchtitle = input(prompt)
            search_by_title(searchtitle, toast)

        def make_selection(char):
            if char == "N":
                enter_lines()
            elif char == "V":
                get_title("V")
#                print(catalog.songs)
#                begin_entry()
            elif char == "D":
                get_title("D")
                begin_entry()
            else:
                print("whatup python?")
                begin_entry()

    #flow control begins here
        print ("N = new song || V = view song || D = delete song")
        selector =  input(prompt)
        if selector == "N" or selector == "V" or selector == "D":
            make_selection(selector)
        else:
            print("unrecognized character\n")
            begin_entry()
    begin_entry()
init_funcs()
