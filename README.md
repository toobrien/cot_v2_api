home page (see "Types of Reports"): https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm

my naming conventions are:

    1. disaggregated reports:

        - `disagg_futs_only`
        - `disagg_futs_and_opts`

    2. "traders in financial futures" reports:
    
        - `fin_futs_only`
        - `fin_futs_and_opts`
    
    3. legacy reports:
    
        - `futs_only`
        - `futs_and_opts`
    
    4. commodity index trader supplemental report:
    
        - `cit_supp`

disaggregated explanatory notes: https://www.cftc.gov/idc/groups/public/@commitmentsoftraders/documents/file/disaggregatedcotexplanatorynot.pdf

financial futures explanatory notes: https://www.cftc.gov/idc/groups/public/@commitmentsoftraders/documents/file/tfmexplanatorynotes.pdf

`gen_defs.py` creates `full_recs.py`, which contains records enums for accessing the results of `cot_v2_api.get_contract`. these enums contain every field in the original CoT files, as published by the CFTC. if any of the report formats change, the api should continue functioning as normal. re-run `gen_defs.py` to update the record format.

note that all values returned by the api are strings.