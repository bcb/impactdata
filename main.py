import sys

from impactdata.utils import get_disruptions, alert


if __name__ == '__main__':
    disruptions = get_disruptions()
    alerted = alert(disruptions)
    print(alerted, file=sys.stderr)
