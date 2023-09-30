# 1. Import Dash
import dash
from dash import Dash, html, callback, Output, Input,State
import dash_bootstrap_components as dbc

# 2. Create a Dash app instance
styleCss = "./assets/styles.css"
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,styleCss])

row1= dbc.Row([
    # Add columns here @Chaitanya
    html.H1("Chaitanya")
],class_name="row1")
row2 = dbc.Row([
    # Add columns here @Meemik
    html.H1("Meemik")
],class_name="row2")




row3=dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Enter the ignition code',className='text-dark'),
                    dbc.Input(id='code',placeholder='Enter the code',type='password'),
                    dbc.Button('Submit',id='submit',color='primary',className='mt-3 d-block m-auto')
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
    
# run app
if __name__ == '__main__':
    app.run_server(debug=True)
