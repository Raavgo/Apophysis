from typing import Tuple

import requests
from PIL import Image
from io import BytesIO

def get_next_image(dims:Tuple[int, int]) -> Image:
    req = requests.get(f"https://picsum.photos/{dims[0]}/{dims[1]}")
    return Image.open(BytesIO(req.content))



def get_next_malware_batch() -> Image:
    from datetime import datetime, timedelta

    def next_date(date_str: str) -> str:
        if date_str:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        else:
            date_obj = datetime.today()

        next_day = date_obj + timedelta(days=1)
        return next_day.strftime("%Y-%m-%d")

    with open("malware_batch.txt", "a+") as file:

        for line in file:
            pass
        if line:
            timestamp = line.split("/")[-1].replace(".zip", "")
        else:
            timestamp = ""
        timestamp = next_date(timestamp)

    url = f"https://datalake.abuse.ch/malware-bazaar/daily/{timestamp}.zip"
    print(url)

if __name__ == '__main__':
    get_next_malware_batch()
