"""Comms with the Public Transport Victoria API."""
import requests

from .settings import API_KEY, PTV_BASE_URL


def get_disruptions():
    """Get current disruptions"""
    return requests.get(f'{PTV_BASE_URL}/v3/disruptions')
