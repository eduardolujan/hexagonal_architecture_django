# Hexagonal Architecture 


The hexagonal architecture, or ports and adapters architecture, is an architectural pattern used in 
software design. It aims at creating loosely coupled application components that can be easily connected 
to their software environment by means of ports and adapters. This makes components exchangeable at any 
level and facilitates test automation.

![Hexagonal Architecture](./docs/imgs/hexagonal_diagram1.png)

## Hexagonal Architecture Django

![Hexagonal Architecture Django](./docs/imgs/hexagonal_diagram2.png)


## Setup
Setup

###Local
Local setup
  

### Docker

```
docker-compose up -d
```

### Task List 
- [x] Django orm models
- [x] Django rest framework
- [x] Cors
- [x] Repository pattern
- [x] Repository Create, Get, Update, Delete, All, Search (Criteria/Specification pattern )
- [x] Entities 
- [x] Mapped orm entities 
- [x] Bundle context 
- [x] Abstract unit of work
- [ ] Domain Events 
- [ ] Domain bus events
- [ ] Domain event handlers
- [ ] Commands
- [ ] CQS
- [ ] CQRS pattern
- [ ] Command bus handlers
- [ ] Command handlers



### Env file content

```
DJANGO_READ_DOT_ENV_FILE=True


# PostgreSQL
# ------------------------------------------------------------------------------
POSTGRES_HOST=had_postgres
POSTGRES_PORT=5432
POSTGRES_DB=hexagonal_django
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DATA=~/Documents/Projects/docker/hexagonal_django/postgres
POSTGRES_BACKUPS=~/Documents/projects/docker/hexagonal_django/postgres_backups
POSTGRES_EXTERNAL_PORT=5432
POSTGRES_LOCALHOST=127.0.0.1


# Redis
# ------------------------------------------------------------------------------
REDIS_PORT=6379
REDIS_HOST=localhost
REDIS_DATABASE=0
REDIS_URL=redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DATABASE}
REDIS_DATA=~/Documents/projects/docker/hexagonal_django/redis


# Celery
CELERY_BROKER_URL=redis://localhost:6379/0

# Rabbitmq
RABBITMQ_HOST=had_rabbitmq
RABBITMQ_USER=rabbitmq
RABBITMQ_PASS=password
RABBITMQ_VHOST=app
RABBITMQ_MANAGEMENT_PORT=15672
RABBITMQ_PORT=5672
RABBITMQ_DIR=~/Documents/projects/docker/hexagonal_django/rabbitmq
```


