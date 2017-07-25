"""Alert public transport users when their route is disrupted."""
from slackclient import SlackClient

from . import ptv, settings


def send(disruptions, users):
    """
    Send disruption alerts to users.

    Args:
        disruptions: List of disruptions from the `ptv.get_disruptions`
            function.
        users: List of users to send the disruptions to.
    """
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
