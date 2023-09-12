from flask import Blueprint
from models.history_model import HistoryModel
import json

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/history/", methods=["GET"])
def list_history():
    history_data = json.loads(HistoryModel.list_as_json())
    return history_data, 200
