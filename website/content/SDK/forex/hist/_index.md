## Get underlying data 
### forex.hist(to_symbol: str = 'USD', from_symbol: str = 'EUR', resolution: str = 'd', interval: int = 5, start_date: str = '') -> pandas.core.frame.DataFrame

Get historical forex data.

    Parameters
    ----------
    to_symbol : str
        To forex symbol
    from_symbol : str
        From forex symbol
    resolution : str, optional
        Resolution of data.  Can be "i", "d", "w", "m" for intraday, daily, weekly or monthly
    interval : int, optional
        Interval for intraday data
    start_date : str, optional
        Start date for data.

    Returns
    -------
    pd.DataFrame
        Historical data for forex pair
