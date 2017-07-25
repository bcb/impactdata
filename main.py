import sys


if __name__ == '__main__':
    disruptions = get_disruptions()
    alerted = alert(disruptions)
    print(alerted, file=sys.stderr)
