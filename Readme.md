# music-organizer

## The Rationale

This is a personal project. 

I am using Google Play Music. 
I like creating playlist. 

This tool is very opiniated. 
It tells the number of songs per playlist. Along with Tags. 
Also. Find if a song already lived in one of your playlist.

## notes

- clean up always at the end. make it work first
- ai with google music api

## installation

- `pip install gmusicapi`
- `pip install tabulate`
- on mac only: `chmod 755 music`

## command

| command      | description                                  |
| ------------ | -------------------------------------------- |
| register     | register this pc                             |
| login        | login                                        |
| logout       | delete local credentials                     |
| count        | list all playlists with songs count and tags |
| find "query" | find query in all playlist                   |
