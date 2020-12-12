import yaml
import logging

def open_yaml_file(full_path):
    """Opens YAML config file

    Args:
        full_path (str): full path to file

    Returns:
        dict: dictionary with configuration items
    """
    logging.debug('Opening file on path: %s' % full_path)
    try:
        with open(full_path, 'r') as fp:
            return yaml.load(fp, Loader=yaml.FullLoader)
    except OSError as e:
        logging.error("Error openning config file: %s" % e)
        exit(1)