# Good website for format codes for datetime.strptime()
# https://www.programiz.com/python-programming/datetime/strptime
from datetime import datetime, timedelta
import time
from datetime import datetime

# Chapter 9.9- Working with Timestamps
print("\nChapter 9.9- Working with Timestamps" + "-" * 20)
print(time.time())


def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end-start
print(duration)

# Chapter 9.10- Working with DateTimes
print("\nChapter 9.10- Working with DateTimes" + "-" * 20)
dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y%m"))

print(dt2 > dt1)

birth = input(
    "What is your birthday? Enter as Month/Day/Year like 02/28/1908:"
)
birth_date = datetime.strptime(birth, "%m/%d/%Y")
print(birth_date)
date_now = datetime.now()
duration_seconds = date_now-birth_date
print(f"You have lived a happy life of {duration_seconds}.")

# Chapter 9.11- Working with Time Deltas
print("\nChapter 9.11- Working with Time Deltas" + "-" * 20)
dt1 = datetime(2018, 1, 1)+timedelta(days=1, seconds=1000)
print(dt1)
dt2 = datetime.now()

duration = dt2-dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total_seconds", duration.total_seconds())
