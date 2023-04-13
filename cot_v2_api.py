from    requests        import get
from    common_symbols  import COMMON_SYMBOLS


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


def get_contract(
    report_type:    str, 
    code_or_symbol: str, 
    format:         bool = True):

    code = code_or_symbol

    if code_or_symbol in COMMON_SYMBOLS:

        code = COMMON_SYMBOLS[code_or_symbol]

    res     = get(f"{API_ROOT}/{report_type}/{code}")
    data    = res.json()

    if format:

        headers = list(data.keys())
        cols    = list(data.values())

        data = {
            i : cols[i]
            for i in range(len(headers))
        }

    return data

