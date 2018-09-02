from tkinter import *  # GUI module
from string import ascii_letters  # string variable containing the alphabet
from math import floor  # always-round-down function
from time import time  # function returns time in seconds since 1970;
# difference between two results will be used for time measurement
from sys import platform  # function that determines the OS application is being run on
from random import shuffle  # function that randomly changes the order of elements in a sequence
from os.path import exists  # function that checks if a file exists in a particular locale
if platform == 'win32':
    import winsound  # module for playing .wav sound files on Windows systems
# all of the above modules come with a standard installation of Python


# checks if a "button.txt" file exists in the same folder as the executable. If it does, attempts to pull content from
# it where one line becomes one item in a list.
try:
    with open("buttons.txt", encoding='utf-8', mode='r') as file:

        temp_content = file.readlines()
        content = []
        for x in temp_content:
            content.append(x.strip())  # strips lead/trail whitespace and newline characters if any are present (ex. \n)

        while len(content) < 24:  # adds placeholder items to list, if imported content has less than 24 items
            content.append(len(content) + 1)

# if "button.txt" file is not found, creates numbers 1 through 24 to use as placeholders
except FileNotFoundError:
    content = list(range(1, 25))

time_started = 0
time_cumulative = 0
button_names = list(ascii_letters[:24])  # once instanced, buttons will be named 'a' - 'x', except for the center button
shuffle(content)

root = Tk()  # initializes tkinter module (too broad topic to comment, sorry)
root.title('Standup bingo')  # names the display window (top bar)

# checks if a "logo.gif" file exists in the same folder as the executable. If it does, pulls it in and stores under the
# "logo" variable. Sets a flag, based on which instancing of center button might not occur (when no image is available).
try:
    logo = PhotoImage(file='logo.gif')
    logo_found = True
except TclError:
    logo_found = False


class LogoButton:
    """The "barebones" button for storing the logo."""
    def __init__(self, master):
        self.button = Button(master, image=logo, height=110, width=100, bg='red', relief=FLAT)


class BingoButton:
    """The full and "proper" game button."""
    def __init__(self, master):
        self.button = Button(master,
                             text=content.pop(),
                             height=7,
                             width=14,
                             wraplength=100,
                             justify=LEFT,
                             command=self.toggle,  # called whenever button is clicked
                             bg='white',
                             relief=RAISED)
        self.pressed = False  # boolean flag to store button state; initialized as False (not pressed)

    def toggle(self):
        r"""
        Toggle pressed / depressed state of a bingo button.

        Whenever a button is pressed, launch check_bingo() to check for bingos.
        """
        if not self.pressed:
            self.button.config(relief=SUNKEN, bg='red')
            self.pressed = True
            self.check_bingo()  # bingo is checked every time a button is activated (pressed)
        else:  # bingo is not checked when a button has been depressed
            self.button.config(relief=RAISED, bg='white')
            self.pressed = False

    @staticmethod
    def check_bingo():
        """
        Call the 'prepare_state' function to compile and load the current game state into the 'bingoes' variable.

        Play a sound if bingo is found and application is running on Windows.
        """
        bingoes = prepare_state()  # check the prepare_state docstring for more info
        for y in bingoes:  # this word is typo'd on purpose because I felt like it :)
            if all(y):  # checks if any lane consists entirely of "True" booleans for the "pressed" flag
                if platform == 'win32':
                    if exists('bingo.wav'):
                        winsound.PlaySound('bingo.wav', winsound.SND_ASYNC)
                    else:  # if "bingo.wav" is not present in .exe folder, attempts to play a built-in Windows sound
                        winsound.PlaySound('SystemHand', winsound.SND_ALIAS | winsound.SND_ASYNC)


# dictionary comprehension, in which buttons are instanced. Letters from the "button_names" list act as keys, and each
# key has an individual BingoButton instance assigned as its value. In this way it is possible to keep a reference
# (handle) for the instances to manipulate them at a later time.
butts = {x: BingoButton(root) for x in button_names}
# .grid geometry configurations should not be done in the same row as assignments because they 'return None'
butts['a'].button.grid(row=0, column=1, rowspan=3, pady=(10, 0))
butts['b'].button.grid(row=0, column=2, rowspan=3, pady=(10, 0))
butts['c'].button.grid(row=0, column=3, rowspan=3, pady=(10, 0))
butts['d'].button.grid(row=0, column=4, rowspan=3, pady=(10, 0))
butts['e'].button.grid(row=0, column=5, rowspan=3, pady=(10, 0))
butts['f'].button.grid(row=3, column=1, rowspan=3)
butts['g'].button.grid(row=3, column=2, rowspan=3)
butts['h'].button.grid(row=3, column=3, rowspan=3)
butts['i'].button.grid(row=3, column=4, rowspan=3)
butts['j'].button.grid(row=3, column=5, rowspan=3)
butts['k'].button.grid(row=6, column=1, rowspan=3)
butts['l'].button.grid(row=6, column=2, rowspan=3)
butts['m'].button.grid(row=6, column=4, rowspan=3)
butts['n'].button.grid(row=6, column=5, rowspan=3)
butts['o'].button.grid(row=9, column=1, rowspan=3)
butts['p'].button.grid(row=9, column=2, rowspan=3)
butts['q'].button.grid(row=9, column=3, rowspan=3)
butts['r'].button.grid(row=9, column=4, rowspan=3)
butts['s'].button.grid(row=9, column=5, rowspan=3)
butts['t'].button.grid(row=12, column=1, rowspan=3, pady=(0, 10))
butts['u'].button.grid(row=12, column=2, rowspan=3, pady=(0, 10))
butts['v'].button.grid(row=12, column=3, rowspan=3, pady=(0, 10))
butts['w'].button.grid(row=12, column=4, rowspan=3, pady=(0, 10))
butts['x'].button.grid(row=12, column=5, rowspan=3, pady=(0, 10))
# center button is instanced only if a .gif file was found earlier; otherwise a blank space is left in the middle
if logo_found:
    fff = LogoButton(root)
    fff.button.grid(row=6, column=3)


