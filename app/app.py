import os
from bottle import *

@route('/')
def index(section='home'):
    return template('index')

@error(404)
def error404(error):
    return 'This is not the page you are looking for.'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 1337))
    run(host='0.0.0.0', port=port, debug=True, reloader=True)
