from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    frenchtranslation = language_translator.translate(
    text=english_text, model_id='en-fr').get_result()
    return frenchtranslation
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here

    englishtranslation = language_translator.translate(
    text=french_text, model_id='fr-en').get_result()
    return englishtranslation
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    authenticator = IAMAuthenticator('8hd5Nw2PVGkJyUYHfiG3s-oU8zHSyuxNIhhVamCttHgQ')
    language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )

language_translator.set_service_url('https://api.us-south.language-tr

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
