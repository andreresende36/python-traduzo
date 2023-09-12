from flask import Blueprint, render_template, request

from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.find()

    text_to_translate = "O que deseja traduzir"
    translate_from = "english"
    translate_to = "afrikaans"
    translated = "Tradução"

    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
        translated = translate_text(
            text_to_translate, translate_from, translate_to
        )

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


def translate_text(text, source_language, target_language):
    try:
        translator = GoogleTranslator(
            source=source_language, target=target_language
        )
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        print(f"Erro na tradução: {e}")
        return "Erro na tradução"


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    raise NotImplementedError
