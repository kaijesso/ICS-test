"""Make a class to sort songs"""
class Music(object):
  def __init__(self, songTitle, artist, album, genre):
    self.songTitle = songTitle
    self.artist = artist
    self.album = album
    self.genre = genre
  def printInformation(self):
    print (self.songTitle, "is sung by", self.artist, "on the album titled", self.album, ". It falls under the", self.genre, "genre.")

first = Music("First", "Cold War Kids", "Hold My Home", "alternaive")
first.printInformation()
print()
blue = Music("Blue Ain't Your Colour", "Keith Urban", "Ripcord", "country")
blue.printInformation()
print()
relapse = Music("Relapse", "Carrie Underwood", "Storyteller", "country")
relapse.printInformation()
