from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return render_template_string(f.read())

@app.route('/timetable')
def timetable():
    return """
    <html>
    <head>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
    <div class="container">
        <h1>University Timetable</h1>

        <table>
            <tr>
                <th>Day</th>
                <th>9-10</th>
                <th>10-11</th>
                <th>11-12</th>
                <th>1-2</th>
            </tr>

            <tr>
                <td>Monday</td>
                <td>Python</td>
                <td>DSA</td>
                <td>DBMS</td>
                <td>AI</td>
            </tr>

            <tr>
                <td>Tuesday</td>
                <td>Java</td>
                <td>Python</td>
                <td>OS</td>
                <td>DBMS</td>
            </tr>

            <tr>
                <td>Wednesday</td>
                <td>AI</td>
                <td>DSA</td>
                <td>Python</td>
                <td>Java</td>
            </tr>

            <tr>
                <td>Thursday</td>
                <td>OS</td>
                <td>DBMS</td>
                <td>AI</td>
                <td>Python</td>
            </tr>

            <tr>
                <td>Friday</td>
                <td>Java</td>
                <td>DSA</td>
                <td>OS</td>
                <td>AI</td>
            </tr>

        </table>

        <br>

        <a href="/">Back</a>
    </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)