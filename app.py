# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for
import json
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "ngemba-secret-key-2025")

# Translations dictionary
TRANSLATIONS = {
  'en': {
    'concrete_nouns': 'Concrete Nouns',
    'core_verbs': 'Core Verbs',
    'adjectives': 'Adjectives',
    'elementary_phrases': 'Elementary Phrases',
    'home': 'Home',
    'learn_ngemba': 'LearnNgemba',
    'discover': 'Discover Ngemba words and meanings through interactive pictures and real speaker recordings.',
    'about_ngemba': 'Ngemba is a language spoken in the western part of Cameroon. It includes parts of the Bamendjou, Bamenka, Bamenda, Bafounda, Bansoa and Bamougoum villages. This Ngemba learning tool features the voices of speakers with the Ngemba dialect spoken in Bamendjou. Each section has cards with images and a written word in French or English. When you click the image, a recording of the word or sentence in Ngemba will play. You may have to turn your volume up if you cannot hear well.',
    'get_ready': 'Get ready to learn Ngemba!',
    'start_learning': 'Start Learning',
    'thank_you': 'Special thank you to the speakers who contributed to this language learning tool:',
    'copyright': '© 2025 Learn Ngemba. Open educational project for Ngemba language preservation.',
    'learn_everyday': 'Learn everyday objects in Ngemba',
    'learn_actions': 'Learn essential actions in Ngemba',
    'describe_world': 'Describe the world in Ngemba',
    'master_phrases': 'Master basic conversational phrases',
    'animals': 'Animals',
    'objects': 'Objects',
    'nature': 'Nature',
    'contact': 'Contact',
    'contact_message': 'Contact website creator <strong>Francis Fokoue-Nkoutche</strong> at <a href="mailto:fokouefrancis5@gmail.com">fokouefrancis5@gmail.com</a> if you have any questions or wish to add words.'
  },
  'fr': {
    'concrete_nouns': 'Noms Concrets',
    'core_verbs': 'Verbes Principaux',
    'adjectives': 'Adjectifs',
    'elementary_phrases': 'Phrases Élémentaires',
    'home': 'Accueil',
    'learn_ngemba': 'Apprendre Ngemba',
    'discover': 'Découvrez les mots et significations Ngemba à travers des images interactives et des enregistrements de locuteurs réels.',
    'about_ngemba': 'Le Ngemba est une langue parlée dans la partie ouest du Cameroun. Il comprend des parties des villages de Bamendjou, Bamenka, Bamenda, Bafounda, Bansoa et Bamougoum. Cet outil d\'apprentissage Ngemba présente les voix de locuteurs avec le dialecte Ngemba parlé à Bamendjou. Chaque section contient des cartes avec des images et un mot écrit en français ou en anglais. Lorsque vous cliquez sur l\'image, un enregistrement du mot ou de la phrase en Ngemba sera joué. Vous devrez peut-être augmenter le volume si vous ne pouvez pas bien entendre.',
    'get_ready': 'Préparez-vous à apprendre le Ngemba !',
    'start_learning': 'Commencer l\'Apprentissage',
    'thank_you': 'Merci spécial aux locuteurs qui ont contribué à cet outil d\'apprentissage linguistique :',
    'copyright': '© 2025 Apprendre Ngemba. Projet éducatif ouvert pour la préservation de la langue Ngemba.',
    'learn_everyday': 'Apprenez les objets du quotidien en Ngemba',
    'learn_actions': 'Apprenez les actions essentielles en Ngemba',
    'describe_world': 'Décrivez le monde en Ngemba',
    'master_phrases': 'Maîtrisez les phrases conversationnelles de base',
    'animals': 'Animaux',
    'objects': 'Objets',
    'nature': 'Nature',
    'contact': 'Contact',
    'contact_message': 'Contactez le créateur du site <strong>Francis Fokoue-Nkoutche</strong> à <a href="mailto:fokouefrancis5@gmail.com">fokouefrancis5@gmail.com</a> si vous avez des questions ou souhaitez ajouter des mots.'
  }
}

@app.context_processor
def inject_translations():
    """Make translations available to all templates"""
    lang = session.get('language', 'en')
    return dict(t=TRANSLATIONS.get(lang, TRANSLATIONS['en']), lang=lang)

def load_words():
    """Load words from JSON file - called on each request so changes are picked up"""
    with open('data/words.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_language():
    """Get the current language from session or default to English"""
    return session.get('language', 'en')

@app.get("/")
def index():
    """Language selection page"""
    return render_template("language_select.html")

@app.get("/home")
def home():
    lang = request.args.get('lang', session.get('language', 'en'))
    session['language'] = lang
    return render_template("home.html", lang=lang)

@app.get("/concrete-nouns")
def concrete_nouns():
    lang = get_language()
    words = load_words()
    cards = [w for w in words if w.get("category") == "concrete_nouns"]
    
    # Organize by subcategory
    animals = [w for w in cards if w.get("subcategory") == "animals"]
    objects = [w for w in cards if w.get("subcategory") == "objects"]
    nature = [w for w in cards if w.get("subcategory") == "nature"]
    
    return render_template("concrete_nouns.html", animals=animals, objects=objects, nature=nature, lang=lang)

@app.get("/core-verbs")
def core_verbs():
    lang = get_language()
    words = load_words()
    cards = [w for w in words if w.get("category") == "core_verbs"]
    return render_template("core_verbs.html", cards=cards, lang=lang)

@app.get("/adjectives")
@app.get("/adjectives-test")
def adjectives():
    lang = get_language()
    words = load_words()
    cards = [w for w in words if w.get("category") == "adjectives"]
    print(f"===ADJECTIVES ROUTE CALLED===", flush=True)
    print(f"Number of cards: {len(cards)}", flush=True)
    for i, card in enumerate(cards):
        print(f"  Card {i}: {card}", flush=True)
    response = app.make_response(render_template("adjectives.html", cards=cards, lang=lang))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.get("/elementary-phrases")
def elementary_phrases():
    lang = get_language()
    words = load_words()
    cards = [w for w in words if w.get("category") == "elementary_phrases"]
    return render_template("elementary_phrases.html", cards=cards, lang=lang)

@app.get("/grid")
def grid():
    words = load_words()
    q = (request.args.get("q") or "").strip().lower()
    cards = [c for c in words if q in c["en"].lower() or q in c["id"]]
    return render_template("grid.html", cards=cards)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

