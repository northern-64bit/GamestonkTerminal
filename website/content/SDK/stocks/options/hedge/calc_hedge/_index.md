To obtain charts, make sure to add `chart=True` as the last parameter

## Get underlying data 
### stocks.options.hedge.calc_hedge(portfolio_option_amount: float = 100, side: str = 'Call', greeks: dict = {'Portfolio': {'Delta': 1, 'Gamma': 9.1268e-05, 'Vega': 5.4661}, 'Option A': {'Delta': 1, 'Gamma': 9.1268e-05, 'Vega': 5.4661}, 'Option B': {'Delta': 1, 'Gamma': 9.1268e-05, 'Vega': 5.4661}}, sign: int = 1)

Determine the hedge position and the weights within each option and
    underlying asset to hold a neutral portfolio

    Parameters
    ----------
    portfolio_option_amount: float
        Number to show
    side: str
        Whether you have a Call or Put instrument
    greeks: dict
        Dictionary containing delta, gamma and vega values for the portfolio and option A and B. Structure is
        as follows: {'Portfolio': {'Delta': VALUE, 'Gamma': VALUE, 'Vega': VALUE}} etc
    sign: int
        Whether you have a long (1) or short (-1) position

    Returns
    -------
    option A weight: float
    option B weight: float
    portfolio weight: float
    is_singular: boolean

## Getting charts 
### stocks.options.hedge.calc_hedge(portfolio_option_amount: float = 100, side: str = 'Call', greeks: dict = {'Portfolio': {'Delta': 1, 'Gamma': 9.1268e-05, 'Vega': 5.4661}, 'Option A': {'Delta': 1, 'Gamma': 9.1268e-05, 'Vega': 5.4661}, 'Option B': {'Delta': 1, 'Gamma': 9.1268e-05, 'Vega': 5.4661}}, sign: int = 1, chart=True)

Determine the hedge position and the weights within each option and
    underlying asset to hold a neutral portfolio and show them

    Parameters
    ----------
    portfolio_option_amount: float
        Number to show
    side: str
        Whether you have a Call or Put instrument
    greeks: dict
        Dictionary containing delta, gamma and vega values for the portfolio and option A and B. Structure is
        as follows: {'Portfolio': {'Delta': VALUE, 'Gamma': VALUE, 'Vega': VALUE}} etc
    sign: int
        Whether you have a long (1) or short (-1) position

    Returns
    -------
    A table with the neutral portfolio weights.
