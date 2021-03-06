from datetime import timedelta
import os


class Config:
    SERVICE_NAME = "Mom's_day"
    SERVICE_NAME_UPPER = SERVICE_NAME.upper()
    DOMAIN = None
    PUBLIC_HOST = "52.78.5.142"

    RUN_SETTING = {
        'threaded': True
    }

    IMAGE_PATH = '../static'

    SECRET_KEY = os.getenv('SECRET_KEY', '0la2kd03jfk1kk3fj3ivn3002m2me421')

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_HEADER_TYPE = 'JWT'

    MONGODB_SETTINGS = {
        'host': None,
        'port': None,
        'username': None,
        'password': os.getenv('MONGO_PW_{}'.format(SERVICE_NAME_UPPER)),
        'db': SERVICE_NAME
    }

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': 'CareWorker App + Daughter App'
        },
        'basePath': '/ '
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'Some Tag',
                'description': 'Some API'
            },

            # CareWorker ----------
            {
                'name': '[CareWorker] 계정',
                'description': '요양보호사 계정 관련 API'
            },
            {
                'name': '[CareWorker] 연결',
                'description': '자녀와의 연결 관련 API'
            },
            {
                'name': '[CareWorker] 폼 작성',
                'description': '노인의 하루를 담은 폼을 작성하는 API'
            },
            # ---------------------

            # Daughter ------------
            {
                'name': '[Daughter] 계정',
                'description': '자녀 계정 관련 API'
            },
            {
                'name': '[Daughter] 순위',
                'description': '자녀 앱에서 볼 수 있는 요양 보호사-시설 순위 API(랭킹, 상세정보, 평가)'
            },
            {
                'name': '[Daughter] 연결',
                'description': '요양보호사와의 연결 관련 API'
            },
            {
                'name': '[Daughter] 폼',
                'description': '오늘 노인의 하루정보에 관한 API'
            }
            # ---------------------
        ]
    }
