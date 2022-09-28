from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

app = Dash(__name__)

start_date = "09/15/2021%2000:00:00"
end_date = "09/27/2022%2023:59:59"
date_range = "d30"
freq = "p1d"

url = "https://www.marketwatch.com/investing/future/{}/downloaddatapartial?startdate={}&enddate={}&daterange={}&frequency={}&csvdownload=true&downloadpartial=false&newdates=false".format(
    '{key}',
    start_date, 
    end_date,
    date_range,
    freq
)

wti_url = url.format(key = "cl.1")
brent_url = url.format(key = "brn.1") +  "&countrycode=uk"

df_wti = pd.read_csv(wti_url)
df_brent = pd.read_csv(brent_url)

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