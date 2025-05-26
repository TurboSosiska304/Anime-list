from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = "anime_secret_key"

DATA_FILE = "anime_data.json"
LANGUAGES = ["en", "ru"]

TRANSLATIONS = {
    "en": {
        "title": "Anime Tracker",
        "add_anime": "Add Anime",
        "edit_anime": "Edit Anime",
        "name": "Name",
        "watched": "Watched",
        "yes": "Yes",
        "no": "No",
        "link": "Link (optional)",
        "submit": "Submit",
        "back": "Back",
        "language": "Language",
        "no_anime": "No anime added yet.",
        "watched_eps": "Watched episodes",
        "total_eps": "Total episodes",
        "rating": "Rating",
        "edit": "Edit"
    },
    "ru": {
        "title": "Аниме Трекер",
        "add_anime": "Добавить аниме",
        "edit_anime": "Редактировать аниме",
        "name": "Название",
        "watched": "Просмотрено",
        "yes": "Да",
        "no": "Нет",
        "link": "Ссылка (необязательно)",
        "submit": "Сохранить",
        "back": "Назад",
        "language": "Язык",
        "no_anime": "Аниме пока не добавлены.",
        "watched_eps": "Просмотрено серий",
        "total_eps": "Всего серий",
        "rating": "Оценка",
        "edit": "Редактировать"
    }
}

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@app.before_request
def set_language():
    lang = request.args.get("lang")
    if lang in LANGUAGES:
        session["lang"] = lang
    if "lang" not in session:
        session["lang"] = "en"

@app.route("/")
def index():
    anime_list = load_data()
    lang = session["lang"]
    t = TRANSLATIONS[lang]
    return render_template("index.html", anime_list=anime_list, t=t, lang=lang)

@app.route("/add", methods=["GET", "POST"])
def add():
    lang = session["lang"]
    t = TRANSLATIONS[lang]
    if request.method == "POST":
        anime = {
            "name": request.form["name"].strip(),
            "watched": request.form["watched"] == "yes",
            "link": request.form["link"].strip(),
            "watched_eps": request.form.get("watched_eps", "0"),
            "total_eps": request.form.get("total_eps", "0"),
            "rating": int(request.form.get("rating", 0))
        }
        anime_list = load_data()
        anime_list.append(anime)
        save_data(anime_list)
        return redirect(url_for("index"))
    return render_template("add.html", t=t, lang=lang)

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    anime_list = load_data()
    lang = session["lang"]
    t = TRANSLATIONS[lang]
    if index >= len(anime_list):
        return redirect(url_for("index"))
    if request.method == "POST":
        anime_list[index] = {
            "name": request.form["name"].strip(),
            "watched": request.form["watched"] == "yes",
            "link": request.form["link"].strip(),
            "watched_eps": request.form.get("watched_eps", "0"),
            "total_eps": request.form.get("total_eps", "0"),
            "rating": int(request.form.get("rating", 0))
        }
        save_data(anime_list)
        return redirect(url_for("index"))
    return render_template("edit.html", anime=anime_list[index], index=index, t=t, lang=lang)

if __name__ == "__main__":
    app.run(debug=True)
