from datetime import datetime, timedelta
from config import DATA_PATH

def get_data() -> tuple[float, float, int]:
    print(f"{DATA_PATH}last_updated.txt")
    last_update_file = open(f"{DATA_PATH}last_updated.txt")
    text = last_update_file.read().split(sep="\n")
    last_updated = int(text[0])

    timestamp = last_updated
    ct = datetime.fromtimestamp(timestamp)
    filename = ct.isoformat()[:10]

    date = datetime.fromtimestamp(timestamp) + timedelta(hours=2)
    label = date.isoformat(sep=" ")[5:19]

    file = open(f'{DATA_PATH}{filename}.txt', 'r')
    text = file.read().split(sep='\n')[-2].split(sep=';')
    temperature = float(text[1])
    humidity = float(text[2])
    return (temperature, humidity, label)
