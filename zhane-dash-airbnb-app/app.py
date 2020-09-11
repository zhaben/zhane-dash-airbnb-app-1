import dash
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
from plotly import graph_objs as go
from plotly.graph_objs import *
from dash.dependencies import Input, Output, State
import dash_html_components as html

#API Keys and datasets
mapbox_access_token = 'pk.eyJ1IjoiZ29sZGVkaXRpb24yMTIiLCJhIjoiY2tld3dvMGxmMGJsbjM1bXV5cXNjam84cSJ9.32Xt4hp12-2Fa3Rk2XFLgQ'
airbnb_data = pd.read_csv("AB_NYC_2019.csv")


app = dash.Dash(__name__)
server = app.server

# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv("AB_NYC_2019.csv")

#df = df.groupby(['name', 'neighbourhood_group', 'neighbourhood', 'room_type', 'latitude', 'longitude'])[['minimum_nights']].mean()
df.reset_index(inplace=True)
print(df[:5])

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([


        html.H1("Airbnb Dashboard", style={'text-align': 'center'}),
        html.Br(),
        html.H4('Room Type in Map:'),
        dcc.Dropdown(id="slct_room_type",
                     options=[
                         {'label': str(item), 'value': str(item)} for item in df['room_type'].unique()],
                     multi=True,
                     value=list(set(df['room_type'])),  #list(set(df['room_type']))
                     style={'width': "40%"},
                     placeholder="Select a room type"
                     ),

    
        html.H4('Choose Map Region:'),
        dcc.Checklist(id = 'slct_region',
                    options=[
                        {'label': str(item), 'value': str(item)} for item in df['neighbourhood_group'].unique()],
                        value= [item for item in df['neighbourhood_group'].unique()],  #value=list(set(df['neighbourhood_group'])),
                    labelStyle={'display': 'inline-block'}            
                     ),        
#['Brooklyn', 'Manhattan', 'Queens', 'Staten Island', 'Bronx']
        html.Br(),
        html.Div(id='output_container', children=[]),
        html.Br(),
        dcc.Graph(id='airbnb_map', figure={})

    ])

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='airbnb_map', component_property='figure')],
    [Input(component_id='slct_room_type', component_property='value'),
    Input(component_id='slct_region', component_property='value')]
)
        
def update_graph(option_slctd_1, option_slctd_2):
    print(option_slctd_1, option_slctd_2)
    print(type(option_slctd_1), type(option_slctd_2))

    container = ["You're looking for: {} ".format(option_slctd_1),
                 "near {}".format(option_slctd_2)]
    
    dff = df.copy()
    
    df_sub = dff[
        (dff["room_type"].isin(option_slctd_1)) & 
        (dff["neighbourhood_group"].isin(option_slctd_2))]   

    # Plotly Express
    fig = px.scatter_mapbox(df_sub, lat=df_sub["latitude"], lon=df_sub["longitude"], hover_name=df_sub["name"], hover_data=["neighbourhood_group", "neighbourhood", "room_type","price"],
                        color = df_sub["room_type"], color_discrete_map={"Private room":"fuchsia", "Entire home/apt":"goldenrod", "Shared room":"blue"}, zoom=10, height=300)
    fig.update_layout(mapbox_style="dark", mapbox_accesstoken=mapbox_access_token)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        
    fig.update_layout(
            uirevision= 'foo', #preserves state of figure/map after callback activated
            clickmode= 'event+select',
            hovermode='closest',
            hoverdistance=2,   #hover box
            title=dict(text="Where to Stay?",font=dict(size=50, color='green')),
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=25,    #angle of map
                style='dark',
                center=dict(
                    lat=40.80105,
                    lon=-73.945155
                ),
                pitch=40,
                zoom=10
            ))
    
    return container, fig

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=False)




# ########### Initiate the app
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# server = app.server
# app.title=tabtitle

# ########### Set up the layout
# app.layout = html.Div(children=[
#     html.H1(myheading),
#     dcc.Graph(
#         id='flyingdog',
#         figure=beer_fig
#     ),
#     html.A('Code on Github', href=githublink),
#     html.Br(),
#     html.A('Data Source', href=sourceurl),
#     ]
# )

# if __name__ == '__main__':
#     app.run_server()
