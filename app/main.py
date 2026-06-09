import random
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>Is This a Dumpster Fire?</title></head>
<body style="text-align:center; font-family:sans-serif; margin-top:100px;">
  <h1>🎲 Is This a Dumpster Fire?</h1>
  <p style="font-size:4em;">{{ emoji }}</p>
  <p style="font-size:1.5em;">You rolled a <b>{{ roll }}</b> — {{ verdict }}</p>
  <a href="/" style="font-size:1.2em;">Roll again</a>
</body>
</html>
"""

@app.route("/")
def roll():
    result = random.randint(1, 6)
    if result % 2 == 1:
        emoji, verdict = "🔥", "Dumpster fire!"
    else:
        emoji, verdict = "✅", "You're safe... for now."
    return render_template_string(HTML, emoji=emoji, roll=result, verdict=verdict)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
