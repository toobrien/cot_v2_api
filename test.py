from cot_v2_api import API_ROOT, get_contract, REPORT_TYPES
from full_recs  import futs_only_full
from json       import dumps
from requests   import get
from time       import time

def t1():

    start   = time()
    con     = get_contract("futs_only", "132741")

    recs = zip(
                con[futs_only_full.as_of_date_in_form_yyyy_mm_dd],
                con[futs_only_full.open_interest_all]
            )

    for rec in recs:

        print(rec[0], rec[1])

    print(f"elapsed: {time() - start:0.1f}s")


def t2():

    res = get(f"{API_ROOT}/futs_only/132741").json()

    print(dumps(res, indent = 4))


if __name__ == "__main__":

    t1()
    #t2()