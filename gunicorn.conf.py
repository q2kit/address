wsgi_app = "project.wsgi:application"
loglevel = "debug"
workers = 2
bind = "0.0.0.0:8023"
reload = True
accesslog = errorlog = "/var/log/gunicorn/address.q2k.dev.log"
capture_output = True
#pidfile = "/var/run/gunicorn/address.q2k.dev.pid"
daemon = True
