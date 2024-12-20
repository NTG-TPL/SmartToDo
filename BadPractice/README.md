Плохая практика написания Dockerfile (BadDockerfile):
- Использование не оптимальный базовый образ. заменили на slim

# SmartToDo

Это простое приложение для управления списком задач (TODO List) на основе FastAPI. Приложение позволяет создавать, просматривать, обновлять и удалять задачи. В будущем планируется добавить поддержку базы данных, простой UI и сервис AI-ассистента.

## Оглавление

- [Текущая функциональность](#текущая-функциональность)
- [Установка и запуск](#установка-и-запуск)
- [Предварительные требования](#предварительные-требования)
- [Сборка и запуск с помощью Docker](#сборка-и-запуск-с-помощью-docker)
- [API Endpoints](#api-endpoints)
- [Будущие улучшения](#будущие-улучшения)
- [Contributing](#contributing)
- [Лицензия](#лицензия)

## Текущая функциональность

- Создание новой задачи (TODO).
- Просмотр всех задач.
- Просмотр конкретной задачи по ID.
- Обновление задачи по ID.
- Удаление задачи по ID.

## Установка и запуск

### Предварительные требования
- Docker
- Python 3.11

> ### Сборка и запуск с помощью Docker
> 1. **Перейдите в папку:** `cd fastapi-todo-list`
> 2. **Соберите Docker образ:** `docker build -t todo-fastapi-app .`
> 3. **Запустите контейнер:** `docker run -d -p 8000:8000 my-fastapi-app`. Приложение будет доступно по адресу http://localhost:8000.

**Swagger:** http://localhost:8000/docs

### Будущие улучшения
В ближайшем будущем планируется добавить следующие улучшения:
- **База данных:**
Переход от встроенного хранилища данных к базе данных (PostgreSQL).
Сохранение задач в базе данных для обеспечения сохранности данных.

- **Простой UI:**
Добавление простого веб-интерфейса для управления задачами.

- **Сервис AI-ассистента:**
Добавление сервиса AI-ассистента, который будет следить за тем, чтобы все задачи были описаны по системам, выбранным пользователем (например, Smart).
Интеграция с AI-сервисами для анализа и улучшения описаний задач.