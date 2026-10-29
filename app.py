import os
from flask import Flask, render_template

# template ka exact rasta batana padega
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    skills = [
        {"title": "Communication Skill", "desc": "Daily speaking practice", "icon": "💬"},
        {"title": "Public Speaking", "desc": "Stage fear removal", "icon": "🎤"},
        {"title": "Body Language", "desc": "Posture & gestures", "icon": "🧍"},
        {"title": "Group Discussion", "desc": "GD practice", "icon": "👥"},
        {"title": "Interview Skills", "desc": "HR questions", "icon": "💼"},
        {"title": "Personality Development", "desc": "Confidence growth", "icon": "🌟"}
    ]
    return render_template('index.html', skills=skills)

if __name__ == '__main__':
    app.run(debug=True)
