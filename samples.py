from cot_v2_api import API_ROOT, get_contract, get_index, format, report
from raw_recs   import futs_only_raw
from recs       import futs_only
from json       import dumps
from polars     import from_dict
from requests   import get
from sys        import argv
from time       import time


def s0():

    # set "format" to false to keep original headers
    
    # note: in this example, an exchange symbol is used instead of a contract code.
    #       you can add more symbols -> code mappings to the common_symbols file.
    #       use the report's index (see sample 3) to discover the mapping.
           
    # example: put into a polars dataframe

    con = get_contract(report.futs_only, "NQ", format.none)
    df  = from_dict(con)

    print(df)


def s1():

    # set "format" to true for use with cot_v2_api record types
    # example: print eurodollar open interest by date

    eurodollars = "132741" # find using the index
    con         = get_contract(report.futs_only, eurodollars, format.full)

    recs = zip(
                con[futs_only_raw.as_of_date_in_form_yyyy_mm_dd],
                con[futs_only_raw.open_interest_all]
            )

    for rec in recs:

        print(rec[0], rec[1])


def s2():

    # bypass this library and get the raw data (column headers are in-tact)

    report_name     = "futs_only"
    contract_code   = "076691" # platinum; find using the index

    res = get(f"{API_ROOT}/{report_name}/{contract_code}").json()

    print(dumps(res, indent = 4))


def s3():

    # print the "futures only" index

    idx = get_index(report.futs_only)

    print(dumps(idx, indent = 4))


def s4():

    con = get_contract(report.futs_only, "ZC", format.raw)

    total_oi    = int(con[futs_only_raw.open_interest_all][0])
    comm_long   = int(con[futs_only_raw.commercial_positions_long_all][0])
    comm_short  = int(con[futs_only_raw.commercial_positions_short_all][0])
    comm_net    = comm_long - comm_short

    rec0 = [
        f"name:                         {con[futs_only_raw.market_and_exchange_names][0]}",
        f"total oi:                     {total_oi}",
        f"comm_long:                    {comm_long}",
        f"comm_short:                   {comm_short}",
        f"comm_pct_long:                {con[futs_only_raw.pct_of_oi_commercial_long_all][0]}",
        f"comm_pct_long (self-calc):    {comm_long / total_oi * 100:0.1f}",
        f"comm_pct_short:               {con[futs_only_raw.pct_of_oi_commercial_short_all][0]}",
        f"comm_pct_short (self-calc):   {comm_short / total_oi * 100:0.1f}",
        f"comm_net (self-calc):         {comm_net}",
        f"comm_net_pct (self-calc):     {comm_net / total_oi * 100:0.1f}",
    ]

    print("\n".join(rec0))


if __name__ == "__main__":

    to_run = int(argv[1])

    samples = [
        s0,
        s1,
        s2,
        s3,
        s4
    ]
    
    start = time()

    samples[to_run]()

    print(f"elapsed: {time() - start:0.1f}s")