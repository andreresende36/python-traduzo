from bson import ObjectId
from src.models.history_model import HistoryModel
from src.models.user_model import UserModel
from src.database.db import db


# Req. 9
def test_history_delete(app_test):
    mock_data = {"name": "admin", "password": "123456", "token": "123456"}
    user = UserModel(mock_data)
    user.save()

    mock_history_data = {
        "text-to-translate": "Hello, I like videogame",
        "translate-from": "en",
        "translate-to": "pt",
    }
    history = HistoryModel(mock_history_data)
    history.save()

    assert (
        db.get_collection("history").find_one({"_id": history.data["_id"]})
        is not None
    )
    app_test.delete(
        f"/admin/history/{ObjectId(history.data['_id'])}",
        headers={
            "Authorization": user.data["token"],
            "User": user.data["name"],
        },
    )
    assert (
        db.get_collection("history").find_one({"_id": history.data["_id"]})
        is None
    )
