from dash import Dash, html, dcc, callback, Output,Input
import plotly.express as px
import pandas as pd

data_path = "result.csv"
df = pd.read_csv(data_path)
app = Dash(__name__)
options =[ 
          {'label': 'All', 'value': 'all'},
          {'label': 'North', 'value': 'north'},
          {'label': 'South', 'value': 'south'},
          {'label': 'East' , 'value': 'east'},
          {'label': 'West' , 'value': 'west'}
          ]

app.layout = html.Div(
        style={
            "fontFamily":"Arial, sans-serif",
            "margin": "0 auto",
            "padding": "20px",
            "maxWidth": "800px",
            },
        children=[
            html.H1(children='Soul Foods'),

    html.P(
    "Sales: This is a graph that show the sales of Pink morsels for the past few months",
    style={
               "fontsize": "18px",
               "textAlign": "center"},
           ),
    dcc.Graph(
        className = 'graph',
        id = 'line-chart',
        figure = px.line(df, x='date', y='sales'),
        style={
            "border": "2px solid #4CAF50",
            "borderRadius": "8px",
            "padding": "10px",
            "backgroundColor": "#f9f9f9",
            },
        ),
    html.Div(
        [
            html.Label(
                "Choose a Region:",
                style={"fontSize": "16px",
                       "marginBottom": "8px"
                       },
            ),
            dcc.RadioItems(
                options=[
                    {'label': 'All', 'value': 'all'},
                    {'label': 'North', 'value': 'north'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'East' , 'value': 'east'},
                    {'label': 'West' , 'value': 'west'}
                ],
                value='all',  # Initial selected value
                inline=True,  # Display options horizontally
                id = 'location',
                className = 'radio',
                labelStyle={
                    "display": "block",
                    "padding": "5px",
                    "cursor": "pointer",
                    },
                style={
                    "marginTop": "10px",
                    "fontSize": "16px"},
            ),
        ]),
    ])
@callback(
        Output('line-chart', 'figure'),
        Input('location','value')
 )
def update_graph(location):
    if location == 'all':
        figure = px.line(df, x = 'date', y = 'sales')
    else:
        filtered_df = df[df['region'] == location]  
        figure = px.line(filtered_df, x='date', y='sales')

    return figure
        


#run the app 
if __name__ == '__main__':
    app.run_server(debug=True)
