from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    name = "Pakawat Phasook"
    
    # Get the current time and format it in 'LLLL' format using moment.js (done in the template)
    current_time = datetime.now(pytz.timezone('America/Toronto'))  # Adjust timezone as needed
    return render_template('index.html', name=name, time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
