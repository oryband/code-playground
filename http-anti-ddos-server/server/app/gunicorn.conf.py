import multiprocessing

accesslog = '-'

bind = "127.0.0.1:8000"
worker_class='aiohttp.GunicornWebWorker'
workers = multiprocessing.cpu_count() * 2 + 1
