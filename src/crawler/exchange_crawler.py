import time

import requests
import csv

api_keys = ['4770ce7538ac41c6b4e6ff21fd9a37a1', 'b6e9835f6c21419082134cc94ceabd4a']
base_url = 'https://openexchangerates.org/api/'
filename = 'exchange_rate.csv'
filednames = ["AED",  "AFN",  "ALL",  "AMD",  "ANG",  "AOA",  "ARS",  "AUD",  "AWG",  "AZN",  "BAM",  "BBD",  "BDT",  "BGN",  "BHD",  "BIF",  "BMD",  "BND",  "BOB",  "BRL",  "BSD",  "BTC",  "BTN",  "BWP",  "BYN",  "BZD",  "CAD",  "CDF",  "CHF",  "CLF",  "CLP",  "CNH",  "CNY",  "COP",  "CRC",  "CUC",  "CUP",  "CVE",  "CZK",  "DJF",  "DKK",  "DOP",  "DZD",  "EGP",  "ERN",  "ETB",  "EUR",  "FJD",  "FKP",  "GBP",  "GEL",  "GGP",  "GHS",  "GIP",  "GMD",  "GNF",  "GTQ",  "GYD",  "HKD",  "HNL",  "HRK",  "HTG",  "HUF",  "IDR",  "ILS",  "IMP",  "INR",  "IQD",  "IRR",  "ISK",  "JEP",  "JMD",  "JOD",  "JPY",  "KES",  "KGS",  "KHR",  "KMF",  "KPW",  "KRW",  "KWD",  "KYD",  "KZT",  "LAK",  "LBP",  "LKR",  "LRD",  "LSL",  "LYD",  "MAD",  "MDL",  "MGA",  "MKD",  "MMK",  "MNT",  "MOP",  "MRO",  "MRU",  "MUR",  "MVR",  "MWK",  "MXN",  "MYR",  "MZN",  "NAD",  "NGN",  "NIO",  "NOK",  "NPR",  "NZD",  "OMR",  "PAB",  "PEN",  "PGK",  "PHP",  "PKR",  "PLN",  "PYG",  "QAR",  "RON",  "RSD",  "RUB",  "RWF",  "SAR",  "SBD",  "SCR",  "SDG",  "SEK",  "SGD",  "SHP",  "SLL",  "SOS",  "SRD",  "SSP",  "STD",  "STN",  "SVC",  "SYP",  "SZL",  "THB",  "TJS",  "TMT",  "TND",  "TOP",  "TRY",  "TTD",  "TWD",  "TZS",  "UAH",  "UGX",  "USD",  "UYU",  "UZS",  "VEF",  "VES",  "VND",  "VUV",  "WST",  "XAF",  "XAG",  "XAU",  "XCD",  "XDR",  "XOF",  "XPD",  "XPF",  "XPT",  "YER",  "ZAR",  "ZMW",  "ZWL"]


def get_currencies():
    url = base_url + 'currencies.json'
    r = requests.get(url)
    result = r.json()
    write_to_file(result)


def write_to_file(json):
    with open(filename, 'a+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=filednames)
        writer.writerow(json)
    csvfile.close()


def get_exchange_rate(index):
    url = base_url + 'latest.json?app_id=' + api_keys[index % 2]
    r = requests.get(url)
    result = r.json()['rates']
    write_to_file(result)


if __name__ == '__main__':
    with open(filename, 'a+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=filednames)
        writer.writeheader()
        counter = 0
    csvfile.close()
    while True:
        get_exchange_rate(counter)
        counter = counter + 1
        time.sleep(1800)
