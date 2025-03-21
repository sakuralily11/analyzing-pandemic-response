import dash
import sqlite3
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/dataset', name='Dataset', title='Dataset', id='dataset-link')

# Get content for page
con = sqlite3.connect("assets/content.db")
cur = con.cursor()
res = cur.execute("SELECT page_content FROM content where page_id=\'dataset-link\'")
dataset_md = res.fetchall()[0][0]

layout = dbc.Container([
    dbc.Col([], width=2),
    dbc.Col([
        dbc.Row([
            dcc.Markdown(dataset_md, mathjax=True)
        ])
    ], width = 8),
    dbc.Col([], width=2),
])
