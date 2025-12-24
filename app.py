from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Load words from JSON
with open('data/words.json', 'r', encoding='utf-8') as f:
    WORDS = json.load(f)

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/concrete-nouns")
def concrete_nouns():
    cards = [w for w in WORDS if w.get("category") == "concrete_nouns"]
    return render_template("concrete_nouns.html", cards=cards)

@app.get("/core-verbs")
def core_verbs():
    cards = [w for w in WORDS if w.get("category") == "core_verbs"]
    return render_template("core_verbs.html", cards=cards)

@app.get("/adjectives")
def adjectives():
    cards = [w for w in WORDS if w.get("category") == "adjectives"]
    return render_template("adjectives.html", cards=cards)

@app.get("/culture")
def culture():
    cards = [w for w in WORDS if w.get("category") == "culture"]
    return render_template("culture.html", cards=cards)

@app.get("/elementary-phrases")
def elementary_phrases():
    cards = [w for w in WORDS if w.get("category") == "elementary_phrases"]
    return render_template("elementary_phrases.html", cards=cards)

@app.get("/grid")
def grid():
    q = (request.args.get("q") or "").strip().lower()
    cards = [c for c in CARDS if q in c["en"].lower() or q in c["id"]]
    return render_template("grid.html", cards=cards)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
