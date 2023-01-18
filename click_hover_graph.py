from dash import Dash,html,dcc,Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import json




app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

data = px.data.tips()

print(data.head())

fig = px.pie(data, values='tip', names='day')


app.layout = html.Div([

    dbc.Row([
      
          dbc.Col([
                           dcc.Graph(id='pie',figure=fig,style={
                            'width':'600px',
                            'height':'400px'
                           })      
          ]),

          dbc.Col([
                    dcc.Graph(id='bar',style={
                            'width':'600px',
                            'height':'400px'
                           })
          ])

          ],style={
            'display':'flex'
          })
       
])


@app.callback(
    Output('bar','figure'),
    Input('pie','hoverData')
)
def update(val):
         data = px.data.tips()
         if val is not None:
                         day = val['points'][0]['label']
                         mask = data['day']==day
                         new_data = data[mask]
                         fig1 = px.bar(new_data, x='sex', y='size',color='smoker')
                         return fig1


         else:
             raise PreventUpdate

        

if __name__ == '__main__':
       app.run_server(debug = True)
