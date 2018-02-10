from flask import Flask

from pages.api import BossList, BossWeak

app = Flask(__name__)


@app.route('/api/GetBossList')
def boss_list():
    return BossList.exec()


@app.route('/api/GetBossWeak')
def boss_weak():
    return BossWeak.exec()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8057, use_reloader=False)
