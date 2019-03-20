from plotly.graph_objs import Bar
from plotly.graph_objs import Figure
from plotly.graph_objs import Histogram
from plotly.graph_objs import Layout
from plotly.graph_objs import Scatter
import datetime


def differences(days):
    data = [
        Bar(
            x=[day.date for day in days],
            y=[day.overtime.total_seconds() / 3600 for day in days],
            name="overtime",
        ),
        Bar(
            x=[day.date for day in days],
            y=[day.minus_hours.total_seconds() / 3600 for day in days],
            name="minus hours",
        ),
        Bar(
            x=[day.date for day in days],
            y=[0 for day in days],
            showlegend=False,
            text=[day.remark for day in days],
            textposition="outside",
        ),
    ]

    layout = Layout(
        title="Overtime / Minus hours",
        barmode="stack",
        xaxis={"title": "Date"},
        yaxis={"title": "Worktime difference (in Hours)"},
    )

    return dict(data=data, layout=layout)


def histograms(days):
    data = [
        Histogram(
            x=[
                day.overtime.total_seconds() / 3600
                for day in days
                if day.overtime > datetime.timedelta()
            ],
            name="overtime",
            xbins={"size": 0.25},
            opacity=0.75,
        ),
        Histogram(
            x=[
                day.minus_hours.total_seconds() / 3600
                for day in days
                if day.minus_hours < datetime.timedelta()
            ],
            name="minus hours",
            xbins={"size": 0.25},
            opacity=0.75,
        ),
    ]

    layout = Layout(
        title="Overtime / Minus hours",
        xaxis={"title": "Overtime / Minus hours"},
        yaxis={"title": "Occurrences (in days)"},
        barmode="overlay",
    )

    return dict(data=data, layout=layout)


def integrated(days):
    integrated = []
    total = datetime.timedelta()

    for day in days:
        total += day.overtime + day.minus_hours
        integrated.append(datetime.timedelta(seconds=total.total_seconds()))

    data = [
        Scatter(
            x=[day.date for day in days],
            y=[total.total_seconds() / 3600 for total in integrated],
            name="overtime / minus hours",
        )
    ]

    layout = Layout(
        title="Total overtime / minus hours",
        xaxis={"title": "Date"},
        yaxis={"title": "Integrated time difference (in hours)"},
    )

    return dict(data=data, layout=layout)
