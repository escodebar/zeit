# Zeit

A time evaluation tool.

## Installation

You may install `zeit` directly from this Git repository using `pip`:

```shell
$ pip install git+https://github.com/escodebar/zeit.git
```

## Usage

To use `zeit` you first need some data files on which you record your working time.
The file's name needs to be formatted with the year and the month of the data it contains.
Each line in the text file then contains the working time for the day of that month.
Shifts are split with tabs, text may also be included.

*Example* For instance, for January 2019 one creates a text file `2019-01`.
The content could looks as follows:
```
08:00-16:33	Holidays
08:00-16:33	Holidays
09:20-12:30	13:30-17:15
08:45-11:45	12:30-19:45
13:30-14:00

07:00-12:15	13:00-17:00
09:00-12:00	13:15-19:30
07:30-12:25	12:55-17:20
05:20-12:15	13:00-18:30
08:30-12:00	13:20-18:45


11:00-12:00	12:45-18:00	18:50-20:45
09:00-12:00	13:00-16:40
08:15-12:00	12:40-20:15
08:15-12:00	12:40-18:50
07:00-11:30	12:30-17:30


06:35-12:00	13:00-17:00
Compensation
06:45-11:45	13:00-17:50
07:45-12:00	12:30-17:15
09:00-11:50	12:20-22:00


08:25-12:00	13:00-17:30	22:20-23:45
08:30-11:50	12:30-18:00	18:50-20:15
08:10-11:50	13:10-18:00
08:00-16:33	Holidays
```

Once files are provided, run the `zeit` module using python:
```shell
$ python -m zeit --data-path /path/to/data/files
```

## Configuration

8 hours 24 minutes of working time per day are used as default.
This can be changed by setting the `ZEIT_SHIFT_LENGTH` environment variable.
The configuration is also read from a local `.env` file.
