import sys
import requests

from settings import API_KEY



def get_disruptions():
    pass


def alert(disruptions):
    pass


if __name__ == '__main__':
    disruptions = get_disruptions()
    alerted = alert(disruptions)
    print(alerted, file=sys.stderr)
