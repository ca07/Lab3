#
# app.py
#

import dash
from dash import dcc
from dash import html
from pandas.io.formats import style
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import matplotlib.pyplot as plt
# from scipy import stats

# Calling the data wrangling program, "calculated" is a dummy variable
from mortality_rates import calculated

app = dash.Dash(__name__)

# Loads the final csv-file from the data-wrangling program
df = pd.read_csv("rel_mortality_df.csv", delimiter=';')

#colors = {"background": "#f8f9fe", "text": "#011833"}

app.layout = html.Div([
    html.H1(
        "Mortality Rates per 100,000 Population and Year"
    ),
    html.Div([
        html.Label("Choose Sex"),
        dcc.Dropdown(
            id = "sex-dropdown",
            options = [
                {"label": s, "value": s} for s in df.Sex.unique()
            ],
            value = "all",
            className = "dropdown"
        ),
        dcc.Graph(
            id = "mortality",
            className = "chart",
        )
    ])
])

@app.callback(
    Output("mortality", "figure"),
    Input("sex-dropdown", "value")
)

def update_graph(selected_sex):
    df_selection = df[df.Sex == selected_sex].reset_index().drop(columns = ['index'])
    
    fig = px.scatter(
        df_selection,
        x = "Year",
        y = "Mortality",
        hover_name = "Mortality",
        trendline="ols",
        log_x = True,
        size_max = 60
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
    