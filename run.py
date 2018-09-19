import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from app import create_app

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)


if __name__ == '__main__':
    app.run(debug=True)