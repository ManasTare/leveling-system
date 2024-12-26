from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    skills = {
        "workout": ["Push-ups", "Squats", "Planks", "Running"],
        "it_skills": ["Python", "SQL", "Networking", "Cybersecurity"],
        "miscellaneous": ["Cooking", "Time Management", "Public Speaking"]
    }
    return render_template('index.html', skills=skills)

if __name__ == '__main__':
    app.run(debug=True)
