# -*- coding: utf-8 -*-
"""
97110 - Afonso Ferreira 

"""

import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


def generate_table(dataframe, max_rows=30):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

energy_all=pd.read_csv('energy_all.csv')
energy_final=pd.read_csv('energy_final.csv')
raw_data_meteo=pd.read_csv('raw_data_meteo.csv')
IST_meteo_data_2017_2018_2019=pd.read_csv('IST_meteo_data_2017_2018_2019.csv')
IST_Central_Pav_2017_Ene_Cons=pd.read_csv('IST_Central_Pav_2017_Ene_Cons.csv')
IST_Central_Pav_2018_Ene_Cons=pd.read_csv('IST_Central_Pav_2018_Ene_Cons.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Img(src=app.get_asset_url('IST_logo.png')),
    html.H2('97110 - Afonso Ferreira'),
    dcc.Tabs(id='tabs', value='tab1', children=[
        dcc.Tab(label='Dados em Estudo', value='tab6'),
        dcc.Tab(label='Gráficos', value='tab1'),
        dcc.Tab(label='Final Data', value='tab2'),
        dcc.Tab(label='Clustering', value='tab3'),
        dcc.Tab(label='Feature Selection', value='tab4'),
        dcc.Tab(label='Regression and Error Methods', value='tab5')
        
        
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))

def render_content(tab):
    if tab == 'tab1':
        return html.Div([
            html.H3('Gráficos'),
            dcc.RadioItems(
        id='radio',
        options=[
            {'label': 'Gráfico da Temperatura ao longo do tempo', 'value': 1},
            {'label': 'Gráfico da Humidade Relativa ao longo do tempo', 'value': 2},
            {'label': 'Gráfico da Velocidade do Vento ao longo do tempo', 'value': 3},
            {'label': 'Gráfico da Velocidade Instantânea do Vento ao longo do tempo', 'value': 4},
            {'label': 'Gráfico da Pressão ao longo do tempo', 'value': 5},
            {'label': 'Gráfico da Radiação Solar ao longo do tempo', 'value': 6},
            {'label': 'Gráfico da Chuva ao longo do tempo', 'value': 7},
            {'label': 'Gráfico da Potência ao longo do tempo', 'value': 8},
            {'label': 'Gráfico da Potência ao longo do tempo %25', 'value': 9}            
        ], 
        value=1
        ),
        html.Div(id='data_preparation'),
                    ])
    
    elif tab == 'tab6':
        return html.Div([
            html.H3('Dados em Estudo'),
            dcc.RadioItems(
        id='dropdown0',
        options=[
            {'label': 'IST_meteo_data_2017_2018_2019', 'value': 1},
            {'label': 'IST_Central_Pav_2017_Ene_Cons.csv', 'value': 2},
            {'label': 'IST_Central_Pav_2018_Ene_Cons.csv', 'value': 3},
        ], 
        value=1
        ),
        html.Div(id='dados1234'),
                    ])
               
    elif tab == 'tab2':
        return html.Div([
            html.H3('Final Data'),
            dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Dados Arranjados', 'value': 1}
                    ], 
        value=1
        ),
        html.Div(id='final_data'),
                    ])
    
    elif tab == 'tab3':
        return html.Div([
            html.H3('Clustering'),
            dcc.RadioItems(
        id='radio2',
        options=[
            {'label': 'Elbow Curve', 'value': 1},
            {'label': 'Cluster Gráfico_Chuva em função da humidade relativa', 'value': 2},
            {'label': 'Cluster Gráfico_Radiação Solar em função da humidade relativa', 'value': 3},
            {'label': 'Cluster Gráfico_Temperatura em função da chuva', 'value': 4},
            {'label': 'Cluster Gráfico_Temperatura em função da humidade relativa', 'value': 5},
            {'label': 'Cluster Gráfico_Temperatura em função da radiação solar', 'value': 6},
            {'label': 'Cluster Gráfico_Velocidade do vento em relação às rajadas de vento', 'value': 7}
          
        ], 
        value=1
        ),
        html.Div(id='Cluster_id'),
                    ])
    
    elif tab == 'tab4':
        return html.Div([
            html.H3('Feature Selection'),
            dcc.Dropdown(
        id='dropdown2',
        options=[
            {'label': 'Kbest', 'value': 1},
            {'label': 'RFE', 'value': 2},
            {'label': 'Emsemble', 'value': 3},
         ], 
          value=1
        ),
        html.Div(id='feature_selection'),
                    ])
    
    elif tab == 'tab5':
        return html.Div([
            html.H3('Regression and Error Methods'),
      dcc.RadioItems(
        id='Radio3',
        options=[
            {'label': 'Linear Regression', 'value': 1},
            {'label': 'Support Vector Regressor', 'value': 2},
            {'label': 'Decision Tree Regressor', 'value': 3},
            {'label': 'Random forest', 'value': 4},
            {'label': 'Uniformized data', 'value': 5},
            {'label': 'Gradient Boosting', 'value': 6},
            {'label': 'Bootstrapping', 'value': 7},
            {'label': 'Neural Networks', 'value': 8}
        
        ], 
        value=1
        ),
        html.Div(id='regression'),
                    ])
    
