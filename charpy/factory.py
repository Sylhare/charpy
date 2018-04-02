# -*- coding: utf-8 -*-
"""
Use export FLASK_APP="charpy.factory:create_app()"


"""
from flask import Flask
from werkzeug.utils import find_modules, import_string
from charpy.blueprints.simple_page import simple_page


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug

    # add your modules
    app.register_blueprint(simple_page)
    #register_blueprints(app)

    return app


def register_blueprints(app):
    """Automagically register all blueprint named bp in packages

    Check the argument 'bp' in all the modules in the folder inserted in findmodules
    then register all blueprints in the app
    """
    for name in find_modules('charpy.blueprints', recursive=True):
        mod = import_string(name)

        if hasattr(mod, 'bp'):
           # print(mod.bp)
            app.register_blueprint(mod.bp)
    return None


if __name__ == "__main__":  # pragma: no cover
    app = create_app(debug=True)
    print(app.blueprints)
    app.run()
