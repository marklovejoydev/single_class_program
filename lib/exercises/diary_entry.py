import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary input must have a title and content")
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        if wpm <= 0:
            raise Exception("wpm must be greater than 0")
        contents_length = len(self.contents.split())
        return math.ceil(contents_length /wpm)

    def reading_chunk(self, wpm, minutes):
        words_can_read = wpm * minutes
        words = self.contents.split()
        if self.read_so_far >= len(words):
            self.read_so_far = 0  # Reset to 0 if all content has been read
                
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_can_read
        chunk_words = words[chunk_start : chunk_end]
        self.read_so_far = min(chunk_end, len(words))  # Update read_so_far, ensuring it doesn't exceed content length
        return " ".join(chunk_words)