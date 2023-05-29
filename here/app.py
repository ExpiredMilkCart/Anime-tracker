from flask import Flask, render_template, request

app = Flask(__name__)

class Anime:
    def __init__(self, title, genre, episodes_watched, image_url, website_url):
        self.title = title
        self.genre = genre
        self.episodes_watched = episodes_watched
        self.image_url = image_url
        self.website_url = website_url

anime_data = []

@app.route('/')
def display_anime():
    return render_template('anime.html', anime_list=anime_data)

@app.route('/add_anime', methods=['POST'])
def add_anime():
    title = request.form['title']
    genre = request.form['genre']
    episodes_watched = request.form['episodes_watched']
    image_url = request.form['image_url']
    website_url = request.form['website_url']

    # Check if anime already exists in the list
    for anime in anime_data:
        if anime.title == title:
            return render_template('anime.html', anime_list=anime_data)

    anime = Anime(title, genre, episodes_watched, image_url, website_url)
    anime_data.append(anime)

    return render_template('anime.html', anime_list=anime_data)

if __name__ == '__main__':
    app.run(debug=True)
