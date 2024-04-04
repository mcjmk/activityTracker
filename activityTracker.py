import os
import pygetwindow as gw
import time
import csv
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog

categories = ["Work", "Learning", "Hobby", "Entertainment", "Social Media", "Daily chores"]


def ask_for_category(activity_details):
    ROOT = tk.Tk()
    ROOT.withdraw()
    category = simpledialog.askstring(title="Activity categorization",
                                      prompt=f"Select category for: {activity_details}",
                                      initialvalue=categories[0])
    return category


def track_active_window():
    current_window = None
    start_time = datetime.now()
    csv_filename = 'activity_log.csv'

    file_exists = os.path.isfile(csv_filename)
    if not file_exists or os.stat(csv_filename).st_size == 0:
        with open(csv_filename, 'w', newline='', encoding="utf-8") as csvfile:
            headers = ['Activity Name', 'Start Time', 'End Time', 'Duration', 'Category']
            writer = csv.writer(csvfile)
            writer.writerow(headers)

    while True:
        new_window = gw.getActiveWindow()
        if new_window != current_window:
            if current_window is not None:
                end_time = datetime.now()
                duration = end_time - start_time
                current_window_title_quoted = f'"{current_window.title}"'
                category = ""
                if new_window.title:
                    category = ask_for_category(current_window_title_quoted)
                print(f"You spend {duration} on the activity {current_window.title}!")

                with open(csv_filename, 'a', newline='', encoding="utf-8") as csvfile:
                    log_writer = csv.writer(csvfile)
                    log_writer.writerow([current_window.title, start_time.strftime('%Y-%m-%d %H:%M:%S'),
                                         end_time.strftime('%Y-%m-%d %H:%M:%S'), str(duration), category])

                    print(f"Activity {current_window.title} saved")
                    print(f"{[current_window_title_quoted, start_time.strftime('%Y-%m-%d %H:%M:%S'),
                              str(duration)], category}")

            current_window = new_window
            start_time = datetime.now()

            time.sleep(0.5)


if __name__ == '__main__':
    track_active_window()
