from datetime import datetime, timedelta
from config import DATA_PATH

def get_data() -> tuple[float, float]:
    last_update_file = open(f"{DATA_PATH}last_updated.txt")
    text = last_update_file.read().split(sep="\n")

    timestamp = int(text[0])
    ct = datetime.fromtimestamp(timestamp)
    filename = ct.isoformat()[:10]

    file = open(f'{DATA_PATH}{filename}.txt', 'r')
    text = file.read().split(sep='\n')[-2].split(sep=';')
    temperature = float(text[1])
    humidity = float(text[2])
    return (temperature, humidity)
