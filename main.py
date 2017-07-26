from ptvalerts import ptv, slack


if __name__ == '__main__':
    users = (
        ptv.User('@barry', 'Belgrave', 2),
        ptv.User('@harry', 'Hurstbridge', 8),
        ptv.User('@wally', 'Werribee', 16),
        ptv.User('@freddy', 'Frankston', 6),
    )
    disruptions = ptv.get_disruptions()
    slack.send(users, disruptions)
