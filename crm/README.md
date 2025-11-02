# CRM Project Setup

## Requirements
- Install Redis and the necessary dependencies:
  - Install Redis: [Redis Installation Guide](https://redis.io/download)
  - Install dependencies: `pip install -r requirements.txt`

## Setup
1. Run migrations: `python manage.py migrate`
2. Start Redis: `redis-server`
3. Start Celery worker: `celery -A crm worker -l info`
4. Start Celery Beat: `celery -A crm beat -l info`
5. Verify the logs in `/tmp/crm_report_log.txt` for generated CRM reports.
