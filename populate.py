#!/usr/bin/env python3
import csv
import requests

BASE_URL = "http://localhost:8000"

def main():
    with open("flight_passengers.csv") as fd:
        books_csv = csv.DictReader(fd)
        for book in books_csv:
            x = requests.post(BASE_URL+"/travelers", json=book)
            if not x.ok:
                print(f"Failed to post book {x} - {book}")

if __name__ == "__main__":
    main()