## Get underlying data 
### portfolio.maxdrawdown(portfolio: openbb_terminal.portfolio.portfolio_model.PortfolioModel) -> pandas.core.frame.DataFrame

Class method that retrieves maximum drawdown ratio for portfolio and benchmark selected

    Parameters
    ----------
    portfolio: Portfolio
        Portfolio object with trades loaded

    Returns
    -------
    pd.DataFrame
        DataFrame with maximum drawdown for portfolio and benchmark for different periods
