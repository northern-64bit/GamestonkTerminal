## Get underlying data 
### crypto.dd.all_binance_trading_pairs() -> pandas.core.frame.DataFrame

Returns all available pairs on Binance in DataFrame format. DataFrame has 3 columns symbol, baseAsset, quoteAsset
    example row: ETHBTC | ETH | BTC
    [Source: Binance]


    Returns
    -------
    pd.DataFrame
        All available pairs on Binance
        Columns: symbol, baseAsset, quoteAsset

