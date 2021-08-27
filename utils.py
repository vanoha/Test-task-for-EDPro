import dash_html_components as html
import dash_core_components as dcc

import plotly.graph_objs as go

import pandas as pd
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()




def Header(app):
    return html.Div([get_header(app), html.Br([])])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [html.H5("⁣")]
                    ),
                    html.Div(
                        [html.H5("Данные об эмоциях слушателей")],
                        className="seven columns main-title",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"}
            ),
        ],
        className="row",
    )
    return header


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    k = 0
    j = 0
    html_row1 = []
    for i in df.keys():
        j += 1
        if j == 6:
            break
        html_row1.append(html.Td(html.B([i])))
    table.append(html.Tr(html_row1))
    for index, row in df.iterrows():
        html_row = []
        k += 1
        if k == 4:
            break
        j = 0
        for i in range(len(row)):
            j += 1
            if j == 6:
                break
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

