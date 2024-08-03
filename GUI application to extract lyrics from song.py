class LyricsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lyrics Extractor")
        self.root.geometry("500x400")
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Song Title").grid(row=0, column=0, padx=10, pady=10)
        self.song_entry = tk.Entry(self.root, width=50)
        self.song_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Artist").grid(row=1, column=0, padx=10, pady=10)
        self.artist_entry = tk.Entry(self.root, width=50)
        self.artist_entry.grid(row=1, column=1, padx=10, pady=10)
        
        fetch_button = tk.Button(self.root, text="Fetch Lyrics", command=self.fetch_lyrics)
        fetch_button.grid(row=2, columnspan=2, pady=10)
        
        self.lyrics_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=60, height=15)
        self.lyrics_text.grid(row=3, columnspan=2, padx=10, pady=10)
    
    def fetch_lyrics(self):
        song_title = self.song_entry.get()
        artist = self.artist_entry.get()
        
        if not song_title or not artist:
            messagebox.showwarning("Input Error", "Please provide both song title and artist name.")
            return
        
        try:
            song = genius.search_song(song_title, artist)
            if song:
                self.lyrics_text.delete('1.0', tk.END)
                self.lyrics_text.insert(tk.INSERT, song.lyrics)
            else:
                messagebox.showinfo("No Lyrics Found", "Could not find lyrics for the specified song.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    root = tk.Tk()
    app = LyricsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
