from config import DATA_PATH
from datetime import datetime, timedelta

def compile_data() -> tuple[list, list, list]:
    last_update_file = open(f"{DATA_PATH}last_updated.txt")
    text = last_update_file.read().split(sep="\n")

    end_timestamp = int(text[0])
    start_timestamp = end_timestamp - 86400 #amount of seconds in 1 day

    end = datetime.fromtimestamp(end_timestamp)
    start = datetime.fromtimestamp(start_timestamp)

    start_filename = datetime.isoformat(start)[:10]
    end_filename = datetime.isoformat(end)[:10]

    start_file = open(f"{DATA_PATH}{start_filename}.txt")
    end_file = open(f"{DATA_PATH}{end_filename}.txt")
    
    start_text = start_file.read()
    while True:
        start_index = start_text.find(str(start_timestamp))
        if (start_index != -1):
            break
        start_timestamp += 1
    start_text = start_text[start_index:]
    start_array = start_text.split(sep="\n")[:-1]

    end_text = end_file.read()
    end_array = end_text.split(sep="\n")[:-1]

    last_array = start_array + end_array

    temp_array = []
    humid_array = []
    labels = []
    counter = 0
    for i in last_array:
        if counter % 40 == 0:
            help_array = i.split(sep=';')
            timestamp = int(help_array[0])
            date = datetime.fromtimestamp(timestamp) + timedelta(hours=2)
            label = date.isoformat(sep=" ")[5:19]
            labels.append(label)


            temperature = float(help_array[1])
            humidity = float(help_array[2])
            temp_array.append(temperature)
            humid_array.append(humidity)
        counter += 1
    start_file.close()
    end_file.close()
    return (labels, temp_array, humid_array)

