"""Alert four public transport users when their route is disrupted."""
from slackclient import SlackClient

import ptv, settings


USERS = (
    ptv.User('Barry', 'Belgrave', 1),
    ptv.User('Harry', 'Hurstbridge', 2),
    ptv.User('Wally', 'Werribee', 3),
    ptv.User('Freddy', 'Frankston', 4),
)


if __name__ == '__main__':
    # Get all disruptions
    disruptions = ptv.get_disruptions()
    # Alert the four users
    slack_client = SlackClient(settings.SLACK_TOKEN)
    for user in USERS:
        # Get the list of disruptions for their route
        route_disruptions = ptv.filter_disruptions(disruptions, user.route_id)
        if route_disruptions:
            # Get the disruptions into one string (saves multiple api calls)
            descriptions = ptv.get_descriptions(disruptions)
            # Send the alert
            message = f'{user.route_name}: {descriptions}'
            slack_client.api_call(
                'chat.postMessage', channel=user.name, text=message)
