from django.core.cache import cache
import requests
from django.conf import settings


def market_prices(request):
    print("MARKET PRICES FUNCTION RUNNING")

    data = cache.get("market_data")

    if data:
        return {"metals": data}

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

    market_data = []

    try:
        for name, symbol in metals.items():

            response = requests.get(
                f"https://www.goldapi.io/api/{symbol}/USD",
                headers=headers,
                timeout=5
            )

            if response.status_code == 200:
                data = response.json()

                price = data.get("price", 0)
                change = data.get("ch", 0)

                market_data.append({
                    "name": name,
                    "price": round(price, 2),
                    "change": round(change, 2)
                })

        cache.set("market_data", market_data, 120)

        return {"metals": market_data}

    except Exception as e:
        print("Gold API error:", e)
        return {"metals": []}