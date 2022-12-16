import pandas as pd
from thetadata import ThetaClient, SecType


def get_roots() -> pd.Series:
    # Create a ThetaClient
    client = ThetaClient()  # No credentials required for free access

    # Connect to the Terminal
    with client.connect():  # Make any requests for data inside this block. Requests made outside this block won't run.
        # List all roots that have traded options
        out = client.get_roots(sec=SecType.OPTION)

    # We are out of the client.connect() block, so we can no longer make requests.
    return out


if __name__ == "__main__":
    roots = get_roots()
    print(roots)