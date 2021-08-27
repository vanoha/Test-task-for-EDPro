import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


emotions = pd.read_csv(DATA_PATH.joinpath("emotions.csv"))
surveys_df = pd.read_csv(DATA_PATH.joinpath("sur.csv"), encoding='cp1251')


def showPie():
    emotion = {}
    cols = surveys_df.columns
    st = []
    for i in surveys_df[cols[10]]:
        st = i.split(";")
        for j in st:
            if j in emotion:
                emotion[j] += 1
            else:
                emotion[j] = 1
    fig = go.Figure()
    fig.add_trace(go.Pie(values=list(emotion.values()),
                         labels=list(emotion.keys()),
                         hole=0.6,
                         ))
    fig.update_layout(
        annotations=[{"text": 'Эмоции <br> слушателей', "x": 0.5, "y": 0.5, "font_size": 20, "showarrow": False}])
    return fig


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Проблемы данных"),
                                    html.Br([]),
                                    html.P(
                                        "В датасете surveys обнаружены следующие проблемы: ",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                    html.P(
                                        "1) В столбце 'Видели ли вы ролик...' присутствует одно значение NaN. "
                                        "Предложение по решению: так как оно одно, то его удаление не сильно повлияет "
                                        "на общую картину данных. ",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                    html.P(
                                        "2) В датасете присутствуют столбцы с данными типа: 'Да', 'Нет', 'Затрудняюсь "
                                        "ответить'. С текстовым типом данных довольно трудно работать (особеннно "
                                        "невозможно, если строить модель машинного обучения на этом столбце). "
                                        "Предложение по решению: заменить эти слова на числа типа int (это сделано "
                                        "выше). ",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                    html.P(
                                        "3) Со столбцом 'Укажите ваш пол' та же ситуация, что и выше. Решение такое "
                                        "же (сделано). ",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                    html.P(
                                        "4) Столбец 'Отметка времени' не несет какой-либо полезной информации для "
                                        "последующей работы с данными. Поэтому предпроложительно его можно удалить. ",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                    html.P(
                                        "5) Для данного датасета можно построить корреляционную матрицу и посмотреть, "
                                        "как столбцы влияют друг на друга. Далее в предобработке данных можно "
                                        "выяснить, стоит ли удалять некоторые столбцы. Если корреляция двух столбцов "
                                        "около '1', то один из них можно вполне удалить.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                    html.P(
                                        "В датасете emotions в столбцах эмоций могут быть выбросы. Существует "
                                        "эвристика, по которой выбросами считаются значения, входящие в 5% крайних с "
                                        "обеих сторон процентов ранжированной выборки. Поэтому Однако в первые 5% во "
                                        "всех столбцах входят только значения равные 0. Человек может выражать полное "
                                        "отсутствие счастья (например), когда слушает музыкальную дорожку, "
                                        "поэтому я бы не стал удалять строки со значениями 0 в этих столбцах.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Эмоции слушателей"],
                                        className="subtitle padded",
                                    ),
                                    html.Table(make_dash_table(emotions)),
                                ],
                                className="h",
                            ),
                        ]
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Таблица опроса слушателей"],
                                        className="subtitle padded",
                                    ),
                                    html.Table(make_dash_table(surveys_df)),
                                ],
                                className="h",
                            ),
                        ]
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Какие эмоции возникают у наших слушателей",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure=showPie(),
                                        config={"displayModeBar": False},
                                    ),
                                ],
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
