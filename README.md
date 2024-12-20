Плохая практика написания Dockerfile:
- Использование не оптимальный базовый образ. (В основном Dockerfile заменил на slim образ)
- Не использутеся `.dockerignore`, что замедляет процесс сборки, а также может привести к утечке данных. Наличие `.dockerignore` может уменьшить количество поводов для признания недействительным кэша при сборке похожих образов. Например, если при повторной сборке образа меняются служебные файлы проекта, из-за чего данные, хранящиеся в кэше, необоснованно признаются недействительными. (В основной Dockerfile добавил .dockerignore файл)
- Копируется вся папка проекта. При изменении кода будут заново устанавливаться все зависимости, т.к. их нет в кэше. (В основном Dockerfile сначала копируется файл requirements.txt, затем ставятся все зависимости, а потом копируются оставшиеся файлы проекта)

Когда не стоит использовать контейнеры:
- Случай, когда важна скорость и управление ресурсами - докер может тормозить
- Когда нужно прямое взаимодействие с железом - CPU, GPU
- Приложения с большим количеством зависимостей. Приложения, требующие установки большого количества библиотек, могут привести к слишком тяжелым и сложным в управлении образам.

Плохие практики использования контейнеров:
- Хранение данных в контейнере
- Создание слишком больших образов

# SmartToDo

Это простое приложение для управления списком задач (TODO List) на основе FastAPI. Приложение позволяет создавать, просматривать, обновлять и удалять задачи. В будущем планируется добавить поддержку базы данных, простой UI и сервис AI-ассистента.

## Оглавление

- [Текущая функциональность](#текущая-функциональность)
- [Установка и запуск](#установка-и-запуск)
- [Предварительные требования](#предварительные-требования)
- [Сборка и запуск с помощью Docker](#сборка-и-запуск-с-помощью-docker)

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
> 1. **Перейдите в папку:** `cd SmartToDo`
> 2. **Соберите Docker образ:** `docker build -t todo_app .`
> 3. **Запустите контейнер:** `docker run -d -p 8000:8000 -v $(pwd)/logs:/code/logs todo_app`. Приложение будет доступно по адресу http://localhost:8000.

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
