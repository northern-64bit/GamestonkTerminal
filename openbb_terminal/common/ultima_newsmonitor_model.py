""" Ultima Insights News Monitor Model """
__docformat__ = "numpy"

import logging
import os
from urllib.parse import quote

import certifi
import pandas as pd

from openbb_terminal.core.session.current_user import get_current_user
from openbb_terminal.decorators import check_api_key, log_start_end
from openbb_terminal.helper_funcs import request
from openbb_terminal.rich_config import console

logger = logging.getLogger(__name__)


base_url = "https://api.ultimainsights.ai/v1"


@log_start_end(log=logger)
@check_api_key(["API_ULTIMAINSIGHTS_KEY"])
def get_news(term: str = "", sort: str = "articlePublishedDate") -> pd.DataFrame:
    """Get news for a given term and source. [Source: Ultima Insights News Monitor]

    Parameters
    ----------
    term : str
        term to search on the news articles
    sort: str
        the column to sort by

    Returns
    -------
    articles: pd.DataFrame
        term to search on the news articles

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.news()
    """
    # Necessary for installer so that it can locate the correct certificates for
    # API calls and https
    # https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error/73270162#73270162
    os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
    os.environ["SSL_CERT_FILE"] = certifi.where()

    current_user = get_current_user()
    auth_header = {
        "Authorization": f"Bearer {current_user.credentials.API_ULTIMAINSIGHTS_KEY}"
    }

    have_data = False
    limit = 0

    while not have_data:
        if term:
            term = quote(term)
            term = term.upper()
            term = term.strip()
            if term in supported_terms():
                data = request(
                    f"{base_url}/getNewsArticles/{term}", headers=auth_header
                )
            else:
                console.print(
                    "[red]Ticker not supported. Unable to retrieve data\n[/red]"
                )
                return pd.DataFrame()
        else:
            console.print("[red]No term specified. Unable to retrieve data\n[/red]")
            return pd.DataFrame()

        if (
            hasattr(data, "status") and data.status_code == 200
        ):  # Checking if data has status attribute and if data request succeeded
            if data.content:
                have_data = True
            elif limit == 60:  # Breaking if 60 successful requests return no data
                console.print("[red]Timeout occurred. Please try again\n[/red]")
                break
            limit = limit + 1

        elif (
            hasattr(data, "status") and data.status_code != 200
        ):  # If data request failed
            console.print("[red]Status code not 200. Unable to retrieve data\n[/red]")
            break
        else:
            # console.print("[red]Could not retrieve data\n[/red]")
            break
    if not data.json():
        return pd.DataFrame()
    df = pd.DataFrame(
        data.json(),
        columns=[
            "articleHeadline",
            "articleURL",
            "articlePublishedDate",
            "riskCategory",
            "riskElaboratedDescription",
            "relevancyScore",
        ],
    )
    df = df[df["relevancyScore"] < 5]
    df = df[df["relevancyScore"] > 3.5]
    df["riskElaboratedDescription"] = df["riskElaboratedDescription"].str.replace(
        "\n", ""
    )
    df["riskElaboratedDescription"] = df["riskElaboratedDescription"].str.replace(
        "\n", ""
    )
    df["articlePublishedDate"] = pd.to_datetime(df["articlePublishedDate"])
    df = df.sort_values(by=[sort], ascending=False)
    return df


@log_start_end(log=logger)
def supported_terms() -> list:
    """Get supported terms for news. [Source: Ultima Insights]

    Returns
    -------
    terms: list
        list of supported terms (tickers)

    """

    # Necessary for installer so that it can locate the correct certificates for
    # API calls and https
    # https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error/73270162#73270162
    os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
    os.environ["SSL_CERT_FILE"] = certifi.where()
    data = request(f"{base_url}/supportedTickers")
    return list(data.json())


@log_start_end(log=logger)
@check_api_key(["API_ULTIMAINSIGHTS_KEY"])
def get_company_info(ticker: str) -> dict:
    """Get company info for a given ticker. [Source: Ultima Insights]

    Parameters
    ----------
    ticker : str
        ticker to search for company info

    Returns
    -------
    company_info: dict
        dictionary of company info
    """

    # Necessary for installer so that it can locate the correct certificates for
    # API calls and https
    # https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error/73270162#73270162
    os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
    os.environ["SSL_CERT_FILE"] = certifi.where()

    current_user = get_current_user()
    auth_header = {
        "Authorization": f"Bearer {current_user.credentials.API_ULTIMAINSIGHTS_KEY}"
    }

    if ticker in supported_terms():
        data = request(f"{base_url}/getCompanyInfo/{ticker}", headers=auth_header)
        return data.json()
    console.print("[red]Ticker not supported. Unable to retrieve data\n[/red]")
    return {}