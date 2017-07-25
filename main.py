import sys

from impactdata import ptv, slack


if __name__ == '__main__':
    disruptions = ptv.get_disruptions()
    alerted = slack.alert(disruptions)
    print(alerted, file=sys.stderr)
