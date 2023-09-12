from src.models.user_model import UserModel
from src.models.history_model import HistoryModel
from src.app import app
from flask.testing import FlaskClient
import json
from bson import ObjectId


# Req. 9
def test_history_delete(app_test: FlaskClient):
    # Cria um usuário para autenticação
    user_data = {
        "name": "admin_user",
        "password": "admin_password",
    }
    user = UserModel(user_data)
    user.save()

    # Cria um registro de histórico para exclusão
    history_data = {
        "text_to_translate": "Aqui tem um texto para teste",
        "translate_from": "en",
        "translate_to": "pt",
    }
    history = HistoryModel(history_data)
    history.save()

    # Autentica o usuário e obtém o token
    response = app_test.post(
        "/auth",
        data={
            "name": "admin_user",
            "password": "admin_password",
        },
    )
    assert response.status_code == 200
    auth_token = json.loads(response.data)["token"]

    # Obtém o ID do registro de histórico
    history_id = str(history["_id"])

    # Faz uma solicitação DELETE para excluir o registro
    response = app_test.delete(
        f"/admin/history/{history_id}",
        headers={
            "Authorization": auth_token,
            "User": "admin_user",
        },
    )
    assert response.status_code == 204

    # Verifica se o registro foi excluído do banco de dados
    deleted_history = HistoryModel.find_one({"_id": ObjectId(history_id)})
    assert deleted_history is None
