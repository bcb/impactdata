from ptvalerts import ptv, slack


if __name__ == '__main__':
    users = (
        ptv.User('@barry', 'Belgrave', 1),
        ptv.User('@harry', 'Hurstbridge', 2),
        ptv.User('@wally', 'Werribee', 3),
        ptv.User('@freddy', 'Frankston', 4),
    )
    disruptions = ptv.get_disruptions()
    slack.send(users, disruptions)
