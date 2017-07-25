"""Utility functions for accessing the PTV and Slack apis"""
import requests

from .settings import API_KEY, PTV_BASE_URL


def get_disruptions():
    """Get current disruptions from the PTV API"""
    return requests.get(f'{PTV_BASE_URL}/v3/disruptions')
