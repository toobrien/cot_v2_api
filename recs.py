from enum import IntEnum


class disagg_futs(IntEnum):

    pass


class fin_futs_only(IntEnum):

    pass


class futs_only(IntEnum):

    date                = 0
    comm_long           = 1
    comm_long_pct       = 2
    comm_short          = 3
    comm_short_pct      = 4
    comm_net            = 5
    comm_net_pct        = 6
    noncomm_long        = 7
    noncomm_long_pct    = 8
    noncomm_short       = 9
    noncomm_short_pct   = 10
    noncomm_spread      = 11
    noncomm_spread_pct  = 12
    noncomm_net         = 13
    noncomm_net_pct     = 14
    nonrep_long         = 15
    nonrep_long_pct     = 16
    nonrep_short        = 17
    nonrep_short_pct    = 18
    nonrep_net          = 19
    nonrep_net_pct      = 20
    oi                  = 21


class cit_supp(IntEnum):

    pass


# these record types are the same

disagg_futs_and_opts    = disagg_futs
fin_futs_and_opts       = fin_futs_only
futs_and_opts           = futs_only