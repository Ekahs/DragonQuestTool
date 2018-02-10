from flask import Flask

from pages.api import BossList

app = Flask(__name__)


@app.route('/api/GetBossList')
def boss_list():
    return BossList.exec()


if __name__ == '__main__':
    app.run()