@app.callback(Output('data_preparation', 'children'), 
             Input('radio', 'value'))

def render_figure_png(radio_year):
    
    if radio_year == 1:
        return html.Div([html.H3('Gráfico da temperatura ao longo do tempo'),html.Img(src='assets/Gráfico_Temperatura_ao_Longo_do_Tempo.PNG'),])
    elif radio_year == 2:
        return html.Div([html.Img(src='assets/grafico da humidade relativa ao longo do tempo.PNG'),])
    elif radio_year == 3:
        return html.Div([html.Img(src='assets/Grafico da velocidade do vento ao longo do tempo.PNG'),])
    elif radio_year == 4:
        return html.Div([html.Img(src='assets/Grafico da velocidade instantanea do vento ao longo do tempo.PNG'),])
    elif radio_year == 5:
        return html.Div([html.Img(src='assets/Gráfico da pressao ao longo do tempo.PNG'),])
    elif radio_year == 6:
        return html.Div([html.Img(src='assets/Gráfico da Radiação Solar ao longo do tempo.PNG'),])
    elif radio_year == 7:
        return html.Div([html.Img(src='assets/Gráfico da chuva ao longo do tempo.PNG'),])
    elif radio_year == 8:
        return html.Div([html.Img(src='assets/Gráfico da Potência ao longo do tempo.PNG'),])
    elif radio_year == 9:
        return html.Div([html.Img(src='assets/Gráfico da Potência ao longo do tempo (%25).PNG'),]),
   
    
@app.callback(Output('dados1234', 'children'), 
             Input('dropdown0', 'value'))

def render_figure_png(dados_estudo):
    
    if dados_estudo == 1:
        return generate_table(IST_meteo_data_2017_2018_2019)
    elif dados_estudo == 2:
        return generate_table(IST_Central_Pav_2017_Ene_Cons)
    elif dados_estudo == 3:
        return generate_table(IST_Central_Pav_2018_Ene_Cons)
   
  
@app.callback(Output('final_data', 'children'), 
             Input('dropdown', 'value'))

def render_figure_png(dropdown_year):
    
    if dropdown_year == 1:
        return html.Div(children=[
    dcc.Graph(
        id='final_data',
        figure={
            'data': [
                {'x': energy_final['Date'], 'y': energy_final['Power_kW'], 'type': 'line', 'name': 'Power'},
                {'x': energy_final['Date'], 'y': energy_final['temp_C'], 'type': 'line', 'name': 'Temperature'},
                {'x': energy_final['Date'], 'y': energy_final['solarRad_W/m2'], 'type': 'line', 'name': 'Radiação Solar'},
            ],
        }
    ),
])   


@app.callback(Output('Cluster_id', 'children'), 
             Input('radio2', 'value'))

