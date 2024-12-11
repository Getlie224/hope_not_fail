from flask import Flask, render_template

app = Flask(__name__)

# Dummy timetable data (replace this with real database data later)
courses = [
    {"name": "Math 101", "time": "Monday 9:00 AM", "level": "Freshman"},
    {"name": "English 201", "time": "Tuesday 11:00 AM", "level": "Sophomore"},
    {"name": "History 301", "time": "Wednesday 1:00 PM", "level": "Junior"},
    {"name": "Biology 401", "time": "Thursday 3:00 PM", "level": "Senior"},
    {"name": "Computer Science 102", "time": "Friday 10:00 AM", "level": "Freshman"}
]

@app.route('/')
def home():
    return render_template('final.html', courses=courses)

if __name__ == '__main__':
    app.run(debug=True)
