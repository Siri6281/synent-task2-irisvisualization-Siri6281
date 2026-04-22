import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from sklearn.datasets import load_iris
import webbrowser
import os
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
df.to_csv('iris_dataset.csv', index=False)
print("Dataset saved as iris_dataset.csv")
colors_map = {'setosa': '#4fcf9a', 'versicolor': '#a89de8', 'virginica': '#e07aaa'}
avg = df.groupby('species', observed=True)[iris.feature_names].mean()
fig1 = go.Figure()
for species in iris.target_names:
    fig1.add_trace(go.Bar(
        name=species,
        x=iris.feature_names,
        y=avg.loc[species],
        marker_color=colors_map[species.lower()],
        hovertemplate='<b>%{x}</b><br>Value: %{y:.2f} cm<extra></extra>',
        marker_line=dict(width=0)
    ))
fig1.update_layout(
    title='Average Feature by Species',
    xaxis_title='Features',
    yaxis_title='Measurement (cm)',
    barmode='group',
    plot_bgcolor='#fafbf9',
    paper_bgcolor='#fafbf9',
    hovermode='closest',
    font=dict(family='Georgia, serif', color='#333333', size=11),
    title_font_size=14,
    height=450,
    margin=dict(l=50, r=50, t=80, b=50),
    showlegend=True,
    legend=dict(bgcolor='rgba(255,255,255,0.9)', bordercolor='#e0e0e0', borderwidth=1)
)
fig1.write_html('chart1.html', include_plotlyjs='cdn', config={'responsive': True, 'displayModeBar': False})
chart1_html = open('chart1.html').read().split('<body>')[1].split('</body>')[0]
fig2 = go.Figure()
for i, species in enumerate(iris.target_names):
    subset = df[df['species'] == species]['petal length (cm)']
    fig2.add_trace(go.Histogram(
        x=subset,
        name=species,
        marker_color=colors_map[species.lower()],
        opacity=0.65,
        nbinsx=12,
        hovertemplate='Petal Length: %{x:.2f} cm<br>Count: %{y}<extra></extra>'
    ))
fig2.update_layout(
    title='Petal Length Distribution',
    xaxis_title='Petal Length (cm)',
    yaxis_title='Frequency',
    plot_bgcolor='#fafbf9',
    paper_bgcolor='#fafbf9',
    barmode='overlay',
    hovermode='x unified',
    font=dict(family='Georgia, serif', color='#333333', size=11),
    title_font_size=14,
    height=450,
    margin=dict(l=50, r=50, t=80, b=50),
    showlegend=True,
    legend=dict(bgcolor='rgba(255,255,255,0.9)', bordercolor='#e0e0e0', borderwidth=1)
)
fig2.write_html('chart2.html', include_plotlyjs='cdn', config={'responsive': True, 'displayModeBar': False})
chart2_html = open('chart2.html').read().split('<body>')[1].split('</body>')[0]
fig3 = go.Figure()
for species in iris.target_names:
    subset = df[df['species'] == species]
    fig3.add_trace(go.Scatter(
        x=subset['sepal length (cm)'],
        y=subset['sepal width (cm)'],
        mode='markers',
        name=species,
        marker=dict(
            size=8,
            color=colors_map[species.lower()],
            opacity=0.65,
            line=dict(width=1, color='white')
        ),
        hovertemplate='<b>%{fullData.name}</b><br>Sepal Length: %{x:.2f} cm<br>Sepal Width: %{y:.2f} cm<extra></extra>'
    ))
