import configparser
import sys

from datetime import datetime, timedelta
from time import strftime
from tkinter import *


def close(event):
    sys.exit()


def update_current_time():
    string = strftime('%I:%M:%S %p')
    lbl_current_time.config(text=string)


def update_next_time():
    now = datetime.now()
    service_datetimes = [
        (now + timedelta((12 - now.weekday()) % 7)).replace(hour=18, minute=0, second=0, microsecond=0),
        (now + timedelta((13 - now.weekday()) % 7)).replace(hour=8, minute=15, second=0, microsecond=0),
        (now + timedelta((13 - now.weekday()) % 7)).replace(hour=10, minute=0, second=0, microsecond=0),
        (now + timedelta((13 - now.weekday()) % 7)).replace(hour=11, minute=45, second=0, microsecond=0)]
    # Set to smallest, non-negative timedelta
    td = min([x - now for x in service_datetimes if (x - now).total_seconds() >= 0])
    # Adjust to sync countdown and clock time
    td = td + timedelta(seconds=1)
    if td <= timedelta(minutes=5):
        lbl_next_time.config(foreground='yellow')
    else:
        lbl_next_time.config(foreground='green')
    days, remainder = divmod(td.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    cvs_days_num.itemconfigure(text_id_days, text='{:02}'.format(int(days)))
    cvs_hours_num.itemconfigure(text_id_hours, text='{:02}'.format(int(hours)))
    cvs_minutes_num.itemconfigure(text_id_minutes, text='{:02}'.format(int(minutes)))
    cvs_seconds_num.itemconfigure(text_id_seconds, text='{:02}'.format(int(seconds)))
    return


def update_times():
    update_current_time()
    update_next_time()
    lbl_current_time.after(1000, update_times)


def update_date():
    string = strftime('%a %b %d %Y').upper()
    lbl_date.config(text=string)
    lbl_date.after(1000, update_date)
    return


def update_utility():
    lbl_utility.config(text='love God. love people. make disciples.')
    lbl_utility.after(1000, update_utility)


if __name__ == "__main__":
    # Read Config
    config = configparser.ConfigParser()
    config.read('vcr-clock.ini')
    font_size_middle = int(config['Settings']['FontSize'])

    # Derived Variables
    font_size_other = int(font_size_middle / 4)

    # Create root window
    root = Tk()
    root.configure(background='black', cursor='none')
    # It is desired to go fullscreen from the start
    root.attributes('-fullscreen', True)
    # However, if fullscreen fails for some reason, 5 seconds later force fullscreen
    root.after(5000, lambda : root.attributes('-fullscreen', True))
    root.bind('<Escape>', close)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=4)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create upper section
    frame = Frame(root, background='black')
    frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
    frame_upper = Frame(frame, background='black')
    frame_upper.pack(side=TOP)
    # Create next time text
    lbl_next_time = Label(frame_upper, text='Next service in: ', font=('Trebuchet MS', font_size_other), background='black', foreground='green')
    lbl_next_time.grid(row=0, column=0, sticky='n')
    # Create next time days
    frame_days = Frame(frame_upper)
    frame_days.configure(background='black')
    cvs_days_num = Canvas(frame_days, background='black', highlightthickness=0)
    text_id_days = cvs_days_num.create_text(0, 5, text='12', fill='green', font=('Trebuchet MS', font_size_other), anchor='nw')
    bbox = cvs_days_num.bbox(text_id_days)
    cvs_days_num.configure(width=bbox[2], height=bbox[3] - 10)
    lbl_days_text = Label(frame_days, text='DAYS',
                          font=('Trebuchet MS', int(font_size_other * 0.3)),
                          background='black',
                          foreground='green')
    lbl_days_colon = Label(frame_upper, text=':',
                           font=('Trebuchet MS', font_size_other),
                           background='black',
                           foreground='green')
    frame_days.grid(row=0, column=1, sticky='nsew')
    cvs_days_num.pack(anchor='n')
    lbl_days_text.pack(anchor='s')
    lbl_days_colon.grid(row=0, column=2, sticky='n')
    # Create next time hours
    frame_hours = Frame(frame_upper)
    frame_hours.configure(background='black')
    cvs_hours_num = Canvas(frame_hours, background='black', highlightthickness=0)
    text_id_hours = cvs_hours_num.create_text(0, 5, text='34', fill='green', font=('Trebuchet MS', font_size_other), anchor='nw')
    bbox = cvs_hours_num.bbox(text_id_hours)
    cvs_hours_num.configure(width=bbox[2], height=bbox[3] - 10)
    lbl_hours_text = Label(frame_hours, text='HOURS',
                           font=('Trebuchet MS', int(font_size_other * 0.3)),
                           background='black',
                           foreground='green')
    lbl_hours_colon = Label(frame_upper, text=':',
                            font=('Trebuchet MS', font_size_other),
                            background='black',
                            foreground='green')
    frame_hours.grid(row=0, column=3, sticky='nsew')
    cvs_hours_num.pack(anchor='n')
    lbl_hours_text.pack(anchor='s')
    lbl_hours_colon.grid(row=0, column=4, sticky='n')
    # Create next time minutes
    frame_minutes = Frame(frame_upper)
    frame_minutes.configure(background='black')
    cvs_minutes_num = Canvas(frame_minutes, background='black', highlightthickness=0)
    text_id_minutes = cvs_minutes_num.create_text(0, 5, text='56', fill='green', font=('Trebuchet MS', font_size_other), anchor='nw')
    bbox = cvs_minutes_num.bbox(text_id_minutes)
    cvs_minutes_num.configure(width=bbox[2], height=bbox[3] - 10)
    lbl_minutes_text = Label(frame_minutes, text='MINUTES',
                             font=('Trebuchet MS', int(font_size_other * 0.3)),
                             background='black',
                             foreground='green')
    lbl_minutes_colon = Label(frame_upper, text=':',
                              font=('Trebuchet MS', font_size_other),
                              background='black',
                              foreground='green')
    frame_minutes.grid(row=0, column=5, sticky='nsew')
    cvs_minutes_num.pack(anchor='n')
    lbl_minutes_text.pack(anchor='s')
    lbl_minutes_colon.grid(row=0, column=6, sticky='n')
    # Create next time seconds
    frame_seconds = Frame(frame_upper)
    frame_seconds.configure(background='black')
    cvs_seconds_num = Canvas(frame_seconds, background='black', highlightthickness=0)
    text_id_seconds = cvs_seconds_num.create_text(0, 5, text='78', fill='green', font=('Trebuchet MS', font_size_other), anchor='nw')
    bbox = cvs_seconds_num.bbox(text_id_seconds)
    cvs_seconds_num.configure(width=bbox[2], height=bbox[3] - 10)
    lbl_seconds_text = Label(frame_seconds, text='SECONDS',
                             font=('Trebuchet MS', int(font_size_other * 0.3)),
                             background='black',
                             foreground='green')
    frame_seconds.grid(row=0, column=7, sticky='nsew')
    cvs_seconds_num.pack(anchor='n')
    lbl_seconds_text.pack(anchor='s')

    # Create middle section
    frame = Frame(root, background='black', highlightbackground='red', highlightthickness=2)
    frame.grid(row=1, column=0, padx=5, pady=5, ipadx=2, ipady=2, sticky='nsew')
    lbl_current_time = Label(frame, text='12:00:00 AM', font=('Trebuchet MS', font_size_middle), background='black', foreground='red')
    lbl_current_time.pack(side=TOP, expand=True)
    lbl_date = Label(frame, text='FRI FEB 28 2025', font=('Trebuchet MS', int(font_size_middle / 3) * 2), background='black', foreground='red')
    lbl_date.pack(side=BOTTOM, expand=True)

    # Create lower section
    frame = Frame(root, background='black')
    frame.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
    lbl_utility = Label(frame, text='LOWER', font=('Trebuchet MS', font_size_other), background='black', foreground='purple')
    lbl_utility.pack(side=BOTTOM)

    # Call GUI update functions
    update_times()
    update_date()
    update_utility()

    # Move to GUI main loop
    mainloop()
