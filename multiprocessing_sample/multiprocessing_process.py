from multiprocessing import Process
from datetime import datetime


def main():
    now = datetime.utcnow()
    print(now.strftime('%Y/%m/%d %H:%M:%S.%f')[:-3])


if __name__ == "__main__":
    jobs = [
        Process(target=main, args=()),
        Process(target=main, args=()),
        Process(target=main, args=()),
        Process(target=main, args=()),
        Process(target=main, args=()),
        Process(target=main, args=()),
        Process(target=main, args=()),
    ]

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()
