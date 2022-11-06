## Get underlying data 
### keys.reddit(client_id: str, client_secret: str, password: str, username: str, useragent: str, persist: bool = False, show_output: bool = False) -> str

Set Reddit key
    Parameters
    ----------
        client_id: str
        client_secret: str
        password: str
        username: str
        useragent: str
        persist: bool
            If False, api key change will be contained to where it was changed. For example, Jupyter notebook.
            If True, api key change will be global, i.e. it will affect terminal environment variables.
            By default, False.
        show_output: bool
            Display status string or not. By default, False.
    Returns
    -------
    status: str
