# airflow-trigger-dags

Triggers DAG runs using Airflow CLI and subprocess.

## trigger_runs

Triggers multiple DAG runs of the same `dag_id` with array of exection dates from config file.

### Examples

Shell command to execute script:

```shell
python python trigger_runs.py /path/to/config_file.yml
```

Example config file:

```yaml
airflow_home: /path/to/airflow # same as $AIRFLOW_HOME
airflow_bin: /path/to/airflow_bin # if airflow installed on virtualenv on /path/to/airflow_venv, then should be /path/to/airflow_venv/bin/airflow

dags:
  - dag_id: dag_id
    run_id_suffix: recover
    exec_dates:
      - '2020-11-11T16:05:00'
      - '2020-11-12T18:05:00'
  - dag_id: other_dag_id
    run_id_suffix: new
    exec_dates:
      - '2020-12-12T16:05:00'
```

This config file creates the following DAG runs with dagrun_id:

```
# for dag_id
'recover__2020-11-11T16:05:00'
'recover__2020-11-12T18:05:00'
# for other_dag_id
'new__2020-12-11T16:05:00'
```

## trigger_dag_runs

Triggers multiple DAG runs of the same `dag_id` starting from one `input_date` to `input_date` + `increment` seconds * `quantity`.

### Examples

Shell command to execute script:

```shell
python python trigger_dag_run.py /path/to/config_file.yml
```

Example config file:

```yaml
airflow_home: /path/to/airflow # same as $AIRFLOW_HOME
airflow_bin: /path/to/airflow_bin # if airflow installed on virtualenv on /path/to/airflow_venv, then should be /path/to/airflow_venv/bin/airflow

dag_id: dag_id
input_date: '2020-12-11T16:05:00'
increment: 3600 # in seconds
quantity: 4 # increments of run
```

This config file creates the following DAG runs with dagrun_id:

```
'script_created_2020-12-11T16:05:00'
'script_created_2020-12-11T17:05:00'
'script_created_2020-12-11T18:05:00'
'script_created_2020-12-11T19:05:00'
```