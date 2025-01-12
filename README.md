1. I installed MLFlow and Airflow as prerequisites to virtual env.:
- `pip install mlflow`
- `pip install apache-airflow`

2. I created poetry project using my exising `mlops` virtual environment:
- `poetry new project`

3. Then I defined my dependencies in `pyproject.toml`:
- `poetry lock` and `poetry install` etc.

4. `airflow db init` for airflow database initialization

5. `airflow users create --username khushbakhtx --firstname Khushbakht --lastname Shoymardonov --role Admin --email khushbakht.dev@gmail.com --password admin` : creating user administrator for entering to airflow web interface.

6. `docker-compose build` -> `docker-compose up`

7. `localhost:8080` to set up dags...



