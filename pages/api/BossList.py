import json

import libs.dao.dao as dao
from libs.dao.models import BossList


def exec():
    return get_json()


def get_json():
    boss_model_list = dao.db_session.query(BossList).all()
    boss_list = {'list': []}
    for boss_model in boss_model_list:
        boss_list['list'].append({'id': boss_model.boss_list_id, 'name': boss_model.name, 'type': boss_model.boss_type})

    return json.dumps(boss_list)
