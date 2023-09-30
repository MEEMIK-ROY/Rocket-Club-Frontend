# 1. Import Dash
import dash
from dash import Dash, html, callback, Output, Input,State, dcc
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
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        html.H4('Enter the ignition code',className='text-dark'),
                        dbc.Input(id='code',placeholder='Enter the code',type='password'),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('Submit',id='submit',color='primary',className='mt-3 d-block m-auto')
                        ],width=6),
                        dbc.Col([
                            dbc.Button('Retract',id='retract',color='primary',className='mt-3 d-block m-auto')
                        ],width=6)
                    ])
                    
                ],className='d-block m-auto w-20 border border-dark rounded-5')
            ],class_name="border-0",inverse=True)
        ],width=12)
    ],className='mt-5')

row4=dbc.Row([
        dbc.Col([
            html.H3('Status: ',id='status',className='mt-5')
        ],width=6)
    ])


container = html.Div([
    row1,
    row2,
    row3,
    row4
])
app.layout = dbc.Container(container, fluid=True)




#Event Listener section
@app.callback(
    Output('status','children'),
    Input('submit','n_clicks'),
    State('code','value')
)
def update_status(n_clicks,code):
    if n_clicks is None:
        return ''
    elif code == '1234':
        return 'Rocket launched'
    else:
        return 'Error'
    
# @callback(
#     Output('live-chart','figure'),
#     [Input('interval-component','n_intervals')]
# )
# def update_chart(n):
#     x_data = list(range(10))
#     y_data = [random.randint(0,100) for i in range(10)]

#     trace = go.Scatter(
#         x=x_data,
#         y=y_data,
#         mode='lines+markers',
#         name='Live Chart',
#         line={'color':'blue'},
#         marker={'color':'red'},
#     )

#     layout = go.Layout(
#         title="Live Chart",
#         xaxis=dict(range=[0,10]),
#         yaxis=dict(range=[0,100]),
#     )

#     return {"data": [trace], "layout": layout}
# run app
if __name__ == '__main__':
    app.run_server(debug=True)
