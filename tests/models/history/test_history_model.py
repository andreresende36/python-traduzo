import json
from src.models.history_model import HistoryModel


# Req. 7
def test_list_as_json():
    translations = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]
    history_json = json.loads(HistoryModel.list_as_json())
    for i, translation in enumerate(translations):
        del history_json[i]["_id"]
        assert history_json[i] == translation
