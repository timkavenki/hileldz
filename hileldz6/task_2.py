'''У додатку є json файл. Написати програму, яка прочитає його та порахує загальну тривалість всіх треків в альбомі.

  Базовий кейс - поверне кількість секунд.

  * Дод. ускладнення повернути у вигляді рядка години:хвилини:секунди, прик. 0:41:39'''

import json
import datetime

def calculate_total_duration(album_file):
    with open(album_file) as file:
        data = json.load(file)
        tracks = data['tracks']

        total_seconds = 0
        for track in tracks:
            duration = track['duration']
            track_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(duration.split(':'))))
            total_seconds += track_seconds

        return total_seconds

def format_duration(total_seconds):
    duration = datetime.timedelta(seconds=total_seconds)
    return str(duration)

album_file = 'acdc.json'

total_seconds = calculate_total_duration(album_file)
print("Загальна тривалість треків (у секундах):", total_seconds)

formatted_duration = format_duration(total_seconds)
print("Загальна тривалість треків (у форматі годин:хвилини:секунди):", formatted_duration)