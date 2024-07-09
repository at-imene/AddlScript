import requests
import webbrowser
import time

def check_website(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'accès à {url}: {e}")
        return False

def main():
    url = "https://aadl3inscription2024.dz/"
    while True:
        if check_website(url):
            print(f"{url} est joignable. Ouverture dans le navigateur.")
            webbrowser.open(url)
            break
        else:
            print(f"{url} n'est pas encore joignable. Nouvelle vérification dans 60 secondes.")
            time.sleep(3)

if __name__ == "__main__":
    main()
