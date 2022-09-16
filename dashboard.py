from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)


df = pd.read_csv("C:\\Users\\maria\\Documents\\VSCodeProjects\\Oil Dashboard\\FUTURE_US_XNYM_CL.csv")

fig = go.Figure([go.Scatter(x = df['Date'], y = df['Close'],\
                     line = dict(color = 'firebrick', width = 4), name = 'Close Front Month')
                     ])
fig.update_layout(title = 'WTI Front Month Close Prices vs US Oil Storage',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)