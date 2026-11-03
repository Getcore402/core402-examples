import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_GATEWAY_URL = os.getenv("API_GATEWAY_URL", "http://localhost:3000/v1/scrape")
API_KEY = os.getenv("CORE402_API_KEY", "your_api_key_here")

def fetch_protected_data(target_url):
    # Utilisation de x-api-key comme attendu par l'API Gateway
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "url": target_url
    }

    print(f"[*] Interrogation de l'API Core402 pour : {target_url}")
    response = requests.post(API_GATEWAY_URL, json=payload, headers=headers)

    if response.status_code == 200:
        print("[+] Données récupérées avec succès !")
        return response.json()
    elif response.status_code == 402:
        print("[!] Paiement requis (HTTP 402) - Vérifiez le solde de votre clé API.")
        return None
    else:
        print(f"[x] Erreur inattendue : {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    target = "https://example.com"
    data = fetch_protected_data(target)
    if data:
        print(data)
