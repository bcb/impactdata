"""
Communicate with the Public Transport Victoria API.

PTV Timetable API documentation is here:
https://www.ptv.vic.gov.au/about-ptv/ptv-data-and-reports/digital-products/ptv-timetable-api/
"""
from collections import namedtuple
from urllib.parse import urljoin

import requests

from . import settings


# User type, use this to store data about each user
User = namedtuple('User', ('slack_name', 'route_name', 'route_id'))


def get_disruptions():
    """
    Get all metro train disruptions.

    This function sends a GET requests to the PTV API to retrieve the metro
    train disruptions. Endpoint is described here:
    http://timetableapi.ptv.vic.gov.au/swagger/ui/index#!/Disruptions/Disruptions_GetAllDisruptions

    Returns:
        List of disruptions. See the API response at the above url.
    """
    url = urljoin(settings.PTV_BASE_URL, '/v3/disruptions')
    response = requests.get(url)
    try:
        return response.json()['disruptions']['metro_train']
    except KeyError as exc:
        raise ValueError('Could not retrieve disruptions') from exc


def filter_disruptions(disruptions, route_id):
    """
    Filter disruptions by route.

    Args:
        disruptions: List of PTV disruptions.
        route_id: PTV route.
    Returns:
        The same list filtered down to only include the specified route.
    """
    filtered_disruptions = [
        d for d in disruptions for r in d['routes'] if r['route_id'] == route_id]
    return filtered_disruptions


def get_descriptions(disruptions):
    """
    Get the descriptions from a list of disruptions.

    Args:
        disruptions: List of disruptions returned by `get_disruptions`.
    Returns:
        The descriptions of each disruption, in a comma-separated string.
    """
    descriptions = ", ".join([d['description'] for d in disruptions])
    return descriptions
