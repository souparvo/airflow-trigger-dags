#
# Use:  
#   python trigger_dag_run.py [config_file_path]
#

import sys
import subprocess
from datetime import datetime, timedelta
import logging
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

config = open_yaml_file(CONFIG_FILE)

AIRFLOW_HOME = config['airflow_home']
AIRFLOW_BIN = config['airflow_bin']

DAG_ID = config['dag_id']
INPUT_DATE = config['input_date']
INCREMENT = int(config['increment'])
QTY = int(config['quantity'])

# @TODO - add multiple runs (use array on YAML file and iterate)
for item in range(QTY):
    # create de date
    trigger_date = (datetime.strptime(INPUT_DATE, "%Y-%m-%dT%H:%M:%S") + timedelta(seconds=(INCREMENT * item))).strftime("%Y-%m-%dT%H:%M:%S")
    logger.info("Here is the command %s" % trigger_date)
    run_id = "script_created_%s" % trigger_date
    logger.info("Creating run id: %s" % run_id)
    # Create command to trigger dag
    cmd = "AIRFLOW_HOME={0} {1} trigger_dag -r {2} -e {3} {4}".format(AIRFLOW_HOME, AIRFLOW_BIN, run_id, trigger_date, DAG_ID)
    logger.debug("Lauching command: %s" % cmd)
    subprocess.check_output(cmd, shell=True)