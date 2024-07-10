from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

data_path = "result.csv"
df = pd.read_csv(data_path)
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Soul Foods'),

    html.Div(children='''
        Sales: This is a graph that show the sales of Pink morsels for the past few months
        '''),

    dcc.Graph(
        id = 'line-chart',
        figure = px.line(df, x='date', y='sales')
        )
    ])

#run the app 
if __name__ == '__main__':
    app.run_server(debug=True)
