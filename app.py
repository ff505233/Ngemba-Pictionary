from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

def load_words():
    """Load words from JSON file - called on each request so changes are picked up"""
    with open('data/words.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/concrete-nouns")
def concrete_nouns():
    words = load_words()
    cards = [w for w in words if w.get("category") == "concrete_nouns"]
    
    # Organize by subcategory
    animals = [w for w in cards if w.get("subcategory") == "animals"]
    objects = [w for w in cards if w.get("subcategory") == "objects"]
    nature = [w for w in cards if w.get("subcategory") == "nature"]
    
    return render_template("concrete_nouns.html", animals=animals, objects=objects, nature=nature)

@app.get("/core-verbs")
def core_verbs():
    words = load_words()
    cards = [w for w in words if w.get("category") == "core_verbs"]
    return render_template("core_verbs.html", cards=cards)

@app.get("/adjectives")
@app.get("/adjectives-test")
def adjectives():
    words = load_words()
    cards = [w for w in words if w.get("category") == "adjectives"]
    print(f"===ADJECTIVES ROUTE CALLED===", flush=True)
    print(f"Number of cards: {len(cards)}", flush=True)
    for i, card in enumerate(cards):
        print(f"  Card {i}: {card}", flush=True)
    response = app.make_response(render_template("adjectives.html", cards=cards))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.get("/culture")
def culture():
    words = load_words()
    cards = [w for w in words if w.get("category") == "culture"]
    return render_template("culture.html", cards=cards)

@app.get("/elementary-phrases")
def elementary_phrases():
    words = load_words()
    cards = [w for w in words if w.get("category") == "elementary_phrases"]
    return render_template("elementary_phrases.html", cards=cards)

@app.get("/grid")
def grid():
    words = load_words()
    q = (request.args.get("q") or "").strip().lower()
    cards = [c for c in words if q in c["en"].lower() or q in c["id"]]
    return render_template("grid.html", cards=cards)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

