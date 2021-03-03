import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd

from liveSport import *
from utils import *

roundGap=10
ls=liveSeason()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(id='timeRemaining', children=''),
    dcc.Interval(id='match-interval',interval=roundGap*1000,n_intervals=0),
    dcc.Interval(id='countdown-interval',interval = 1*1000,n_intervals=0),
    html.Div(className='row', children=[
        html.Div(dt.DataTable(id='latestPoints'),className='two columns'),
        html.Div(dcc.Graph(id='graph-of-rankings'),className='ten columns')
    ]),
    html.H1(id='resultsHeader', children='Latest Results:'),
    dt.DataTable(id='latestResults')
])

@app.callback(Output('timeRemaining', 'children'),
              Input('countdown-interval', 'n_intervals'))
def countdownUpdate(n):
    return 'Time until next round: '+str(roundGap-(n%roundGap))+'s'


@app.callback(
    [Output('latestResults','columns'),
    Output('latestResults','data')],
    Input('match-interval','n_intervals'),
    prevent_initial_call=True
)
def nextStep(n):
    ls.playSeason()
    columnNames=["Round", "Match","player1_id","player1_rnkPoints","player1_perform","player2_id","player2_rnkPoints","player2_perform","winner_id"]
    res = pd.DataFrame(ls.currentTourn.matchRec, columns=columnNames)
    res = res[res['Round']==max(res['Round'])].to_dict('records')
    columnNames = [{'name': col, 'id': col} for col in columnNames]
    return columnNames, res

@app.callback(
    Output('graph-of-rankings','figure'),
    Input('match-interval','n_intervals'),
    prevent_initial_call=True)
def plotRankings(n):
    if ls.currentTournComplete:
        fig = px.line(ls.playerSum.set_index("name").T[2:],labels={
                     "index": "Tournament",
                     "value": "Ranking points",
                     "name": "Player"
                 })
        return fig
    else:
        return dash.no_update
    
@app.callback(
    [Output('latestPoints','columns'),
    Output('latestPoints','data')],
    Input('graph-of-rankings','figure'),
    prevent_initial_call=True)
def rankingTableUpdate(n):
    df = ls.playerSum.iloc[:,[0,-1]]
    df.rename(dict(zip(df.columns,["player",'points'])), axis='columns',inplace=True)
    df.sort_values(axis=0,by='points',ascending=False,inplace=True)
    columnNames = [{'name': col, 'id': col} for col in df.columns]
    return columnNames, df.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
