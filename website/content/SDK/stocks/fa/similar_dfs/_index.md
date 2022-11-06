## Get underlying data 
### stocks.fa.similar_dfs(symbol: str, info: Dict[str, Any], n: int, no_filter: bool = False)


    Get dataframes for similar companies

    Parameters
    ----------
    symbol : str
        The ticker symbol to create a dataframe for
    into : Dict[str,Any]
        The dictionary produced from the yfinance.info function
    n : int
        The number of similar companies to produce
    no_filter : bool
        True means that we do not filter based on market cap

    Returns
    -------
    new_list : List[str, pd.DataFrame]
        A list of similar companies
