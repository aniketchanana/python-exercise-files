playlist = {
    "title" : "patagonia bus",
    "author":"aniket",
    "songs" :[
        {
            "title":"song1",
            "artist":['blue'],
            "duration":2.5
        },
        {
            "title":"song2",
            "artist":['kitty','djcat'],
            "duration":3.7
        },
        {
            "title":"song3",
            "artist":['aniket'],
            "duration":2
        }
    ]
}

sum = 0
for song in playlist["songs"] :
    sum += song["duration"]

print(sum)