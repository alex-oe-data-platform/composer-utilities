# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

# Optimized DAG adhering to Airflow best practices:
# 1. Use `schedule` parameter instead of deprecated `schedule_interval`
# 2. Use static start_date (datetime.datetime with UTC timezone) instead of days_ago()
# 3. Use EmptyOperator instead of removed DummyOperator
# 4. Remove top-level print statements / side effects
# 5. Define default_args with retries and retry_delay
default_args = {
    "retries": 2,
    "retry_delay": datetime.timedelta(minutes=5),
}

with DAG(
    dag_id="airflow2_example_schedule_interval",
    schedule="@daily",
    start_date=datetime.datetime(2024, 1, 1, tzinfo=datetime.timezone.utc),
    catchup=False,
    default_args=default_args,
    tags=["airflow2", "compatibility_test"],
) as dag:
    start = EmptyOperator(task_id="start_task")
    end = EmptyOperator(task_id="end_task")

    start >> end
