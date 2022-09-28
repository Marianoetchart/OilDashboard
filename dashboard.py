from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

app = Dash(__name__)

df_wti = pd.read_csv("C:\\Users\\maria\\Documents\\VSCodeProjects\\Oil Dashboard\\FUTURE_US_XNYM_CL.csv")
df_brent = pd.read_csv("C:\\Users\\maria\\Documents\\VSCodeProjects\\Oil Dashboard\\FUTURE_UK_IFEU_BRN.1.csv")

app.layout = html.Div(children=[
    html.H1(children='Oil Front Month Dashboard'),

    html.Div(children='''
        Select Crude Oil: 
    '''),

    dcc.Dropdown(id='dropdown', options=[
            {'label': 'WTI', 'value': 'wti'},
            {'label': 'Brent', 'value': 'brent'}],
            value = 'brent'),

    dcc.Graph(id='generic-graph')
])


@app.callback(Output('generic-graph', 'figure'), 
              [Input('dropdown', 'value')])
def update_figure(selected_value):
    if selected_value == 'wti':
        x, y = df_wti['Date'], df_wti['Close']
    if selected_value == 'brent':
         x, y = df_brent['Date'], df_brent['Close']

    fig = go.Figure([go.Scatter(x = x, y = y,\
                     line = dict(color = 'firebrick', width = 4), name = 'Front Month Close')
                     ])
    
    fig.update_layout(title = 'Front Month Close Prices',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)