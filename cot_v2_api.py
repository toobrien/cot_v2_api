from    common_symbols  import COMMON_SYMBOLS
from    enum            import IntEnum
from    raw_recs        import *
from    requests        import get
from    recs            import *

class report(IntEnum):

    disagg_futs_only        = 0
    disagg_futs_and_opts    = 1
    fin_futs_only           = 2
    fin_futs_and_opts       = 3
    futs_only               = 4
    futs_and_opts           = 5
    cit_supp                = 6


class format(IntEnum):

    none        = 0
    raw         = 1
    convenience = 2


API_ROOT    = "https://tvix.xyz/cot_v2"
REPORT_STR  = {
                report.disagg_futs_only:        "disagg_futs_only",
                report.disagg_futs_and_opts:    "disagg_futs_and_opts",
                report.fin_futs_only:           "fin_futs_only",
                report.fin_futs_and_opts:       "fin_futs_and_opts",
                report.futs_only:               "futs_only",
                report.futs_and_opts:           "futs_and_opts",
                report.cit_supp:                "cit_supp"
            }


def convenience_recs(report_type: int, data: dict):

    conv = {}

    if report_type in [ report.disagg_futs_only, report.disagg_futs_and_opts ]:

        pass

    elif report_type in [ report.fin_futs_only, report.fin_futs_and_opts ]:

        pass

    elif report_type in [ report.futs_only, report.futs_and_opts ]:

        n_recs = len(data[futs_only_raw.as_of_date_in_form_yyyy_mm_dd])

        conv[futs_only.date] = data[futs_only_raw.as_of_date_in_form_yyyy_mm_dd]

        conv[futs_only.comm_long]       = [ int(x)      for x in data[futs_only_raw.commercial_positions_long_all]  ]
        conv[futs_only.comm_long_pct]   = [ float(x)    for x in data[futs_only_raw.pct_of_oi_commercial_long_all]  ]
        conv[futs_only.comm_short]      = [ int(x)      for x in data[futs_only_raw.commercial_positions_short_all] ]
        conv[futs_only.comm_short_pct]  = [ float(x)    for x in data[futs_only_raw.pct_of_oi_commercial_short_all] ]
        conv[futs_only.comm_net]        = [ conv[futs_only.comm_long][i]        - conv[futs_only.comm_short][i]        for i in range(n_recs) ]
        conv[futs_only.comm_net_pct]    = [ conv[futs_only.comm_long_pct][i]    - conv[futs_only.comm_short_pct][i]    for i in range(n_recs) ]
                                    
        conv[futs_only.noncomm_long]        = [ int(x)      for x in data[futs_only_raw.noncommercial_positions_long_all]       ]
        conv[futs_only.noncomm_long_pct]    = [ float(x)    for x in data[futs_only_raw.pct_of_oi_noncommercial_long_all]       ]
        conv[futs_only.noncomm_short]       = [ int(x)      for x in data[futs_only_raw.noncommercial_positions_short_all]      ]
        conv[futs_only.noncomm_short_pct]   = [ float(x)    for x in data[futs_only_raw.pct_of_oi_commercial_short_all]         ]
        conv[futs_only.noncomm_spread]      = [ int(x)      for x in data[futs_only_raw.noncommercial_positions_spreading_all]  ]
        conv[futs_only.noncomm_spread_pct]  = [ float(x)    for x in data[futs_only_raw.pct_of_oi_noncommercial_spreading_all]  ]
        conv[futs_only.noncomm_net]         = [ conv[futs_only.noncomm_long][i]     - conv[futs_only.noncomm_short][i]      for i in range(n_recs) ]
        conv[futs_only.noncomm_net_pct]     = [ conv[futs_only.noncomm_long_pct][i] - conv[futs_only.noncomm_short_pct][i]  for i in range(n_recs) ]

        conv[futs_only.nonrep_long]         = [ int(x)      for x in data[futs_only_raw.nonreportable_positions_long_all]  ]
        conv[futs_only.nonrep_long_pct]     = [ float(x)    for x in data[futs_only_raw.pct_of_oi_nonreportable_long_all]  ]
        conv[futs_only.nonrep_short]        = [ int(x)      for x in data[futs_only_raw.nonreportable_positions_short_all] ]
        conv[futs_only.nonrep_short_pct]    = [ float(x)    for x in data[futs_only_raw.pct_of_oi_nonreportable_short_all] ]
        conv[futs_only.nonrep_net]          = [ conv[futs_only.nonrep_long][i]      - conv[futs_only.nonrep_short][i]       for i in range(n_recs) ]
        conv[futs_only.nonrep_net]          = [ conv[futs_only.nonrep_long_pct][i]  - conv[futs_only.nonrep_short_pct][i]   for i in range(n_recs) ]
        
        conv[futs_only.oi] = [ int(x) for x in data[futs_only_raw.open_interest_all] ]

    elif report_type == report.cit_supp:

        pass

    return conv


def get_index(report_type: int):

    res = get(f"{API_ROOT}/{REPORT_STR[report_type]}/index")

    return res.json()


def get_contract(
    report_type:    int, 
    code_or_symbol: str, 
    fmt:            int,
    start_date:     str = None,
    end_date:       str = None
):

    code = code_or_symbol

    if code_or_symbol in COMMON_SYMBOLS:

        code = COMMON_SYMBOLS[code_or_symbol]

    res     = get(f"{API_ROOT}/{REPORT_STR[report_type]}/{code}")
    data    = res.json()

    if fmt != format.none:

        headers = list(data.keys())
        cols    = list(data.values())

        data = {
            i : cols[i]
            for i in range(len(headers))
        }
    
        if fmt == format.convenience:

            data = convenience_recs(report_type, data)

    return data

