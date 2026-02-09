from flask import Flask, render_template_string
import requests

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>SentinelX Dashboard</title>
    <style>
        body { font-family: Arial;
background: #111; color: #eee; }
        table { width: 50%; margin: 40px
auto; border-collapse: collapse; }
        th, td {padding: 12px; border: 1px
solid #444; text-align; center; }
        th { background: #222; }
        .OK { color: #00ff00; }
        .FAIL { color: #ff3333; }
        .UNKNOWN { color: #ffaa00; }
    </style>
</head>
<body>
    <h1 style="text-align:center;">
SentinelX Live Dashboard</h1>
    <table>
        <tr>
            <th>Service</th>
            <th>Status</th>
            <th>Last Checked</th>
        </tr>
        {% for name, info in services.items()
%}
        <tr>
            <td>{{ name }}</td>
            <td
class="{{ info.status }}">{{ info.status }}</td>
            <td>{{ info.last_checked }}</td>
        </tr>
        {%endfor %}
    </table>
</body
</html
"""

@app.route("/")
def dashboard():
    try:
        services = requests.get("http://localhost:7000/status", timeout=2).json()
    except:
        services = {}
    return render_template_string(HTML, services=services)

if __name__== "__main__":
    app.run(host="0.0.0.0", port=8000)
