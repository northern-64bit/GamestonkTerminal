## Get underlying data 
### stocks.fa.av_balance(symbol: str, limit: int = 5, quarterly: bool = False, ratios: bool = False, plot: bool = False) -> pandas.core.frame.DataFrame

Get balance sheets for company

    Parameters
    ----------
    symbol : str
        Stock ticker symbol
    limit : int
        Number of past to get
    quarterly : bool, optional
        Flag to get quarterly instead of annual, by default False
    ratios: bool
        Shows percentage change, by default False
    plot: bool
        If the data shall be formatted ready to plot

    Returns
    -------
    pd.DataFrame
        DataFrame of the balance sheet