fig3.update_layout(
    title='Sepal Length vs Sepal Width',
    xaxis_title='Sepal Length (cm)',
    yaxis_title='Sepal Width (cm)',
    plot_bgcolor='#fafbf9',
    paper_bgcolor='#fafbf9',
    hovermode='closest',
    font=dict(family='Georgia, serif', color='#333333', size=11),
    title_font_size=14,
    height=450,
    margin=dict(l=50, r=50, t=80, b=50),
    showlegend=True,
    legend=dict(bgcolor='rgba(255,255,255,0.9)', bordercolor='#e0e0e0', borderwidth=1)
)
fig3.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#e5e5e5')
fig3.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#e5e5e5')
fig3.write_html('chart3.html', include_plotlyjs='cdn', config={'responsive': True, 'displayModeBar': False})
chart3_html = open('chart3.html').read().split('<body>')[1].split('</body>')[0]
corr_matrix = df[iris.feature_names].corr()
fig4 = go.Figure(data=go.Heatmap(
    z=corr_matrix.values,
    x=iris.feature_names,
    y=iris.feature_names,
    colorscale='Greens',
    zmin=-1, zmax=1,
    text=corr_matrix.values,
    texttemplate='%{text:.2f}',
    textfont={"size": 11},
    colorbar=dict(title='Correlation'),
    hovertemplate='%{x} vs %{y}<br>Correlation: %{z:.3f}<extra></extra>'
))
fig4.update_layout(
    title='Feature Correlation Heatmap',
    plot_bgcolor='#fafbf9',
    paper_bgcolor='#fafbf9',
    font=dict(family='Georgia, serif', color='#333333', size=11),
    title_font_size=14,
    height=500,
    margin=dict(l=120, r=80, t=80, b=120),
    xaxis=dict(side='bottom'),
    yaxis=dict(autorange='reversed')
)
fig4.write_html('chart4.html', include_plotlyjs='cdn', config={'responsive': True, 'displayModeBar': False})
chart4_html = open('chart4.html').read().split('<body>')[1].split('</body>')[0]
html_content = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Iris Collection</title>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ height: 100%; }}
  body {{
    background: linear-gradient(135deg, #f0f2f0 0%, #e8eae7 100%);
    font-family: Georgia, serif;
    color: #333333;
    padding: 2.5rem 1.5rem;
    min-height: 100vh;
  }}
  .container {{
    max-width: 800px;
    margin: 0 auto;
    width: 100%;
  }}
  .header {{
    text-align: center;
    margin-bottom: 3rem;
    opacity: 0;
    animation: fadeIn 0.8s ease forwards;
    animation-delay: 0.2s;
  }}
  .company {{
    font-size: 10px; letter-spacing: 0.15em;
    text-transform: uppercase; color: #888888;
    font-family: Helvetica, sans-serif;
    margin-bottom: 0.8rem;
    font-weight: 500;
  }}
  .divider {{
    display: flex; align-items: center; gap: 10px;
    width: 150px; justify-content: center;
    margin: 0 auto 1.2rem;
  }}
  .divider-line {{ flex: 1; height: 0.5px; background: #4fcf9a; }}
  .divider-dot {{ width: 4px; height: 4px; border-radius: 50%; background: #4fcf9a; }}
  .title {{
    font-size: clamp(24px, 8vw, 28px);
    font-weight: 400;
    color: #333333; 
    margin-bottom: 0.3rem;
  }}
  .title span {{ color: #4fcf9a; font-weight: 600; }}
  .subtitle {{
    font-size: clamp(11px, 3vw, 12px);
    color: #888888;
    font-family: Helvetica, sans-serif;
    letter-spacing: 0.01em;
  }}
  .chart-section {{
    margin-bottom: 3.5rem;
    opacity: 0;
    animation: fadeIn 0.8s ease forwards;
    background: white;
    padding: clamp(1.2rem, 4vw, 1.8rem);
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    transition: all 0.3s ease;
  }}
  .chart-section:hover {{
    box-shadow: 0 8px 20px rgba(79, 207, 154, 0.2);
    transform: translateY(-4px);
  }}
  .chart-section:nth-child(2) {{ animation-delay: 0.4s; }}
  .chart-section:nth-child(3) {{ animation-delay: 0.7s; }}
  .chart-section:nth-child(4) {{ animation-delay: 1.0s; }}
  .chart-number {{
    display: inline-block;
    background: linear-gradient(135deg, #4fcf9a, #2aaa7a);
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    text-align: center;
    line-height: 32px;
    font-weight: 600;
    font-size: 14px;
    margin-bottom: 0.8rem;
    font-family: Helvetica, sans-serif;
  }}
  .chart-label {{
    font-size: clamp(13px, 4vw, 14px);
    font-weight: 600;
    color: #333333;
    font-family: Georgia, serif;
    margin-bottom: 1.2rem;
  }}
  .plotly-chart {{
    width: 100%;
    margin-bottom: 1.2rem;
  }}
  .insight {{
    font-size: clamp(11px, 2.5vw, 12px);
    color: #666666;
    font-family: Helvetica, sans-serif;
    line-height: 1.6;
    border-left: 2.5px solid #4fcf9a;
    padding: 0.9rem 0.9rem 0.9rem 1rem;
    background: #f7faf8;
    border-radius: 4px;
  }}
  .button-group {{
    display: flex;
    gap: 12px;
    justify-content: center;
    flex-wrap: wrap;
    margin: 2.5rem auto;
  }}
  .btn {{
    display: inline-block;
    padding: clamp(8px, 2vw, 10px) clamp(30px, 6vw, 35px);
    border: none;
    font-size: clamp(10px, 2.5vw, 11px);
    font-family: Helvetica, sans-serif;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    cursor: pointer;
    width: fit-content;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 600;
    transition: all 0.3s ease;
  }}
  .compare-btn {{
    background: linear-gradient(135deg, #a89de8, #7f77dd);
    color: white;
  }}
  .compare-btn:hover {{
    background: linear-gradient(135deg, #7f77dd, #6d65cc);
    transform: translateY(-2px);
    box-shadow: 0 3px 10px rgba(168, 157, 232, 0.3);
  }}
  .insights-btn {{
    background: linear-gradient(135deg, #e07aaa, #d4537e);
    color: white;
  }}
  .insights-btn:hover {{
    background: linear-gradient(135deg, #d4537e, #c0426b);
    transform: translateY(-2px);
    box-shadow: 0 3px 10px rgba(224, 122, 170, 0.3);
  }}
  .back-btn {{
    background: linear-gradient(135deg, #4fcf9a, #2aaa7a);
    color: white;
  }}
  .back-btn:hover {{ 
    background: linear-gradient(135deg, #2aaa7a, #1a8a5a);
    transform: translateY(-2px);
    box-shadow: 0 3px 10px rgba(79, 207, 154, 0.25);
  }}
  @media (max-width: 768px) {{
    body {{ padding: 2rem 1.2rem; }}
    .header {{ margin-bottom: 2.5rem; }}
    .chart-section {{ margin-bottom: 2.5rem; }}
  }}
  @media (max-width: 480px) {{
    body {{ padding: 1.5rem 1rem; }}
    .header {{ margin-bottom: 2rem; }}
    .divider {{ width: 120px; gap: 8px; }}
    .chart-number {{
      width: 28px;
      height: 28px;
      line-height: 28px;
      font-size: 12px;
    }}
    .chart-section {{ 
      margin-bottom: 2rem;
      padding: 1.2rem;
    }}
  }}
  @keyframes fadeIn {{ to {{ opacity: 1; }} }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <p class="company">Synent Technologies</p>
    <div class="divider">
      <div class="divider-line"></div>
      <div class="divider-dot"></div>
      <div class="divider-line"></div>
    </div>
    <h1 class="title">The <span>Iris</span> Collection</h1>
    <p class="subtitle">A visual journey through nature's data</p>
  </div>
  <div class="chart-section">
    <div class="chart-number">01</div>
    <p class="chart-label">Bar Chart - Average Features by Species</p>
    <div class="plotly-chart">{chart1_html}</div>
    <p class="insight">Hover over bars to see exact values. Setosa has the smallest petal dimensions while Virginica has the largest.</p>
  </div>
  <div class="chart-section">
    <div class="chart-number">02</div>
    <p class="chart-label">Histogram - Petal Length Distribution</p>
    <div class="plotly-chart">{chart2_html}</div>
    <p class="insight">Hover over bars to see frequency counts. Setosa petals are clearly shorter, around 1.5cm.</p>
  </div>
  <div class="chart-section">
    <div class="chart-number">03</div>
    <p class="chart-label">Scatter Plot - Sepal Dimensions Relationship</p>
    <div class="plotly-chart">{chart3_html}</div>
    <p class="insight">Hover over points to see exact measurements. Setosa is clearly separated from other species.</p>
  </div>
  <div class="button-group">
    <a href="compare.html" class="btn compare-btn">Compare Features</a>
    <a href="insights.html" class="btn insights-btn">View Insights</a>
    <a href="index.html" class="btn back-btn">Back to Home</a>
  </div>
</div>
</body>
</html>'''
with open("main.html", "w", encoding='utf-8') as f:
    f.write(html_content)
print("main.html generated successfully!")
compare_html_content = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Compare Features - The Iris Collection</title>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ height: 100%; }}
  body {{
    background: linear-gradient(135deg, #f0f2f0 0%, #e8eae7 100%);
    font-family: Georgia, serif;
    color: #333333;
    padding: 2.5rem 1.5rem;
    min-height: 100vh;
  }}
  .container {{
    max-width: 900px;
    margin: 0 auto;
    width: 100%;
  }}
  .header {{
    text-align: center;
    margin-bottom: 3rem;
    opacity: 0;
    animation: fadeIn 0.8s ease forwards;
    animation-delay: 0.2s;
  }}
  .company {{
    font-size: 10px; letter-spacing: 0.15em;
    text-transform: uppercase; color: #888888;
    font-family: Helvetica, sans-serif;
    margin-bottom: 0.8rem;
    font-weight: 500;
  }}
  .divider {{
    display: flex; align-items: center; gap: 10px;
    width: 150px; justify-content: center;
    margin: 0 auto 1.2rem;
  }}
  .divider-line {{ flex: 1; height: 0.5px; background: #a89de8; }}
  .divider-dot {{ width: 4px; height: 4px; border-radius: 50%; background: #a89de8; }}
  .title {{
    font-size: clamp(24px, 8vw, 28px);
    font-weight: 400;
    color: #333333; 
    margin-bottom: 0.3rem;
  }}
  .title span {{ color: #a89de8; font-weight: 600; }}
  .subtitle {{
    font-size: clamp(11px, 3vw, 12px);
    color: #888888;
    font-family: Helvetica, sans-serif;
    letter-spacing: 0.01em;
  }}
  .chart-section {{
    margin-bottom: 3.5rem;
    opacity: 0;
    animation: fadeIn 0.8s ease forwards;
    animation-delay: 0.4s;
    background: white;
    padding: clamp(1.2rem, 4vw, 1.8rem);
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    transition: all 0.3s ease;
  }}
  .chart-section:hover {{
    box-shadow: 0 8px 20px rgba(168, 157, 232, 0.2);
    transform: translateY(-4px);
  }}
  .chart-number {{
    display: inline-block;
    background: linear-gradient(135deg, #a89de8, #7f77dd);
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    text-align: center;
    line-height: 32px;
    font-weight: 600;
    font-size: 14px;
    margin-bottom: 0.8rem;
    font-family: Helvetica, sans-serif;
  }}
  .chart-label {{
    font-size: clamp(13px, 4vw, 14px);
    font-weight: 600;
    color: #333333;
    font-family: Georgia, serif;
    margin-bottom: 1.2rem;
  }}
  .plotly-chart {{
    width: 100%;
    margin-bottom: 1.2rem;
  }}
  .insight {{
    font-size: clamp(11px, 2.5vw, 12px);
    color: #666666;
    font-family: Helvetica, sans-serif;
    line-height: 1.6;
    border-left: 2.5px solid #a89de8;
    padding: 0.9rem 0.9rem 0.9rem 1rem;
    background: #faf8fb;
    border-radius: 4px;
  }}
  .button-group {{
    display: flex;
    gap: 12px;
    justify-content: center;
    flex-wrap: wrap;
    margin: 2.5rem auto;
  }}
  .btn {{
    display: inline-block;
    padding: clamp(8px, 2vw, 10px) clamp(30px, 6vw, 35px);
    border: none;
    font-size: clamp(10px, 2.5vw, 11px);
    font-family: Helvetica, sans-serif;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    cursor: pointer;
    width: fit-content;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 600;
    transition: all 0.3s ease;
  }}
  .back-btn {{
    background: linear-gradient(135deg, #4fcf9a, #2aaa7a);
    color: white;
  }}
  .back-btn:hover {{ 
    background: linear-gradient(135deg, #2aaa7a, #1a8a5a);
    transform: translateY(-2px);
    box-shadow: 0 3px 10px rgba(79, 207, 154, 0.25);
  }}
  @media (max-width: 768px) {{
    body {{ padding: 2rem 1.2rem; }}
    .header {{ margin-bottom: 2.5rem; }}
    .chart-section {{ margin-bottom: 2.5rem; }}
  }}
  @media (max-width: 480px) {{
    body {{ padding: 1.5rem 1rem; }}
    .header {{ margin-bottom: 2rem; }}
  }}
  @keyframes fadeIn {{ to {{ opacity: 1; }} }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <p class="company">Synent Technologies</p>
    <div class="divider">
      <div class="divider-line"></div>
      <div class="divider-dot"></div>
      <div class="divider-line"></div>
    </div>
    <h1 class="title">Feature <span>Correlation</span></h1>
    <p class="subtitle">Understanding relationships between measurements</p>
  </div>
  <div class="chart-section">
    <div class="chart-number">04</div>
    <p class="chart-label">Feature Correlation Heatmap</p>
    <div class="plotly-chart">{chart4_html}</div>
    <p class="insight">Darker green indicates strong positive correlation. Shows how different measurements are related: for example, petal length and sepal length are highly correlated (0.87), meaning larger flowers tend to have larger both petals and sepals.</p>
  </div>
  <div class="button-group">
    <a href="main.html" class="btn back-btn">Back to Analysis</a>
  </div>
</div>
</body>
</html>'''
with open("compare.html", "w", encoding='utf-8') as f:
    f.write(compare_html_content)
print("compare.html generated successfully!")
insights_html_content = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Insights - The Iris Collection</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { height: 100%; }
  body {
    background: linear-gradient(135deg, #f0f2f0 0%, #e8eae7 100%);
    font-family: Georgia, serif;
    color: #333333;
    padding: 2.5rem 1.5rem;
    min-height: 100vh;
  }
  .container {
    max-width: 800px;
    margin: 0 auto;
    width: 100%;
  }
  .header {
    text-align: center;
    margin-bottom: 3rem;
    opacity: 0;
    animation: fadeIn 0.8s ease forwards;
    animation-delay: 0.2s;
  }
  .company {
    font-size: 10px; letter-spacing: 0.15em;
    text-transform: uppercase; color: #888888;
    font-family: Helvetica, sans-serif;
    margin-bottom: 0.8rem;
    font-weight: 500;
  }
  .divider {
    display: flex; align-items: center; gap: 10px;
    width: 150px; justify-content: center;
    margin: 0 auto 1.2rem;
  }
  .divider-line { flex: 1; height: 0.5px; background: #e07aaa; }
  .divider-dot { width: 4px; height: 4px; border-radius: 50%; background: #e07aaa; }
  .title {
    font-size: clamp(24px, 8vw, 28px);
    font-weight: 400;
    color: #333333;
    margin-bottom: 0.3rem;
  }
  .title span { color: #e07aaa; font-weight: 600; }
  .subtitle {
    font-size: clamp(11px, 3vw, 12px);
    color: #888888;
    font-family: Helvetica, sans-serif;
    letter-spacing: 0.01em;
  }
  .insight-section {
    margin-bottom: 2.5rem;
    opacity: 0;
    animation: fadeIn 0.8s ease forwards;
    background: white;
    padding: clamp(1.2rem, 4vw, 1.8rem);
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    transition: all 0.3s ease;
    border-left: 4px solid #e07aaa;
  }
  .insight-section:nth-child(2) { animation-delay: 0.4s; }
  .insight-section:nth-child(3) { animation-delay: 0.6s; }
  .insight-section:nth-child(4) { animation-delay: 0.8s; }
  .insight-section:nth-child(5) { animation-delay: 1.0s; }
  .insight-section:nth-child(6) { animation-delay: 1.2s; }
  .insight-section:nth-child(7) { animation-delay: 1.4s; }
  .insight-section:hover {
    box-shadow: 0 8px 20px rgba(224, 122, 170, 0.2);
    transform: translateY(-4px);
  }
  .insight-title {
    font-size: 16px;
    font-weight: 600;
    color: #e07aaa;
    margin-bottom: 0.8rem;
    font-family: Georgia, serif;
  }
  .insight-content {
    font-size: 13px;
    color: #666666;
    font-family: Helvetica, sans-serif;
    line-height: 1.7;
  }
  .key-point {
    background: #fef7fa;
    padding: 1rem;
    border-radius: 6px;
    margin-top: 1rem;
    border-left: 3px solid #e07aaa;
    font-size: 12px;
    color: #555555;
  }
  .button-group {
    display: flex;
    gap: 12px;
    justify-content: center;
    flex-wrap: wrap;
    margin: 2.5rem auto;
  }
  .btn {
    display: inline-block;
    padding: clamp(8px, 2vw, 10px) clamp(30px, 6vw, 35px);
    border: none;
    font-size: clamp(10px, 2.5vw, 11px);
    font-family: Helvetica, sans-serif;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    cursor: pointer;
    width: fit-content;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 600;
    transition: all 0.3s ease;
  }
  .back-btn {
    background: linear-gradient(135deg, #4fcf9a, #2aaa7a);
    color: white;
  }
  .back-btn:hover {
    background: linear-gradient(135deg, #2aaa7a, #1a8a5a);
    transform: translateY(-2px);
    box-shadow: 0 3px 10px rgba(79, 207, 154, 0.25);
  } 
  @keyframes fadeIn { to { opacity: 1; } }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <p class="company">Synent Technologies</p>
    <div class="divider">
      <div class="divider-line"></div>
      <div class="divider-dot"></div>
      <div class="divider-line"></div>
    </div>
    <h1 class="title">Key <span>Insights</span></h1>
    <p class="subtitle">Understanding what the data tells us</p>
  </div>
  <div class="insight-section">
    <p class="insight-title"> What Does the Bar Chart Show?</p>
    <p class="insight-content">
      The bar chart compares average measurements for each of the 4 features (sepal length, sepal width, petal length, petal width) across the three species.
    </p>
    <div class="key-point">
      <strong>Key Finding:</strong> Setosa flowers are noticeably smaller than Virginica, with Versicolor in between. This suggests we can use flower size as a distinguishing characteristic between species.
    </div>
  </div>
  <div class="insight-section">
    <p class="insight-title"> What Does the Histogram Show?</p>
    <p class="insight-content">
      The histogram displays the distribution of petal lengths for each species. It shows the frequency (count) of flowers at different petal length ranges.
    </p>
    <div class="key-point">
      <strong>Key Finding:</strong> Setosa petals form a distinct cluster around 1-1.7 cm, while Versicolor and Virginica have much longer petals (3-7 cm) with some overlap. Petal length is an excellent feature for identifying Setosa from the others.
    </div>
  </div>
  <div class="insight-section">
    <p class="insight-title"> What Does the Scatter Plot Show?</p>
    <p class="insight-content">
      The scatter plot visualizes the relationship between sepal length and sepal width, with each species shown in different colors.
    </p>
    <div class="key-point">
      <strong>Key Finding:</strong> Setosa species occupies a distinct region (compact cluster), making it easily separable. Versicolor and Virginica overlap significantly, meaning sepal measurements alone aren't enough to distinguish between them.
    </div>
  </div>
  <div class="insight-section">
    <p class="insight-title"> What Does the Correlation Heatmap Show?</p>
    <p class="insight-content">
      The heatmap shows how strongly features are related to each other. Values close to 1 mean strong positive correlation (both increase together), values close to -1 mean inverse relationship, and values close to 0 mean no relationship.
    </p>
    <div class="key-point">
      <strong>Key Finding:</strong> Petal length and petal width are highly correlated (0.96), as are petal length and sepal length (0.87). This means larger flowers tend to have larger petals AND larger sepals, so these features carry overlapping information.
    </div>
  </div>
  <div class="insight-section">
    <p class="insight-title"> Overall Conclusions</p>
    <p class="insight-content">
      <strong>1. Species Separation:</strong> Setosa is clearly distinct from the other two species across all measurements. Versicolor and Virginica are more similar and harder to distinguish.<br><br>
      <strong>2. Most Useful Features:</strong> Petal length and petal width are the best features for identifying species, especially for separating Setosa from others.<br><br>
      <strong>3. Feature Relationships:</strong> Petal measurements are highly correlated, meaning we don't gain much new information by having both. Sepal width is somewhat independent, providing unique information.<br><br>
      <strong>4. Data Quality:</strong> The dataset shows clear patterns and is well-suited for machine learning classification tasks.
    </p>
  </div>
  <div class="insight-section">
    <p class="insight-title"> Practical Applications</p>
    <p class="insight-content">
      This analysis demonstrates how exploratory data analysis (EDA) helps us understand data before building predictive models. Understanding feature relationships and species differences is crucial for:<br><br>
      ✓ Building effective classification models<br>
      ✓ Choosing the right features for prediction<br>
      ✓ Understanding biological patterns in nature<br>
      ✓ Making data-driven decisions
    </p>
  </div>
  <div class="insight-section">
    <p class="insight-title"> What We Learned</p>
    <p class="insight-content">
      This Iris dataset project demonstrates the complete data science workflow: data loading, cleaning, exploratory analysis, visualization, and interpretation. By examining the data from multiple angles (bar charts, histograms, scatter plots, and correlation matrices), we gained comprehensive insights into the underlying patterns and relationships.
    </p>
    <div class="key-point">
      <strong>Remember:</strong> Good data visualization and analysis skills are as important as machine learning skills in data science!
    </div>
  </div>
  <div class="button-group">
    <a href="main.html" class="btn back-btn">Back to Analysis</a>
  </div>
</div>
</body>
</html>'''
with open("insights.html", "w", encoding='utf-8') as f:
    f.write(insights_html_content)
print("insights.html generated successfully!")
webbrowser.open("file://" + os.path.abspath("main.html"))
