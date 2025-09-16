import requests
import geocoder
from datetime import datetime

def get_precise_coordinates(city_name):
    """Get latitude and longitude from OpenStreetMap"""
    url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200 and len(response.json()) > 0:
        data = response.json()[0]
        return float(data["lat"]), float(data["lon"])
    else:
        return None, None


def get_user_location():
    print("Choose how to provide location:")
    print("1. Enter city or address manually")
    print("2. Use approximate location based on IP")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        city = input("Enter your city or address: ").strip()
        lat, lon = get_precise_coordinates(city)
        if lat and lon:
            print(f"📍 Found location: {city} → ({lat}, {lon})")
            return lat, lon, city
        else:
            print("❌ Could not find exact coordinates. Try a more specific city or address.")
            return None
    elif choice == "2":
        g = geocoder.ip("me")
        if g.ok:
            print(f"🌍 Detected location: {g.city}, {g.country}")
            return g.latlng[0], g.latlng[1], g.city
        else:
            print("❌ Could not detect location via IP.")
            return None
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")
        return None


def get_solar_irradiance(lat, lon):
    """Fetch daily solar irradiance using NASA POWER API"""
    today = datetime.now().strftime("%Y%m%d")

    url = (
        "https://power.larc.nasa.gov/api/temporal/daily/point"
        f"?parameters=ALLSKY_SFC_SW_DWN&start={today}&end={today}"
        f"&latitude={lat}&longitude={lon}&format=JSON&community=RE"
    )

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            irradiance = list(data["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"].values())[0]
            return irradiance  # kWh/m²/day
        except KeyError:
            print("❌ No irradiance data available for this location.")
            return None
    else:
        print(f"❌ Error fetching solar irradiance: {response.status_code}")
        return None


def main():
    print("=== NASA Solar Irradiance Predictor ===")
    location = get_user_location()

    if not location:
        print("❌ Could not get location. Exiting.")
        return

    lat, lon, city = location
    print(f"📍 Using coordinates: {lat}, {lon} ({city})")

    irradiance = get_solar_irradiance(lat, lon)

    if irradiance:
        print(f"☀️ Today's Average Solar Irradiance for {city}: {irradiance} kWh/m²/day")
    else:
        print(f"⚠️ No solar irradiance data found for {city}.")


if __name__ == "__main__":
    main()


