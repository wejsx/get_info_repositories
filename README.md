# GitHub Repository Analyzer

Этот проект представляет собой инструмент для анализа репозиториев на GitHub и их коллабораторов (collaborators). Он использует API GitHub для получения информации о репозиториях пользователя и их участниках.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/wejsx/get_info_repositories
    ```

2. Поместите ваш Github-Токен в  `depends.py` :
    *Не забудьте заменить `your_token` на свой токен.*

## Использование

1. Запустите приложение:

    ```
    docker-compose up --build
    ```

2. Откройте браузер и перейдите по адресу [http://127.0.0.1:80](http://127.0.0.1:80).

## Примеры вывода

Пример вывода информации о репозитории:

```json
[
  {
    "name": "algorithm-python",
    "create": "2023-07-29T12:40:27Z",
    "count_collaborators": 1,
    "collaborators": [
      {
        "login": "wejsx",
        "create": "2022-12-05T21:35:49Z"
      }
    ],
    "stargazers": 0
  }
]
