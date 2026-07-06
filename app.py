from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>B9IS121 - Group 4</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: Segoe UI, sans-serif; background: #f5f5f5; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 40px 20px; }
  .wrap { background: #ffffff; border-radius: 16px; padding: 2.5rem; max-width: 700px; width: 100%; }
  .header { text-align: center; margin-bottom: 2rem; }
  .header h1 { font-size: 22px; font-weight: 500; color: #111; margin-bottom: 6px; }
  .header p { font-size: 14px; color: #888; }
  .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
  .card { background: #f9f9f9; border: 1px solid #ebebeb; border-radius: 12px; padding: 1.5rem 1rem; text-align: center; }
  .av { width: 56px; height: 56px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 500; margin: 0 auto 14px; }
  .card h3 { font-size: 14px; font-weight: 500; color: #111; }
</style>
</head>
<body>
  <div class="wrap">
    <div class="header">
      <h1>B9IS121 - Networking CA1</h1>
      <p>Group 4 - Dublin Business School - MSc Cybersecurity</p>
    </div>
    <div class="grid">
      <div class="card">
        <div class="av" style="background:#dbeafe;color:#1d4ed8">AN</div>
        <h3>Muhammad Arshman Noor</h3>
      </div>
      <div class="card">
        <div class="av" style="background:#ede9fe;color:#6d28d9">HM</div>
        <h3>Hammad Malik</h3>
      </div>
      <div class="card">
        <div class="av" style="background:#dcfce7;color:#15803d">KM</div>
        <h3>Khawaja Moiz</h3>
      </div>
    </div>
  </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
