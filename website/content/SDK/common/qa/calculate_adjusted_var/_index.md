## Get underlying data 
### common.qa.calculate_adjusted_var(kurtosis: float, skew: float, ndp: float, std: float, mean: float) -> float

Calculates VaR, which is adjusted for skew and kurtosis (Cornish-Fischer-Expansion)

    Parameters
    ----------
    kurtosis: float
        kurtosis of data
    skew: float
        skew of data
    ndp: float
        normal distribution percentage number (99% -> -2.326)
    std: float
        standard deviation of data
    mean: float
        mean of data

    Returns
    -------
    float
        Real adjusted VaR
