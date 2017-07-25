import os


def get_env_variable(var_name):
    """Get the environment variable"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ValueError(error_msg)


API_KEY = get_env_variable('API_KEY')
