import os


def get_env_variable(var_name):
    """Get the environment variable"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ValueError(error_msg)


PTV_BASE_URL = 'https://timetableapi.ptv.vic.gov.au'
PTV_KEY = get_env_variable('PTV_KEY')
SLACK_TOKEN = get_env_variable('SLACK_TOKEN')
PEOPLE = (
    ptv.Person('Barry', 'Belgrave', 1),
    ptv.Person('Harry', 'Hurstbridge', 2),
    ptv.Person('Wally', 'Werribee', 3),
    ptv.Person('Freddy', 'Frankston', 4),
)
