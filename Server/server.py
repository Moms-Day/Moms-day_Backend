import os

from app import create_app

from config.production import ProductionConfig

if __name__ == '__main__':
    app = create_app(ProductionConfig)

    if 'SECRET_KEY' not in os.environ:
        print('[WARNING] SECRET_KEY is not exist')

    app.run(**app.config['RUN_SETTING'])
