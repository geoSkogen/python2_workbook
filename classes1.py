class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print(line)
songs = [
["with the gods of Magog swarming around",
"the Pied Piper takes his children underground"],
["and as the song and dance begins",
"the children play at home", "with needles",
"needles and pins"]
]

supper = ["with the gods of Magog swarming around",
"the Pied Piper takes his children underground"]

broadway = ["and as the song and dance begins",
"the children play at home", "with needles",
"needles and pins"]

supper_song = Song(songs[0])

supper_song.sing()

broadway_song = Song(songs[1])

broadway_song.sing()
