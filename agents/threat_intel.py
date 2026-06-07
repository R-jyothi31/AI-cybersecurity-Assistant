import requests
import re

def extract_ip(log_text):

    match = re.search(
        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        log_text
    )

    if match:
        return match.group()

    return None


def check_ip_reputation(ip):

    if not ip:
        return {
            "ip": "Not Found"
        }

    try:

        response = requests.get(
            f"https://ipinfo.io/{ip}/json",
            timeout=5
        )

        data = response.json()

        return {

            "ip": ip,

            "city": data.get(
                "city",
                "Unknown"
            ),

            "country": data.get(
                "country",
                "Unknown"
            ),

            "org": data.get(
                "org",
                "Unknown"
            )
        }

    except:

        return {
            "ip": ip,
            "country": "Unknown"
        }