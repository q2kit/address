wsgi_app = "project.wsgi:application"
loglevel = "debug"
workers = 9
bind = "127.0.0.1:8023"
reload = True
accesslog = errorlog = "/var/log/gunicorn/address.vnsvs.net.log"
capture_output = True
#pidfile = "/var/run/gunicorn/address.vnsvs.net.pid"
daemon = True
