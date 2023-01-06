from dash import Dash,html,dcc,Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px



app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

data = pd.read_csv(r'E:\Dataset\IRIS.csv')
lis = list(data.columns)
lis.remove('species')


app.layout = html.Div([
    html.H1('Demo Dash'),
    dbc.Row([
        dbc.Col([
                html.Div([
                         dcc.Dropdown(lis,lis[0],id='mydrop')
                ],style={
                    'width':'400px'
                })
        ]),
        dbc.Col([
                   html.Div([
                              dcc.Dropdown(lis,lis[1],id='mydrop1')
                   ],style={
                    'width':'400px',
                    'margin-left':'300px'
                })
        ])
    ],style={
        'display':'flex'
    }),
   
   

   dbc.Row([

        dbc.Col([ 
                      dcc.Graph(id='my-graph',style={
                        'width':'100%'
                      })
        ]),
        dbc.Col([ 
                           dcc.Graph(id='my-graph1',style={
                            'width':'100%'
                           })
        ])
   ],style={
    'display':'flex'
   })
   
    
])




@app.callback(
    [Output('my-graph','figure'),
    Output('my-graph1','figure')
    ],
            [Input('mydrop','value'),
            Input('mydrop1','value')
            ]
)
def update(val1,val2):

    df = pd.read_csv(r'E:\Dataset\IRIS.csv')

    fig = px.scatter(df,x=val1,y=val2,color='species')

    fig1 = px.scatter_3d(df, x=val1, y=val2, z='petal_width',
              color='species')

    return fig,fig1
        

if __name__ == '__main__':
       app.run_server(debug = True)
