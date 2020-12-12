#
# Use:  
#   python trigger_dag_run.py [config_file]
#

import sys
import subprocess
from datetime import datetime, timedelta
import logging
import yaml
from utils import open_yaml_file

#### LOGGING

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)

#### END LOGGING

# @TODO - Use argparser and verify inputs
CONFIG_FILE = sys.argv[1]
# CONFIG_FILE = 'config.yml'

config = open_yaml_file(CONFIG_FILE)

AIRFLOW_HOME = config['airflow_home']
AIRFLOW_BIN = config['airflow_bin']

for item in config['dags']:
    # iterate exec_dates
    dag_id = item['dag_id']
    for exec_date in item['exec_dates']:
        # create de date
        logger.info("Exec date: %s" % exec_date)
        run_id = "%s__%s" % (item['run_id_suffix'], exec_date)
        logger.info("Creating run id: %s" % run_id)
        # Create command to trigger dag
        cmd = "AIRFLOW_HOME={0} {1} trigger_dag -r {2} -e {3} {4}".format(AIRFLOW_HOME, AIRFLOW_BIN, run_id, exec_date, dag_id)
        logger.info("Lauching command: %s" % cmd)
        subprocess.check_output(cmd, shell=True)
