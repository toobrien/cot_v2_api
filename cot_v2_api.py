from    enum       import IntEnum
from    requests   import get


API_ROOT = "https://tvix.xyz/cot_v2"

REPORT_TYPES = [
    "disagg_futs_only",
    "disagg_futs_and_opts",
    "fin_futs_only",
    "fin_futs_and_opts",
    "futs_only",
    "futs_and_opts",
    "cit_supp"
]


def get_index(report_type):

    res = get(f"{API_ROOT}/{report_type}/index")

    return res.json()


def get_contract(report_type, code):

    res = get(f"{API_ROOT}/{report_type}/{code}")
    res = res.json()

    headers = list(res.keys())
    cols    = list(res.values())

    data = {
        i : cols[i]
        for i in range(len(headers))
    }

    return data

