from cloudscraper import create_scraper
import time

scape=create_scraper()


print("""



  _    _ _     _     _             _____          _
 | |  | (_)   | |   | |           / ____|        | |
 | |__| |_  __| | __| | ___ _ __ | |     ___   __| | ___
 |  __  | |/ _` |/ _` |/ _ \ '_ \| |    / _ \ / _` |/ _ \\
 | |  | | | (_| | (_| |  __/ | | | |___| (_) | (_| |  __/
 |_|  |_|_|\__,_|\__,_|\___|_| |_|\_____\___/ \__,_|\___|

            Pudgypenguins Checker by Aero25x


    """)




def read_wallets(file_path):
    """Читает кошельки из файла, удаляя пробелы и пустые строки."""
    try:
        with open(file_path, 'r') as file:
            wallets = [line.strip() for line in file if line.strip()]
        return wallets
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []

def get_balance(wallet):
    """Получает баланс для указанного кошелька через API."""
    url = f"https://api.clusters.xyz/v0.1/airdrops/pengu/eligibility/{wallet}"
    try:
        response = scape.get(url)
        response.raise_for_status()  # Проверка на HTTP-ошибки
        data = response.json()

        # Извлечение баланса
        pending_balance_str = data.get("total", {})
        actual_balance = int(pending_balance_str)

        pending_balance_str = data.get("totalUnclaimed", {})
        unclaimed_actual_balance = int(pending_balance_str)


        return actual_balance, unclaimed_actual_balance
    except Exception as e:
        print(f"Ошибка запроса для кошелька {wallet}: {e}")

    return None, None

def main():
    wallets_file = 'wallets.txt'  # Имя файла с кошельками
    wallets = read_wallets(wallets_file)

    if not wallets:
        print("Нет кошельков для обработки.")
        return


    total_balance_ = 0

    for wallet in wallets:
        total_balance, unclaimed_balance  = get_balance(wallet)
        if total_balance is not None and unclaimed_balance is not None:
            total_balance_ +=total_balance
            print(f"{wallet} -> Total: {round(total_balance, 4)} | Unclaimed: {round(unclaimed_balance, 4)}")

        time.sleep(0.5)


    print(f"TOTAL: {total_balance_}")

if __name__ == "__main__":
    main()
