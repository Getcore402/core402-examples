import os
import requests

# Configuration de base de l'API Core402
API_GATEWAY_URL = "https://api.core402.dev/v1/scrape"
API_KEY = os.getenv("CORE402_API_KEY", "your_api_key_here")

def fetch_protected_data(target_url):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
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
