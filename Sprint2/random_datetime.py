import random
import datetime

def gen_timestamp(min_year, max_year):
    # gera um datetime no formato yyyy-mm-dd hh:mm:ss.000000
    year = random.randint(min_year, max_year)
    month = random.randint(11, 12)
    day = random.randint(1, 28)
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    date = datetime.datetime(
        year, month, day, hour, minute, second).isoformat(" ")
    return date

