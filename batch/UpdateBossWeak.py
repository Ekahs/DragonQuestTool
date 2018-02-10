import libs.dao.dao as dao
from libs.dao.models import BossList, BossWeak
from libs.soup.SoupModel import SoupModel

BOSS_URL_1 = 'http://www.dq10data.com/boss_weak1.html'
BOSS_URL_2 = 'http://www.dq10data.com/boss_weak2.html'
BOSS_URL_3 = 'http://www.dq10data.com/boss_weak3.html'
BOSS_URL_4 = 'http://www.dq10data.com/boss_weak4.html'
BOSS_URL_5 = 'http://www.dq10data.com/boss_weak5.html'


def exec():
    set_weak_list(BOSS_URL_1, 1)
    set_weak_list(BOSS_URL_2, 2)
    set_weak_list(BOSS_URL_3, 3)
    set_weak_list(BOSS_URL_4, 4)
    set_weak_list(BOSS_URL_5, 5)


def set_weak_list(url, boss_type):
    soup_model = SoupModel(url)
    soup = soup_model.get_soup()
    boss_table = soup.find('table', class_='tline_b')
    for tr in boss_table.find_all('tr'):
        if tr.find('td').text == '炎':
            continue

        td_array = []
        for td in tr.find_all('td'):
            td_array.append(td.text)

        insert_weak(td_array, boss_type)


def insert_weak(weak_data, boss_type):
    boss_data = dao.db_session.query(BossList).filter(BossList.name == weak_data[0],
                                                      BossList.boss_type == boss_type).all()
    if boss_data is not None:
        target_id = boss_data[0].boss_list_id
        weak = BossWeak(target_id,
                        weak_data[1],
                        weak_data[2],
                        weak_data[3],
                        weak_data[4],
                        weak_data[5],
                        weak_data[6],
                        weak_data[7])
        dao.db_session.add(weak)
        dao.db_session.commit()

exec()
