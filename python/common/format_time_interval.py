import time, sys
from datetime import datetime

def get_time_interval(start_time, end_time):
    start_time = datetime.fromtimestamp(start_time)
    end_time = datetime.fromtimestamp(end_time)
    interval = (end_time - start_time).seconds
    format_interval = get_format_interval(interval)
    return format_interval

def get_format_interval(interval):
    if interval < 60:
        format_interval = "{}s".format(str(interval))
    elif 60 <= interval < 60*60:
        format_interval = "{}min {}s".format(
            str(interval/60), str(interval%60))
    elif 60*60 <= interval <= 60*60*24:
        format_interval = "{}h {}min {}s".format(
            str(interval/(60*60)),
            str(interval%(60*60)/60),
            str(interval%(60*60)%60)
        )
    return format_interval

# Need two parameters: start_time and end_time
if __name__ == "__main__":
    start_time, end_time = sys.argv[1], sys.argv[2]
    interval = get_time_interval(start_time, end_time)
