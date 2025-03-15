'''from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # This connects to index.html

if __name__ == '__main__':
    app.run(debug=True)
'''
from flask import Flask, render_template, request

app = Flask(__name__)

# Mood-based recommendations
recommendations = {
    "happy": {
        "song": "Happy - Pharrell Williams",
        "activity": "Go for a walk in nature! 🌳"
    },
    "sad": {
        "song": "Fix You - Coldplay",
        "activity": "Watch a comfort movie with a warm drink. ☕"
    },
    "energetic": {
        "song": "Can't Stop - Red Hot Chili Peppers",
        "activity": "Do a quick workout or dance session! 💃"
    },
    "relaxed": {
        "song": "Weightless - Marconi Union",
        "activity": "Try meditation or read a book. 📖"
    },
    "overwhelmed": {
        "song": "Weightless - Marconi Union",
        "activity": "Take deep breaths and write down your thoughts. 📝"
    },
    "anxious": {
        "song": "Breathe Me - Sia",
        "activity": "Try a short guided meditation or stretching. 🧘"
    },
    "bored": {
        "song": "Shut Up and Dance - WALK THE MOON",
        "activity": "Try learning something new, like origami or a fun fact. 🎭"
    },
    "motivated": {
        "song": "Eye of the Tiger - Survivor",
        "activity": "Set a small goal and smash it! 🚀"
    },
    "lonely": {
        "song": "Talking to the Moon - Bruno Mars",
        "activity": "Call a friend or write a letter to your future self. ✉️"
    },
    "nostalgic": {
        "song": "Photograph - Ed Sheeran",
        "activity": "Look at old photos or rewatch a childhood movie. 🎞️"
    },
    "stressed": {
        "song": "Someone Like You - Adele",
        "activity": "Listen to calming music and sip some tea. 🍵"
    }
}



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    user_mood = request.form.get("mood")  # Get the selected mood from the form
    recommendation = recommendations.get(user_mood, {"song": "No suggestion", "activity": "Try something new!"})

    return render_template("result.html", mood=user_mood, song=recommendation["song"],
                           activity=recommendation["activity"])


if __name__ == "__main__":
    app.run(debug=True)
