import webbrowser
import os
html_content = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>The Iris Collection</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    min-height: 100vh;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    text-align: center;
    background-color: #2d3830;
    font-family: Georgia, serif;
    overflow: hidden;
  }
  .bg-svg {
    position: fixed; inset: 0;
    width: 100%; height: 100%;
    pointer-events: none; opacity: 0.18;
  }
  .company {
    font-size: 11px; letter-spacing: 0.2em;
    text-transform: uppercase; color: #9aab9e;
    margin-bottom: 1.8rem;
    font-family: Helvetica, sans-serif;
    opacity: 0;
    animation: fadeIn 0.5s ease forwards;
    animation-delay: 0.1s;
  }
  .divider {
    display: flex; align-items: center; gap: 12px;
    width: 200px; justify-content: center;
    margin: 0 auto 1.8rem;
    opacity: 0;
    animation: fadeIn 0.5s ease forwards;
    animation-delay: 0.3s;
  }
  .divider-line { flex: 1; height: 0.5px; background: rgba(255,255,255,0.18); }
  .divider-dot { width: 5px; height: 5px; border-radius: 50%; background: #4fcf9a; flex-shrink: 0; }
  .title {
    font-size: 52px; font-weight: 400;
    color: #edf2ee; line-height: 1.2;
    margin-bottom: 0.5rem;
  }
  .word {
    display: inline-block;
    opacity: 0; transform: translateY(16px);
    animation: wordIn 0.5s ease forwards;
  }
  .green { color: #4fcf9a; }
  .subtitle {
    font-size: 13px; color: #9aab9e;
    font-family: Helvetica, sans-serif;
    margin-bottom: 2.2rem;
    letter-spacing: 0.02em;
    opacity: 0;
    animation: fadeIn 0.5s ease forwards;
    animation-delay: 1.3s;
  }
  .divider-bot {
    display: flex; align-items: center; gap: 12px;
    width: 200px; justify-content: center;
    margin: 0 auto 2rem;
    opacity: 0;
    animation: fadeIn 0.5s ease forwards;
    animation-delay: 1.5s;
  }
  .btn {
    padding: 12px 40px;
    background: transparent; color: #edf2ee;
    border: 0.5px solid rgba(255,255,255,0.3);
    font-size: 12px; font-family: Helvetica, sans-serif;
    letter-spacing: 0.1em; text-transform: uppercase;
    cursor: pointer;
    opacity: 0;
    animation: fadeIn 0.5s ease forwards;
    animation-delay: 1.7s;
  }
  .btn:hover { background: rgba(255,255,255,0.07); }
  @keyframes fadeIn { to { opacity: 1; } }
  @keyframes wordIn { to { opacity: 1; transform: translateY(0); } }
</style>
</head>
<body>
<svg class="bg-svg" viewBox="0 0 1400 900" xmlns="http://www.w3.org/2000/svg">
  <!-- top left -->
  <ellipse cx="100" cy="80"  rx="9" ry="26" fill="#4fcf9a" transform="rotate(-20 100 80)"/>
  <ellipse cx="140" cy="45"  rx="8" ry="22" fill="#a89de8" transform="rotate(15 140 45)"/>
  <ellipse cx="60"  cy="120" rx="7" ry="19" fill="#e07aaa" transform="rotate(-55 60 120)"/>
  <!-- top right -->
  <ellipse cx="1300" cy="75"  rx="9" ry="26" fill="#e07aaa" transform="rotate(20 1300 75)"/>
  <ellipse cx="1260" cy="45"  rx="8" ry="22" fill="#4fcf9a" transform="rotate(-15 1260 45)"/>
  <ellipse cx="1340" cy="120" rx="7" ry="19" fill="#a89de8" transform="rotate(55 1340 120)"/>
  <!-- bottom left -->
  <ellipse cx="100"  cy="820" rx="9" ry="26" fill="#a89de8" transform="rotate(30 100 820)"/>
  <ellipse cx="138"  cy="858" rx="8" ry="22" fill="#e07aaa" transform="rotate(-10 138 858)"/>
  <ellipse cx="58"   cy="780" rx="7" ry="19" fill="#4fcf9a" transform="rotate(62 58 780)"/>
  <!-- bottom right -->
  <ellipse cx="1298" cy="818" rx="9" ry="26" fill="#4fcf9a" transform="rotate(-30 1298 818)"/>
  <ellipse cx="1336" cy="856" rx="8" ry="22" fill="#a89de8" transform="rotate(10 1336 856)"/>
  <ellipse cx="1258" cy="778" rx="7" ry="19" fill="#e07aaa" transform="rotate(-62 1258 778)"/>
</svg>
<!-- content -->
<p class="company">Synent Technologies</p>
<div class="divider">
  <div class="divider-line"></div>
  <div class="divider-dot"></div>
  <div class="divider-line"></div>
</div>
<h1 class="title">
  <span class="word" style="animation-delay:0.5s;">The&nbsp;</span>
  <span class="word green" style="animation-delay:0.8s;">Iris</span><br>
  <span class="word" style="animation-delay:1.0s;">Collection</span>
</h1>
<p class="subtitle">A visual journey through nature\'s data</p>
<div class="divider-bot">
  <div class="divider-line"></div>
  <div class="divider-dot"></div>
  <div class="divider-line"></div>
</div>
<button class="btn" onclick="window.location.href=\'main.html\'">Begin Exploration</button>
</body>
</html>'''
with open("index.html", "w") as f:
    f.write(html_content)
webbrowser.open("file://" + os.path.abspath("index.html")) 