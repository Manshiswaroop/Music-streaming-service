class MusicStreamingService:
    def _init_(self):
        self.songs = []

    def add_song(self, song_title):
        self.songs.append(song_title)

    def list_songs(self):
        for i, song in enumerate(self.songs, start=1):
            print(f"{i}. {song}")

    def play_song(self, song_number):
        if 1 <= song_number <= len(self.songs):
            print(f"Playing: {self.songs[song_number - 1]}")
        else:
            print("Invalid song number")

def main():
    music_service = MusicStreamingService()

    while True:
        print("\nMenu:")
        print("1. Add Song")
        print("2. List Songs")
        print("3. Play Song")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            song_title = input("Enter the song title: ")
            music_service.add_song(song_title)
        elif choice == "2":
            music_service.list_songs()
        elif choice == "3":
            song_numbet= int(input(" Pls input the song number"))
        else :
           print("Quit app")