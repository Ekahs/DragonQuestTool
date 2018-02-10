import libs.dao.dao as dao
from libs.dao.models import BossList
from libs.soup.SoupModel import SoupModel

BOSS_URL_1 = 'http://www.dq10data.com/boss_weak1.html'
BOSS_URL_2 = 'http://www.dq10data.com/boss_weak2.html'
BOSS_URL_3 = 'http://www.dq10data.com/boss_weak3.html'
BOSS_URL_4 = 'http://www.dq10data.com/boss_weak4.html'
BOSS_URL_5 = 'http://www.dq10data.com/boss_weak5.html'


def exec():
    set_boss_list(BOSS_URL_1, 1)
    set_boss_list(BOSS_URL_2, 2)
    set_boss_list(BOSS_URL_3, 3)
    set_boss_list(BOSS_URL_4, 4)
    set_boss_list(BOSS_URL_5, 5)


def set_boss_list(url, boss_type):
    soup_model = SoupModel(url)
    soup = soup_model.get_soup()
    boss_table = soup.find('table', class_='tline_b')
    for tr in boss_table.find_all('tr'):
        td = tr.find('td')
        if td is not None:
            boss_name = tr.find('td').text
            if boss_name != '炎':
                insert_boss(boss_name, boss_type)


def insert_boss(boss_name, boss_type):
    boss_data = dao.db_session.query(BossList).filter(BossList.name == boss_name, BossList.boss_type == boss_type).all()
    if not boss_data:
        boss = BossList(boss_name, boss_type)
        dao.db_session.add(boss)
        dao.db_session.commit()


exec()
