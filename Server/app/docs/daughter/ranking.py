from app.docs import SAMPLE_FACILITY_CODE, SAMPLE_OBJECT_IDS

DAUGHTER_RANKING_FACILITY_GET = {
    'tags': ['[Daughter] 순위'],
    'description': '요양 시설 순위 조회(no token => Only ranking, have token => ranking & own facilities)',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': False
        }
    ],
    'responses': {
        '200': {
            'description': '순위 조회 성공',
            'examples': {
                'no token': {
                        'facilityRanking': [
                            {
                                'facilityCode': SAMPLE_FACILITY_CODE[0],
                                'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                                'name': '무슨무슨 요양병원',
                                'address': '어디어디 어디 어디어디 옆',
                                'overall': 4.5,
                                'medals': ['가성비 갑', '안전 점검 우수']
                            },
                            {
                                'facilityCode': SAMPLE_FACILITY_CODE[1],
                                'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                                'name': '어쩌구저쩌구 요양병원',
                                'address': '왼오왼오 옆옆 어디어디 어디',
                                'overall': 3,
                                'medals': []
                            },
                            {
                                'facilityCode': SAMPLE_FACILITY_CODE[2],
                                'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                                'name': '블라블라 노인 요양원',
                                'address': '바로 거기',
                                'overall': 2.5,
                                'medals': ['가성비 갑', '보호사 친절도 짱']
                            }
                        ]
                },
                'have token': {
                        'facilityRanking': [
                            {
                                'facilityCode': SAMPLE_FACILITY_CODE[0],
                                'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                                'name': '무슨무슨 요양병원',
                                'address': '어디어디 어디 어디어디 옆',
                                'overall': 4.5,
                                'medals': ['가성비 갑', '안전 점검 우수']
                            },
                            {
                                'facilityCode': SAMPLE_FACILITY_CODE[1],
                                'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                                'name': '어쩌구저쩌구 요양병원',
                                'address': '왼오왼오 옆옆 어디어디 어디',
                                'overall': 3,
                                'medals': []
                            },
                            {
                                'facilityCode': SAMPLE_FACILITY_CODE[2],
                                'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                                'name': '블라블라 노인 요양원',
                                'address': '바로 거기',
                                'overall': 2.5,
                                'medals': ['가성비 갑', '보호사 친절도 짱']
                            }
                        ],
                        'myFacilities': [
                            {
                                'facilityCode': SAMPLE_FACILITY_CODE[3],
                                'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                                'name': '여기 엄마 모신곳 병원',
                                'address': '우리집에서 차타고 20분 거리에 있는 이마트 옆',
                                'overall': 1.5,
                                'medals': []
                            }
                        ]
                }
            }
        }
    }
}


DAUGHTER_RANKING_CARE_WORKER_GET = {
    'tags': ['[Daughter] 순위'],
    'description': '요양 보호사 순위 조회',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': False
        }
    ],
    'responses': {
        '200': {
            'description': '순위 조회 성공',
            'examples': {
                'no token': {
                        'careWorkerRanking': [
                            {
                                'careWorkerId': SAMPLE_OBJECT_IDS[0],
                                'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                                'name': '이종현',
                                'workplace': '강남 요양병원',
                                'patientInCharge': 4,
                                'career': 8,
                                'overall': 4.5
                            },
                            {
                                'careWorkerId': SAMPLE_OBJECT_IDS[1],
                                'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                                'name': '정다은',
                                'workplace': '용산 노인의 집',
                                'patientInCharge': 6,
                                'career': 5,
                                'overall': 4.2
                            },
                            {
                                'careWorkerId': SAMPLE_OBJECT_IDS[2],
                                'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                                'name': '정경서',
                                'workplace': '구로 요양원',
                                'patientInCharge': 1,
                                'career': 2,
                                'overall': 3.8
                            }
                        ]
                },
                'have token': {
                    'careWorkerRanking': [
                        {
                            'careWorkerId': SAMPLE_OBJECT_IDS[0],
                            'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                            'name': '이종현',
                            'workplace': '강남 요양병원',
                            'patientInCharge': 4,
                            'career': 8,
                            'overall': 4.5
                        },
                        {
                            'careWorkerId': SAMPLE_OBJECT_IDS[1],
                            'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                            'name': '정다은',
                            'workplace': '용산 노인의 집',
                            'patientInCharge': 6,
                            'career': 5,
                            'overall': 4.2
                        },
                        {
                            'careWorkerId': SAMPLE_OBJECT_IDS[2],
                            'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                            'name': '정경서',
                            'workplace': '구로 요양원',
                            'patientInCharge': 1,
                            'career': 2,
                            'overall': 3.8
                        }
                    ],
                    'myCareWorkers': [
                        {
                            'careWorkerId': SAMPLE_OBJECT_IDS[2],
                            'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                            'name': '정경서',
                            'workplace': '구로 요양원',
                            'patientInCharge': 1,
                            'career': 2,
                            'overall': 3.8
                        },
                        {
                            'careWorkerId': SAMPLE_OBJECT_IDS[3],
                            'imagePath': '서버 어딘가에 있겠죵 ㅎㅎ',
                            'name': '장다혜',
                            'workplace': '관악 중앙 요양원',
                            'patientInCharge': 5,
                            'career': 10,
                            'overall': 3.5
                        }
                    ]
                }
            }
        }
    }
}


