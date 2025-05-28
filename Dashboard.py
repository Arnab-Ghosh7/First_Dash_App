import pandas as pd
import dash
import plotly.graph_objs as go
from dash import html, dcc

# Load data
data = pd.read_csv('gapminder.csv')


# Create Dash app
app = dash.Dash(__name__)  # Correct and modern way

# Define layout properly as a component tree
app.layout = html.Div([
    html.Div(children=[
        html.H1("My First Dashboard", style={'color':'blue','text-align':'center', 'margin': '5px',
            'padding': '5px',
            'fontWeight': 'bold'})

    ], style={'border':'1px black solid', 'float':'left', 'width':'100%', 'height':'50px'}),

    html.Div(children=[
        dcc.Graph(id='box-plot',
                  figure={'data':[go.Box(x=data['aged_15_24_employment_rate_percent'])],'layout':go.Layout(title="Boxplot")})
    ],style={'border':'1px black solid', 'float':'left', 'width':'99.8%'})
])

# Run the server
if __name__ == '__main__':
    app.run(debug=True)


