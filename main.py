from ptvalerts import ptv, slack


if __name__ == '__main__':
    disruptions = ptv.get_disruptions()
    users = (
        ptv.User('@barry', 'Belgrave', 1),
        ptv.User('@harry', 'Hurstbridge', 2),
        ptv.User('@wally', 'Werribee', 3),
        ptv.User('@freddy', 'Frankston', 4),
    )
    slack.send(disruptions, users)
