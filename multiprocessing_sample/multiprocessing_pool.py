from multiprocessing import Pool
from datetime import datetime


def main(x):
    now = datetime.utcnow()
    print(now.strftime('%Y/%m/%d %H:%M:%S.%f')[:-3])


if __name__ == "__main__":
    with Pool(7) as p:
        p.map(main, [1, 2, 3, 4, 5, 6, 7])