def render_figure_png(cluster_1):
    
    if cluster_1 == 1:
        return html.Div([html.Img(src='assets/Elbow Curve.PNG'),])
    elif cluster_1 == 2:
        return html.Div([html.Img(src='assets/Cluster Gráfico_Chuva em função da humidade relativa.PNG'),])
    elif cluster_1 == 3:
        return html.Div([html.Img(src='assets/Cluster Gráfico_Radiação Solar em função da humidade relativa.PNG'),])
    elif cluster_1 == 4:
        return html.Div([html.Img(src='assets/Cluster Gráfico_Temperatura em função da chuva.PNG'),])
    elif cluster_1 == 5:
        return html.Div([html.Img(src='assets/Cluster Gráfico_Temperatura em função da humidade relativa.PNG'),])
    elif cluster_1 == 6:
        return html.Div([html.Img(src='assets/Cluster Gráfico_Temperatura em função da radiação solar.PNG'),])
    elif cluster_1 == 7:
        return html.Div([html.Img(src='assets/Cluster Gráfico_Velocidade do vento em relação às rajadas de vento.PNG'),])


@app.callback(Output('feature_selection', 'children'), 
             Input('dropdown2', 'value'))

def render_figure_png(feature_1):
    
    if feature_1 == 1:
        return html.Div(html.H3('KBest: Foram selecionados como melhores parametros do Kbest: a temperatura, a radiação e a potência na hora anterior'),)
    elif feature_1 == 2:
        return html.Div(html.H3('RFE: Foram selecionados como melhores parametros do RFE: a velocidade do vente, as rajadas e os feriados'),)
    elif feature_1 == 3:
        return html.Div(html.H3('Emsemble: Foram selecionados como melhores parametros do Emsemble: a hora do dia'),)
   

@app.callback(Output('regression', 'children'), 
             Input('Radio3', 'value'))

def render_figure_png(regression_1):
    
    if regression_1 == 1:
        return html.Div([html.Img(src='assets/LinearRegression1.PNG'),html.Img(src='assets/LinearRegression2.PNG'),html.H3('MAE_LR=17.99;     MSE_LR=578.45;       RMSE_LR= 24.05;      cvRMSE_LR=0.1144')])
    elif regression_1 == 2:
        return html.Div([html.Img(src='assets/Support Vector Regressor 1.PNG'),html.Img(src='assets/Support Vector Regressor 2.PNG'),html.H3('MAE_LR=9.99;     MSE_LR=213.29;       RMSE_LR= 16.60;      cvRMSE_LR=0.07')])
    elif regression_1 == 3:
        return html.Div([html.Img(src='assets/Decision Tree Regressor 1.PNG'),html.Img(src='assets/Decision Tree Regressor 2.PNG'),html.H3('MAE_LR=10.14;     MSE_LR=235.03;       RMSE_LR= 15.33;      cvRMSE_LR=0.07')])
    elif regression_1 == 4:
        return html.Div([html.Img(src='assets/Random Forest 1.PNG'),html.Img(src='assets/Random Forest 2.PNG'),html.H3('MAE_LR=8.14;     MSE_LR=152.19;       RMSE_LR= 12.34;      cvRMSE_LR=0.059')])
    elif regression_1 == 5:
        return html.Div([html.Img(src='assets/Uniformized Data 1.PNG'),html.Img(src='assets/Uniformized Data 2.PNG'),html.H3('MAE_LR=8.97;     MSE_LR=179.5;       RMSE_LR= 13.4;      cvRMSE_LR=0.06')])
    elif regression_1 == 6:
        return html.Div([html.Img(src='assets/Gradient Boosting 1.PNG'),html.Img(src='assets/Gradient Boosting 2.PNG'),html.H3('MAE_LR=8.13;     MSE_LR=144.8;       RMSE_LR= 12.03;      cvRMSE_LR=0.057')])
    elif regression_1 == 7:
        return html.Div(html.H3('MAE_LR=7.85;     MSE_LR=141.54;       RMSE_LR= 11.89;      cvRMSE_LR=0.05'))
    elif regression_1 == 8:
        return html.Div([html.Img(src='assets/Neural Networks 1.PNG'),html.Img(src='assets/Neural Networks 2.PNG'),html.H3('MAE_LR=13.47;     MSE_LR=383.83;       RMSE_LR= 19.59;      cvRMSE_LR=0.09')]),
    

if __name__ == '__main__':
    app.run_server(debug=True)
