# Impulse-DevOps-Telecom-2026

Репозиторий содержит решение тестового задания по автоматизации с использованием Python, Docker и Ansible. Реализованы все требования, указанные в задании.

## Task 1


- `task1/script.py` - Python-скрипт, выполняющий HTTP-запросы к сервису проверки HTTP-статусов.

## Task 2


- `task2/Dockerfile` - Dockerfile для сборки образа на базе `ubuntu:22.04`.
- `task2/script.py` - Python-скрипт, который копируется в контейнер и запускается при старте.

## Task 3


Есть основной плейбук `playbooks/main.yml`, который запускает две роли:
- `docker_install` - установка и настройка Docker на целевом хосте;
- `run_script` - сборка Docker-образа, запуск контейнера и получение логов.


`hosts` - это inventory-файл.

`ansible.cfg` - содержит настройки Ansible.
### Запуск playbook

Из каталога `task3`:

```bash
ANSIBLE_CONFIG=./ansible.cfg ansible-playbook playbooks/main.yml -k -K
```

