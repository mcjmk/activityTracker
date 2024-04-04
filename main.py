import os

import pygetwindow as gw
import time
import csv
from datetime import datetime


def track_active_window():
    current_window = None
    start_time = datetime.now()
    csv_filename = 'activity_log'

    file_exists = os.path.isfile(csv_filename)
    if not file_exists or os.stat(csv_filename).st_size == 0:
        with open(csv_filename, 'w', newline='', encoding="utf-8") as csvfile:
            headers = ['Activity Name', 'Start Time', 'End Time', 'Duration']
            writer = csv.writer(csvfile)
            writer.writerow(headers)

    while True:
        new_window = gw.getActiveWindow()
        if new_window != current_window:
            if current_window is not None:
                end_time = datetime.now()
                duration = end_time - start_time
                print(f"You spend {duration} on the activity {current_window.title}!")

                with open(csv_filename, 'a', newline='', encoding="utf-8") as csvfile:
                    log_writer = csv.writer(csvfile)
                    log_writer.writerow([current_window.title, start_time.strftime('%Y-%m-%d %H:%M:%S'),
                                         end_time.strftime('%Y-%m-%d %H:%M:%S'), str(duration)])
                    current_window_title_quoted = f'"{current_window.title}"'

                    print(f"Activity {current_window.title} saved")
                    print(f"{[current_window_title_quoted, start_time.strftime('%Y-%m-%d %H:%M:%S'), str(duration)]}")

            current_window = new_window
            start_time = datetime.now()

        time.sleep(0.5)


if __name__ == '__main__':
    track_active_window()