def prepare_state():
    r"""
    Return the current state of the bingo board based on 'pressed' flags of buttons.

    This function is called only by the BingoButton method 'check_bingo' and only when a button is pressed.
    Compiles and loads the current game state into the 'bingoes' variable.
    This "game state" takes the form of a list, where individual items are nested sub-lists.
    Every sub-list corresponds to a particular "lane" (win possibility) - 5 horizontals, 5 verticals, 2 diagonals.
    Sub-list items are boolean values pulled from the 'pressed' flag of BingoButton instances.
    This list is returned to 'check_bingo', which then checks if any sub-list contains only 'True' values.
    Note that the center field is not included in the checks at all - lanes containing it have only 4 items.
    """
    bingoes = list()
    # horizontals
    bingoes.append([butts['a'].pressed, butts['b'].pressed, butts['c'].pressed, butts['d'].pressed, butts['e'].pressed])
    bingoes.append([butts['f'].pressed, butts['g'].pressed, butts['h'].pressed, butts['i'].pressed, butts['j'].pressed])
    bingoes.append([butts['k'].pressed, butts['l'].pressed, butts['m'].pressed, butts['n'].pressed])
    bingoes.append([butts['o'].pressed, butts['p'].pressed, butts['q'].pressed, butts['r'].pressed, butts['s'].pressed])
    bingoes.append([butts['t'].pressed, butts['u'].pressed, butts['v'].pressed, butts['w'].pressed, butts['x'].pressed])
    # verticals
    bingoes.append([butts['a'].pressed, butts['f'].pressed, butts['k'].pressed, butts['o'].pressed, butts['t'].pressed])
    bingoes.append([butts['b'].pressed, butts['g'].pressed, butts['l'].pressed, butts['p'].pressed, butts['u'].pressed])
    bingoes.append([butts['c'].pressed, butts['h'].pressed, butts['q'].pressed, butts['v'].pressed])
    bingoes.append([butts['d'].pressed, butts['i'].pressed, butts['m'].pressed, butts['r'].pressed, butts['w'].pressed])
    bingoes.append([butts['e'].pressed, butts['j'].pressed, butts['n'].pressed, butts['s'].pressed, butts['x'].pressed])
    # diagonals
    bingoes.append([butts['a'].pressed, butts['g'].pressed, butts['r'].pressed, butts['x'].pressed])
    bingoes.append([butts['e'].pressed, butts['i'].pressed, butts['p'].pressed, butts['t'].pressed])
    return bingoes


def start_time():
    """Note the moment from which to count the passage of time. Display "IN PROGRESS" message."""
    global time_started
    if not time_started:
        time_started = floor(time())
    start.config(state=DISABLED, relief=SUNKEN)
    pause.config(state=ACTIVE, relief=RAISED)
    time_display.config(text='W TRAKCIE!!!', fg='red')


def pause_time():
    """
    Pause counting time and display current cumulative time elapsed.

    Invokes the 'choose_seconds' function to prettify the data before displaying.
    """
    global time_cumulative, time_started
    time_cumulative += floor(time()) - time_started
    time_started = 0
    start.config(state=ACTIVE, relief=RAISED)
    pause.config(state=DISABLED, relief=SUNKEN)
    choose_seconds(time_cumulative)


def reset_time():
    """Reset elapsed time."""
    global time_started, time_cumulative
    time_started = 0
    time_cumulative = 0
    start.config(state=ACTIVE, relief=RAISED)
    pause.config(state=DISABLED, relief=SUNKEN)
    time_display.config(text='wyzerowano', fg='red')
    minutes_display.config(text='')


