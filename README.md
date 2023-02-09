# API для получения погоды и прогноза погоды


# Технологии:
    Python
    FastAPI

# Запуск и работа с проектом

1. Клонировать репозиторий к себе на локальную машину:

```git clone git@github.com/kiselev-pavel-dev/test_weather```

2. Перейти в директорию с проектом:

```cd test_weather```

3. Создать и активировать виртуальное окружение:

```python -m venv venv```
```source venv/scripts/activate```

4. Установить зависимости:

```pip install -r requirements.txt```

5. Создать и наполнить файл .env:
```
API_KEY= Ваш API ключ к сервису https://m3o.com/weather/api

```

6. Запустить проект:

```uvicorn src.main:app --reload```

Документация по API доступна по ссылке http://127.0.0.1:8000/docs


Автор:

Павел Киселев
