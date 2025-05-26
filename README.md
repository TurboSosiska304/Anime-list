# Anime Tracker Web App

A lightweight web application to track your watched (and unwatched) anime. Built with Python and Flask, using a simple JSON file for storage.

---

## ✨ Features

- Add anime with:
  - Name
  - Watched / Not watched
  - Watched episodes
  - Total episodes
  - Rating (stars)
  - Optional link
- Edit existing entries
- Multilingual UI: English 🇬🇧 / Russian 🇷🇺
- Clean, responsive Bootstrap-based design
- Stores data in a local `anime_data.json` file

---

## 🛠 Requirements

- Python 3.7+
- pip

Install dependencies:

```bash
pip install Flask
```

---

## 🚀 How to Run

```bash
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser.

---

## 🌐 Language Switching

Use the dropdown in the top-right corner to switch between English and Russian. Language is stored per session.

---

## 📁 Project Structure

```
anime-tracker/
├── app.py
├── anime_data.json
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
├── static/
│   └── (optional custom CSS)
└── README.md
```

---

## 🔒 License

MIT — do whatever you want, just don’t blame me if it breaks :)

---

Made with ❤️ and anime by [TurboSosiska304](https://github.com/TurboSosiska304)
