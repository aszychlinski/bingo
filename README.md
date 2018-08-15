# bingo
COMPLETE - humorous tool to liven up your "daily standup" meetings! Inspired by real life (...sadly).

## Context
I started learning Python this year. So far it is super fun. 
However, writing things that return to the console window (cmd) got less exciting as time went on.
Luckily, Python comes with the tkinter GUI module, which allows me to "visualize" my ideas. **Interest restored!**

## Introduction
This is a bingo "game" to be used during daily standup meetings. Just listen to the conversation unfold and tap those buttons.
* The area to the left of the bingo board can be used for taking notes. 
* The top-right area is a timer to measure meeting duration.
  * ">" button starts counting time
  * "||" pauses counting and displays accumulated time in seconds (and minutes, if applicable)
  * "0" button resets accumulated time
 * The bottom-right area is for writing down topics you want to raise at the meeting (and ticking them off after doing so).

## Customising the application
* you can replace the texts that appear on buttons by editing the *buttons.txt* file
  * highly recommended! (every project has its own problems and you know them :wink:)
  * one button per line
  * if there are less than 24 lines, file is missing or empty, placeholders will be added
  * if there are more than 24 lines, a random selection of them will be used on every start
* you can replace the *bingo.wav* sound
  * if it is missing entirely, a generic system sound will attempt to play
  * **sound only works on Windows**
* you can replace the *logo.gif* file to change the graphic at the middle of the board
  * if file is missing entirely, blank space appears in the middle (app still works)
  * file *has* to be .gif
* files will be detected when they are in the same folder as the .py (... or .exe)
  
## Resolution

The application was developed and tested entirely on the 1920 x 1080 resolution. On other resolutions, all bets are off. It'll probably be fine though. :laughing:
  
## Compiling to .exe

`pyinstaller` works well with this project. If you want an .exe of this, try:

`pyinstaller -F -y -w --clean standup_bingo.py`

## Feedback?

What I would find particularly valuable is feedback about the quality of *comments* which I have included in my code.
I am still really new to this so I don't have a good feel for it. Are there too many code comments? Too few? 
Are they too detailed / not detailed enough? I did have a particular audience in mind when writing those comments - the kind of person who knows programming but has never seen Python before. That is why I do things like explaining what `random.shuffle` is.

If you have any other feedback, comments or bug reports, feel free to share them.
As of right now I consider this project complete, but you never know.
That being said...

## Disclaimer

1. Read the license (standard MIT).
2. The sample texts provided in the *buttons.txt* file are not meant to describe or resemble any particular project or persons. Any perceived similarity is unintentional.
   * they *are* meant to resemble the grueling process of software creation in general :grinning:
