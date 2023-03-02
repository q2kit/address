wsgi_app = "project.wsgi:application"
loglevel = "debug"
workers = 9
bind = "127.0.0.1:8023"
reload = True
accesslog = errorlog = "/var/log/gunicorn/address.q2k.dev.log"
capture_output = True
pidfile = "/var/run/gunicorn/address.q2k.dev.pid"
daemon = True
