"""Alert public transport users when their route is disrupted."""
from slackclient import SlackClient

import ptv, settings


def send(disruptions, users):
    # Get slack client
    slack_client = SlackClient(settings.SLACK_TOKEN)
    # Alert the users
    for user in users:
        # Get only the disruptions for the user's route
        route_disruptions = ptv.filter_disruptions(disruptions, user.route_id)
        if route_disruptions:
            # Get the disruptions into one string (saves multiple api calls)
            descriptions = ptv.get_descriptions(disruptions)
            # Send the alert
            message = f'{user.route_name} disruptions: {descriptions}'
            slack_client.api_call(
                'chat.postMessage', channel=user.slack_name, text=message)


if __name__ == '__main__':
    disruptions = ptv.get_disruptions()
    users = (
        ptv.User('Barry', '@barry', 'Belgrave', 1),
        ptv.User('Harry', '@harry', 'Hurstbridge', 2),
        ptv.User('Wally', '@wally', 'Werribee', 3),
        ptv.User('Freddy', '@freddy', 'Frankston', 4),
    )
    send(disruptions, users)
