# Airflow project using MLflow.

## Подготовка для работы с проектом.

1. **Установите необходимые зависимости** через команду: 
 - `poetry install`, необходимо чтобы вы были в одной лиректории с `poetry.lock` and `pyproject.toml`.

2. **Активируйте виртуальное окружение** poetry через команду `poetry shell`

3. **Запустите mlflow ui** через `poetry run mlflow ui` и оставляйте ее включенной для последующего запуска Airflow.

4. **Запустите движок docker**. В моем случае это Docker Desktop, и перейдите в ту же директорию где `docker-compose.yaml` чтобы построить docker образы, необходимые для работы с airflow, тк у airflow линуксовая архитектура, а мне (нам) нужно запустить ее на Windows. Далее постройте и запустите
- `docker-compose build`
- `docker-compose up`

5. **Откройте веб интерфейс Airflow по ** `http://localhost:8080` тк мы указывали в docker-compose port 8080:8080

6. **Инициализируем БД** и создаем пользователя:

    У себя я сделал `airflow db init` до начала запуска всего, но в данном случае инициализация бд выполняется вот так (надеюсь):
    ```
    docker-compose exec webserver airflow db init
    ```
    Далее создаем пользователя, в данном случае таким образом:
    ```
    docker-compose exec webserver airflow users create --username admin --firstname Admin --lastname Admin --role Admin --email admin@example.com --password admin
    ```
7. Далее переключить в airflow ui, turn on DAG `train_catboost_model`, и запустить вручную.

- **PS. Для запустка airflow необходимо было чтобы Docker Engine и MLflow ui были запущены**

---
## Проект по классификации (multi-classification) успеваемости студентов
[Ccылка на датасет](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset?select=Student_performance_data+_.csv)


## некие записи во время процесса работы над проектом:

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



