import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Fake data
df = pd.DataFrame({
    'Item': ['Light', 'Fan', 'Mobile', 'Calculator', 'Ear-Phone'],
    'Sell': [150, 200, 120, 300, 180],
    'Profit': [30, 50, 20, 70, 40],
    'Stock': [20, 15, 30, 10, 25]
})

# Plots
fig1 = px.bar(df, x='Item', y='Sell', title='Sales')
fig2 = px.line(df, x='Item', y='Profit', title='Profit')
fig3 = px.pie(df, names='Item', values='Stock', title='Stock Distribution')

# App setup
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Rafas Dashboard"),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3)
])

if __name__ == '__main__':
    app.run(debug=True)
