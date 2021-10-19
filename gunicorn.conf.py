import multiprocessing

wsgi_app = "mask_detector:create_app()"
bind = "127.0.0.1:8001" # only on localhost. to expose, use 0.0.0.0
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = "access.log"
errolog = "error.log"