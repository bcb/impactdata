"""Alert four public transport users when their route is disrupted."""
from impactdata import ptv, slack


if __name__ == '__main__':
    # Get the current disruptions
    disruptions = ptv.get_disruptions()
    # Alert the four users
    PEOPLE = (
        ('Barry', 'Belgrave'),
        ('Harry', 'Hurstbridge'),
        ('Wally', 'Werribee'),
        ('Freddy', 'Frankston')
    ,)
    for name, route in PEOPLE:
        slack.alert(name, route, disruptions)
