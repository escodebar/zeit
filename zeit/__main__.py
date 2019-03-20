from datetime import date
from glob import glob
from pathlib import Path
from plotly.offline import plot
from plotly.tools import make_subplots
from zeit.plots import differences
from zeit.plots import histograms
from zeit.plots import integrated
from zeit.reader import file_reader
import click
import dotenv
import plotly.graph_objs as go
import os


@click.command()
@click.option(
    "--data-path",
    default=os.getcwd(),
    help="The path to the directory with the data and the environment variables.",
)
def main(data_path):
    dotenv.load_dotenv(Path(data_path) / ".env")

    days = [
        day for file_path in glob(f"{data_path}/20*") for day in file_reader(file_path)
    ]

    os.makedirs("plots", exist_ok=True)

    figure = make_subplots(
        rows=3,
        cols=1,
        subplot_titles=[
            "Worktime difference",
            "Worktime difference distribution",
            "Total worktime difference",
        ],
    )

    _differences = differences(days)
    for _difference in _differences["data"]:
        figure.add_trace(_difference, row=1, col=1)

    _distributions = histograms(days)
    for _distribution in _distributions["data"]:
        figure.add_trace(_distribution, row=2, col=1)

    _integrations = integrated(days)
    for _integration in _integrations["data"]:
        figure.add_trace(_integration, row=3, col=1)

    figure["layout"].update(
        title="Worktime",
        xaxis1=dict(title="Date"),
        yaxis1=dict(title="Hours"),
        xaxis2=dict(title="Worktime difference (in Hours)"),
        yaxis2=dict(title="Number of days"),
        xaxis3=dict(title="Date"),
        yaxis3=dict(title="Hours"),
        showlegend=False,
    )

    plot(figure, filename="worktime_plots.html")


if __name__ == "__main__":
    main()
