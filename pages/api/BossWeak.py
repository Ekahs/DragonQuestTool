import json

import libs.dao.dao as dao
from libs.dao.models import BossList, BossWeak


def exec():
    return get_json()


def get_json():
    boss_model_list = dao.db_session.query(BossList).all()
    response = {'list': []}
    for boss_model in boss_model_list:
        boss_weak = dao.db_session.query(BossWeak).filter(BossWeak.boss_list_id == boss_model.boss_list_id).all()[0]
        weak = {'boss_list_id': boss_weak.boss_list_id,
                'fire': boss_weak.fire,
                'ice': boss_weak.fire,
                'storm': boss_weak.fire,
                'thunder': boss_weak.fire,
                'soil': boss_weak.fire,
                'dirk': boss_weak.fire,
                'light': boss_weak.fire
                }
        response['list'].append(weak)

    return json.dumps(response)
