# 1. Import Dash
import dash
from dash import Dash, html, callback, Output, Input,dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import random

# 2. Create a Dash app instance
styleCss = "./assets/styles.css"
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,styleCss])

row1= dbc.Row([
    # Add columns here @Chaitanya
    html.H1("Chaitanya")
],class_name="row1")


row2 = dbc.Row([
    dbc.Col(dbc.Card([
         html.Video(
            controls = True,
            id = 'movie_player',
            src = "https://www.w3schools.com/html/mov_bbb.mp4",
            autoPlay=True
        )
    ]),width=6,class_name="videoCard"),
    dbc.Col(dbc.Card([
        dcc.Graph(id="live-chart", animate=True),
        dcc.Interval(id="interval-component", interval=1000, n_intervals=0),
    ]),width=6,class_name="chartCard")
],class_name="row2")


row3=dbc.Row([
    # Add columns here @Jayanta
    html.H1("Jayanta")
],className="row3")

container = html.Div([
    row1,
    row2,
    row3
])
app.layout = dbc.Container(container, fluid=True)




#Event Listener section

@callback(
    Output('live-chart','figure'),
    [Input('interval-component','n_intervals')]
)
def update_chart(n):
    x_data = list(range(10))
    y_data = [random.randint(0,100) for i in range(10)]

    trace = go.Scatter(
        x=x_data,
        y=y_data,
        mode='lines+markers',
        name='Live Chart',
        line={'color':'blue'},
        marker={'color':'red'},
    )

    layout = go.Layout(
        title="Live Chart",
        xaxis=dict(range=[0,10]),
        yaxis=dict(range=[0,100]),
    )

    return {"data": [trace], "layout": layout}
# 5. Start the Dash server
if __name__ == "__main__":
    app.run_server()