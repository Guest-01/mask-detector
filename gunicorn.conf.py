import multiprocessing

wsgi_app = "mask_detector:create_app()"
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = "access.log"
errolog = "error.log"
timeout = 120