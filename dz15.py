import csv

class AirportNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CountryNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IATACodeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MultipleOptionsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NoOptionsFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def search_airports(file_path, iata_code=None, country=None, name=None):
    try:
        if not iata_code and not country and not name:
            raise NoOptionsFoundError("No search options specified.")

        if sum(1 for param in [iata_code, country, name] if param) > 1:
            raise MultipleOptionsError("Multiple search options specified.")

        if iata_code:
            if not iata_code.isalpha() or len(iata_code) != 3 or not iata_code.isupper():
                raise IATACodeError("Invalid IATA code format.")
            return search_by_iata_code(file_path, iata_code)
        elif country:
            return search_by_country(file_path, country)
        elif name:
            return search_by_name(file_path, name)

    except (NoOptionsFoundError, MultipleOptionsError, IATACodeError, AirportNotFoundError, CountryNotFoundError) as e:
        return str(e)

def search_by_iata_code(file_path, iata_code):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['IATA_Code'] == iata_code:
                return dict(row)
    raise AirportNotFoundError("Airport not found")

def search_by_country(file_path, country):
    airports = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Country'] == country:
                airports.append(dict(row))
    if not airports:
        raise CountryNotFoundError("Country not found")
    return airports

def search_by_name(file_path, name):
    airports = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if name.lower() in row['Airport_Name'].lower():
                airports.append(dict(row))
    if not airports:
        raise AirportNotFoundError("Airport not found")
    return airports

# Example usage:
file_path = 'airports.csv'  # Replace with your CSV file path
try:
    result = search_airports(file_path, iata_code='JFK')
    print(result)
except (AirportNotFoundError, CountryNotFoundError, IATACodeError, MultipleOptionsError, NoOptionsFoundError) as e:
    print(e)