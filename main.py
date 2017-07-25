"""Alert four public transport users when their route is disrupted."""
from slackclient import SlackClient

from impactdata import ptv, settings


if __name__ == '__main__':
    # Get all disruptions
    disruptions = ptv.get_disruptions()
    # Alert the four users
    slack_client = SlackClient(settings.SLACK_TOKEN)
    for person in settings.PEOPLE:
        # Get the list of disruptions for their route
        route_disruptions = ptv.filter_disruptions(disruptions, person.route_id)
        if route_disruptions:
            # Get the disruptions into one string (saves multiple api calls)
            descriptions = ptv.get_descriptions(disruptions)
            # Send the alert
            message = f'{person.route_name}: {descriptions}'
            sc.api_call('chat.postMessage', channel=person.name, text=message)
