### usage

you can access the full database of the commitments of traders reports using `cot_v2_api.py`. the two primary functions are:

- `get_index`: returns an index of cftc code to contract description. these values both codes appear in the text of the cftc reports.
- `get_contract`: returns the cot data for a single contract in a column-oriented format. Set `format` to `format.raw` and you can access the columns using the record enums in `full_recs.py`. use `format.none` to retain the field names (e.g. for use with a dataframe), and `format.convenience` for smaller records that have only the most useful fields (including net and percentage position calculations). the convenience records are defined in `recs.py`.

the convenience records are the same between "futures only" and "futures and options" variants of the same report; i.e., all reports except the supplemental report, which has only one format. although convenience records are provided for both forms of each of the other three reports, it's advisable to simply use the "futures only" version.

`get_index` requires the report type (listed below)--each report tracks a different slate of contracts, although the same contract should have the same code in each report. get index also allows (but does not require) start and end dates. these parameters should be in `yyyy-mm-dd`.

note that, unfortunately, the `date` column returned varies by report. for the disaggregated and financial futures reports, dates represent the publication of the report (i.e. friday). for the legacy and supplemental reports, dates represent the "as of" date, i.e. tuesday, when the data was collected.

`get_contract` requires both the report name and the contract code. you may also use a symbol, if it is mapped to its contract code in `common_symbols.py`. i have populated `common_symbols` with a number of popular contracts already. add any that you see fit after discovering the mapping using `get_index`.

### explanatory links

To better understand the report contents, the cftc website offers some helpful links:

home page (see "types of reports"): https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm

For `get_index` and `get_contract` the `report_type` argument follows these naming conventions:

    1. disaggregated reports:

        - disagg_futs_only
        - disagg_futs_and_opts

    2. "traders in financial futures" reports:
    
        - fin_futs_only
        - fin_futs_and_opts
    
    3. legacy reports:
    
        - futs_only
        - futs_and_opts
    
    4. commodity index trader supplemental report:
    
        - cit_supp

disaggregated explanatory notes: https://www.cftc.gov/idc/groups/public/@commitmentsoftraders/documents/file/disaggregatedcotexplanatorynot.pdf

financial futures explanatory notes: https://www.cftc.gov/idc/groups/public/@commitmentsoftraders/documents/file/tfmexplanatorynotes.pdf


### other

`gen_defs.py` creates `raw_recs.py`, which contains records enums for accessing the results of `cot_v2_api.get_contract`. the enums contain every field in the original CoT files, unaltered and as published by the cftc--only excess whitespace has been stripped. if any of the report formats change, the api should continue functioning as normal. re-run `gen_defs.py` to update the record format.

note that all values returned by the api are strings.

as the cftc adds new archives to their site, the api should incorporate them. the reports are published each friday, and the api updates to include the latest report on saturday.

if you notice any errors (surely there are some), please contact me at `tpo.ac2@gmail.com`