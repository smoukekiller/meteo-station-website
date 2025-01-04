from datetime import datetime, timedelta


def get_data() -> tuple[float, float]:
    ct = datetime.now() - timedelta(seconds=30)
    filename = ct.isoformat()[:10]
    file = open(f'{filename}.txt', 'r')
    text = file.read().split(sep='\n')[-2].split(sep=';')
    temperature = float(text[1])
    humidity = float(text[2])
    return temperature, humidity
