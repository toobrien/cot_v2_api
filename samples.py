from cot_v2_api import API_ROOT, get_contract, get_index, REPORT_TYPES
from full_recs  import futs_only_full
from json       import dumps
from polars     import from_dict
from requests   import get
from sys        import argv
from time       import time


def s0():

    # set "format" to false to keep original headers
    # example: put into a polars dataframe

    con = get_contract("futs_only", "NQ", False)

    df = from_dict(con)

    print(df)


def s1():

    # set "format" to true for use with cot_v2_api record types
    # example: print eurodollar open interest by date

    eurodollars = "132741" # find using the index
    con         = get_contract("futs_only", eurodollars, True)

    recs = zip(
                con[futs_only_full.as_of_date_in_form_yyyy_mm_dd],
                con[futs_only_full.open_interest_all]
            )

    for rec in recs:

        print(rec[0], rec[1])


def s2():

    # bypass this library and get the raw data (column headers are in-tact)

    eurodollar_code = "132741" # find using the index

    res = get(f"{API_ROOT}/futs_only/{eurodollar_code}").json()

    print(dumps(res, indent = 4))


def s3():

    # print the "futures only" index

    idx = get_index("futs_only")

    print(dumps(idx, indent = 4))


if __name__ == "__main__":

    to_run = int(argv[1])

    start = time()

    samples = [
        s0,
        s1,
        s2,
        s3
    ]

    samples[to_run]()

    print(f"elapsed: {time() - start:0.1f}s")