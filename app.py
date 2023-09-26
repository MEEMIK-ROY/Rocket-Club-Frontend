# 1. Import Dash
import dash
from dash import Dash, html, callback, Output, Input
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
    # Add columns here @Jayanta
    html.H1("Jayanta")
],className="row3")

container = html.Div([
    row1,
    row2,
    row3
])
app.layout = dbc.Container(container, fluid=True)

# 5. Start the Dash server
if __name__ == "__main__":
    app.run_server()