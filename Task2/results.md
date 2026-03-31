# Результаты тестирования производительности

**Дата:** 2026-04-01  
**Окружение:** macOS, Python 3.11, nginx 1.29.7, gunicorn 21.2.0  
**Аппаратура:** MacBook Pro

## Тест 1: Статические файлы (nginx + public)
**Endpoint:** `http://localhost:8080/public/test.txt`

| Connections | Threads | Duration | Requests/sec | Latency (avg) | Errors |
|-------------|---------|----------|--------------|---------------|--------|
| 10 | 2 | 10s | 47,914 | 0.2ms | 0 |
| 50 | 4 | 30s | 43,290 | 1.1ms | 0 |
| 100 | 4 | 30s | 35,379 | 2.5ms | read errors |
| 200 | 4 | 30s | 24,915 | 3.5ms | read errors |

**Вывод:** nginx эффективно отдает статику, выдерживая до ~43K RPS без ошибок.

---

## Тест 2: WSGI через nginx (nginx + gunicorn)
**Endpoint:** `http://localhost:8080/gunicorn/`

| Connections | Threads | Duration | Requests/sec | Latency (avg) | Errors |
|-------------|---------|----------|--------------|---------------|--------|
| 10 | 2 | 10s | 74 | 133ms | 0 |
| 50 | 4 | 30s | 77 | 398ms | read errors |
| 100 | 4 | 30s | 77 | 399ms | read errors |
| 200 | 4 | 30s | 77 | 400ms | read errors |

**Вывод:** Производительность ограничена gunicorn (~77 RPS), увеличение соединений не повышает RPS, только увеличивает latency.

---

## Тест 3: Прямое обращение к gunicorn
**Endpoint:** `http://127.0.0.1:8000/`

| Connections | Threads | Duration | Requests/sec | Latency (avg) | Errors |
|-------------|---------|----------|--------------|---------------|--------|
| 10 | 2 | 10s | 74 | 133ms | 0 |
| 50 | 4 | 30s | 74 | 639ms | 0 |
| 100 | 4 | 30s | 74 | 1.32s | 0 |
| 200 | 4 | 30s | 74 | 1.72s | read errors |

**Вывод:** Прямой gunicorn показывает схожую производительность, но с более высокой латентностью при высокой нагрузке.

---

## Сравнительный анализ

| Тип нагрузки | Max RPS | Latency (10 conn) | Latency (200 conn) | Узкое место |
|--------------|---------|-------------------|--------------------|-------------|
| Статика (nginx) | 47,914 | 0.2ms | 3.5ms | Сеть/CPU |
| WSGI через nginx | 77 | 133ms | 400ms | time.sleep(0.05) |
| Прямой gunicorn | 74 | 133ms | 1.7s | time.sleep(0.05) |

---
