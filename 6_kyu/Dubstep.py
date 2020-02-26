"""
Dubstep
https://www.codewars.com/kata/551dc350bf4e526099000ae5
"""
def song_decoder(song):
    song = song.upper()
    f = []
    s = song.split("WUB")
    for i in s:
        if i.isalnum():
            f.append(i)
    return " ".join(f)