# this function is obfuscate-y on purpose because it was an irresistibly amusing idea at the time
def choose_seconds(amount, recursive=False):
    """
    Return amount of time elapsed and the noun appropriate for that amount - or just the noun.

    The first time this function is called, it determines what to display in the "seconds" line of the time display.
    It then passes the amount of seconds to the 'convert_seconds' function to check if a minute conversion is required.
    If so, 'convert_seconds' will call back with the 'recursive=True' argument to get only the noun to use with minutes.
    """
    form = ''
    if amount == 1:
        if not recursive:
            time_display.config(text='1 sekundę.', fg='black')
        else:
            form = 'sekundę'
    elif amount not in (12, 13, 14) and str(amount)[-1] in ('2', '3', '4'):
        if not recursive:
            time_display.config(text=f'{amount} sekundy.', fg='black')
        else:
            form = 'sekundy'
    else:
        if not recursive:
            time_display.config(text=f'{amount} sekund.', fg='black')
        else:
            form = 'sekund'
    if not recursive:
        convert_seconds(amount)
    else:
        return form


def convert_seconds(amount):
    """Display elapsed time in minutes, if that time is 60 seconds or more.

    Calls 'choose_seconds' with argument to pick an appropriate noun."""
    # dwadzieścia dwie, dwadzieścia cztery, osiemdziesiąt trzy minuty
    if amount > 299 and str(amount//60)[-1] in ('2', '3', '4') and amount//60 not in (12, 13, 14):
        minutes_display.config(text=f'(czyli {amount//60} minuty i {amount%60} {choose_seconds(amount%60, True)})')
    elif amount > 299:  # sześć, osiem, dwanaście, czternaście, sześćdziesiąt minut
        minutes_display.config(text=f'(czyli {amount//60} minut i {amount%60} {choose_seconds(amount%60, True)})')
    elif amount > 119:  # dwie, trzy, cztery minuty
        minutes_display.config(text=f'(czyli {amount//60} minuty i {amount%60} {choose_seconds(amount%60, True)})')
    elif amount > 59:  # jedną minutę
        minutes_display.config(text=f'(czyli {amount//60} minutę i {amount%60} {choose_seconds(amount%60, True)})')


# this is the notepad area to the left of the bingo board
notepad = Text(root, height=35, width=20)
notepad.insert(END, 'ten \nobszar \nmożna \nwykorzystać \ndo \nrobienia \nnotatek')
notepad.grid(row=0, column=0, rowspan=15, padx=10)

# these are the various UI elements to the right of the bingo board
intro = Label(root, text='Dzisiejszy standup trwał:')
intro.grid(row=0, column=6, columnspan=3)
time_display = Label(root)
time_display.grid(row=1, column=6, columnspan=3)
minutes_display = Label(root)
minutes_display.grid(row=2, column=6, columnspan=3)
start = Button(root, text='>', padx=10, command=start_time)
start.grid(row=3, column=6, columnspan=3, sticky='w', padx=(20, 0))
pause = Button(root, text='||', padx=10, state=DISABLED, relief=SUNKEN, command=pause_time)
pause.grid(row=3, column=6, columnspan=3)
reset = Button(root, text='0', padx=10, command=reset_time)
reset.grid(row=3, column=6, columnspan=3, sticky='e', padx=(0, 25))

bucketlist = Label(root, text='O czym dzisiaj powiedzieć:')
bucketlist.grid(row=9, column=6, columnspan=3)
# these are the entry fields in the bottom-right corner of the application
topic1, topic2, topic3, topic4, topic5 = Entry(root), Entry(root), Entry(root), Entry(root), Entry(root)
topic1.grid(row=10, column=6, columnspan=2, padx=(10, 0))
topic2.grid(row=11, column=6, columnspan=2, padx=(10, 0))
topic3.grid(row=12, column=6, columnspan=2, padx=(10, 0))
topic4.grid(row=13, column=6, columnspan=2, padx=(10, 0))
topic5.grid(row=14, column=6, columnspan=2, padx=(10, 0))


class ToggleBox:
    """Checkbox that controls colour scheme of itself and bound Entry field, depending on its state."""
    def __init__(self, row, column, bind):
        self.var = IntVar()  # tkinter-specific boolean variable that stores the checkbox state (ticked/not ticked)
        self.box = Checkbutton(root, variable=self.var, command=self.check)
        self.box.grid(row=row, column=column)
        self.bind = bind  # assigns each checkbox to an entry field to its left

    def check(self):  # triggered every time checkbox is clicked
        if self.var.get():  # retrieves boolean state from self.var and sets red background if '1' (checked)...
            self.box.config(selectcolor='red', fg='white')
            self.bind.config(bg='red', fg='white', insertbackground='white')
        else:  # ... sets white background otherwise (unchecked)
            self.box.config(selectcolor='white')
            self.bind.config(bg='white', fg='black', insertbackground='black')


box1 = ToggleBox(10, 8, topic1)
box2 = ToggleBox(11, 8, topic2)
box3 = ToggleBox(12, 8, topic3)
box4 = ToggleBox(13, 8, topic4)
box5 = ToggleBox(14, 8, topic5)


root.mainloop()  # tkinter-required main loop
