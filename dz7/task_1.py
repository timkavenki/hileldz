import argparse
import requests
from datetime import datetime, timedelta
from tabulate import tabulate

def fetch_exchange_rate(date, currency_from, currency_to, amount):
    url = f"https://api.exchangerate.host/convert"
    params = {
        "from": currency_from,
        "to": currency_to,
        "amount": amount,
        "date": date,
    }
    response = requests.get(url, params=params)
    data = response.json()
    rate = data["info"]["rate"]
    result = data["result"]
    return rate, result

def main():
    parser = argparse.ArgumentParser(description="Online Currency Converter")
    parser.add_argument("currency_from", type=str, default="USD", help="Currency to convert from")
    parser.add_argument("currency_to", type=str, default="UAH", help="Currency to convert to")
    parser.add_argument("amount", type=float, default=100.00, help="Amount to convert")
    parser.add_argument("--start_date", type=str, help="Start date for conversion")
    parser.add_argument("--save_to_file", action="store_true", help="Save data to a file")
    args = parser.parse_args()

    if args.start_date:
        try:
            start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Using current date.")
            start_date = datetime.now()
    else:
        start_date = datetime.now()

    current_date = datetime.now()
    data = [["date", "from", "to", "amount", "rate", "result"]]

    while start_date <= current_date:
        date_str = start_date.strftime("%Y-%m-%d")
        rate, result = fetch_exchange_rate(date_str, args.currency_from, args.currency_to, args.amount)
        data.append([date_str, args.currency_from, args.currency_to, args.amount, rate, result])
        start_date += timedelta(days=1)

    if args.save_to_file:
        file_name = f"{current_date.strftime('%d-%m-%Y')}-{args.currency_from}-{args.currency_to}-5-days-weather-forecast.txt"
        with open(file_name, "w") as f:
            for row in data:
                f.write("\t".join(map(str, row)) + "\n")
        print(f"Data saved to {file_name}")
    else:
        print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()