import pickle
from datetime import datetime
import os

data_dir = os.path.join(os.pardir, "historical", "data")
date_format = "%Y-%m-%d"
fn_sep = "_"  # filename separator


def load(ticker, start, end):
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    start = to_date(start)
    end = to_date(end)

    data = load_local(ticker, start, end)

    if data is None:
        from pandas.io.data import DataReader
        print "NOT FOUND. DOWNLOADING..."
        data = DataReader(ticker,  "yahoo", start, end)
        print "DOWNLOAD COMPLETE"
        output = open(os.path.join(data_dir, create_name(ticker, start, end)), "wb")
        pickle.dump(data, output)

    return data


def load_local(ticker, start, end):
    print "looking for local copy of", ticker, "between", start, "and", end
    for file in os.listdir(data_dir):
        t, s, e = parse_name(file)
        if t == ticker and s <= start and end <= e:
            print("FOUND")
            market_data = pickle.load(open(os.path.join(data_dir, file)))
            market_data = market_data[to_str(start):to_str(end)]
            return market_data
    return None


def parse_name(filename):
    ticker, start, end = filename.split(fn_sep)
    return ticker, to_date(start), to_date(end)


def create_name(ticker, start, end):
    return "_".join([ticker, to_str(start), to_str(end)])


def to_date(date, format=date_format):
    return datetime.strptime(date, format)


def to_str(date, format=date_format):
    return datetime.strftime(date, format)