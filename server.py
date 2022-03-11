from flask import Flask, request, jsonify
from crendentials import credentials as cd
import threading
from utils import issues as isu

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    data = request.get_json(silent=True)
    print(data)

    if data['event']['subscription'] == "transfer":
        pass

    if data['event']['log']['type'] == "credited":
        try:
            cd.credentials_init()
            isu.transfer_stark(data['event']['log']['invoice']['amount'])
        except:
            pass
    else:
        pass

    return jsonify(data)


def run_app():
    app.debug = False
    app.run()


if __name__ == '__main__':
    first_thread = threading.Thread(target=run_app)
    second_thread = threading.Thread(target=isu.schedule_issue)
    first_thread.start()
    second_thread.start()
