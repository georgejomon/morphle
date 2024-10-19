from flask import Flask, render_template_string
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv('USER') or os.getenv('USERNAME')
    # Get current server time in IST
    server_time_ist = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime('%Y-%m-%d %H:%M:%S')

    # Get top output (you might want to limit the number of lines for simplicity)
    top_output = subprocess.check_output(['top', '-b', '-n', '1'], universal_newlines=True).splitlines()[:10]

    # HTML template
    html_template = """
    <html>
        <head><title>HTop Output</title></head>
        <body>
            <h1>Server Information</h1>
            <p><strong>Name:</strong> Chris George Jomon</p>
            <p><strong>Username:</strong> {{ username }}</p>
            <p><strong>Server Time (IST):</strong> {{ server_time_ist }}</p>
            <h2>Top Output:</h2>
            <pre>{{ top_output }}</pre>
        </body>
    </html>
    """
    return render_template_string(html_template, username=username, server_time_ist=server_time_ist, top_output='\n'.join(top_output))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
