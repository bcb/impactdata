import os


def get_env_variable(var_name):
    """Get the environment variable"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ValueError(error_msg)


PTV_ID = get_env_variable('PTV_ID')
PTV_KEY = get_env_variable('PTV_KEY')
PTV_BASE_URL = 'https://timetableapi.ptv.vic.gov.au'
PTV_DISRUPTIONS = f'/v3/disruptions?devid={PTV_ID}'
SLACK_TOKEN = get_env_variable('SLACK_TOKEN')
