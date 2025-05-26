from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'anime_data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    anime_list = load_data()
    return render_template('index.html', anime_list=anime_list)

@app.route('/add', methods=['GET', 'POST'])
def add_anime():
    if request.method == 'POST':
        anime = {
            "title": request.form['title'],
            "status": request.form['status'],
            "episodes_watched": int(request.form['episodes_watched']),
            "episodes_total": int(request.form['episodes_total']),
            "score": int(request.form['score']),
            "notes": request.form['notes']
        }
        data = load_data()
        data.append(anime)
        save_data(data)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:index>')
def delete_anime(index):
    data = load_data()
    if 0 <= index < len(data):
        del data[index]
        save_data(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
