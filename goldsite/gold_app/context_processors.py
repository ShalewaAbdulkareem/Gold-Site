from django.core.cache import cache
import requests
from django.conf import settings


def market_prices(request):

    data = cache.get("market_data")
    if data:
        return data

    headers = {
        "x-access-token": settings.GOLD_API_KEY,
        "Content-Type": "application/json"
    }

    metals = {
        "Gold": "XAU",
        "Silver": "XAG",
        "Platinum": "XPT",
        "Palladium": "XPD",
    }

    market_data = {"metals": []}

    try:
        for name, symbol in metals.items():

            response = requests.get(
                f"https://www.goldapi.io/api/{symbol}/USD",
                headers=headers
            ).json()

            price = response.get("price", 0)
            change = response.get("ch", 0)

            market_data["metals"].append({
                "name": name,
                "price": round(price, 2),
                "change": round(change, 2)
            })

        cache.set("market_data", market_data, 120)

        return market_data

    except Exception as e:
        return {"metals": []}