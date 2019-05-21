"""Quantify how modable a car is by scraping a website for parts and returning
the number available (total and per category).
"""

import argparse
import re
import requests
import sys

# Websites to scrape
WEBSITES = {
        "https://www.tdotperformance.ca/": "https://www.tdotperformance.ca/YEAR-MAKE-MODEL-parts/performance-parts",
}

# XXX - bad way to do this. Just first pass.
TEMP_RE = "(?P<num>\d+) total"

def quantify_mod(year=None, make=None, model=None, trim=None):
    """Given a vehicle, scrape a website to quantify the number of available
    aftermarket parts.
    """
    # XXX Add argument checking

    vehicle_str = " ".join([year, make, model])

    summary = {}
    for website, url in WEBSITES.items():
        url = url.replace("YEAR", year).replace("MAKE", make).replace("MODEL", model)
        response = requests.post(url)
        if response.status_code != 200:
            print(f"Failed scrape for {vehicle_str} - bad status.", file=sys.stderr)
            sys.exit(1)
        m = re.search(TEMP_RE, response.text)
        if m is not None:
            num_results = int(m.group("num"))
            sumary["total"] = num_results
        else:
            print(f"Failed scrape for {vehicle_str} - no total found.", file=sys.stderr)
            sys.exit(1)
    
    # Write results
    with open(vehicle_str.replace(" ", "_") + ".json", "w") as f:
        json.dump(summary, f)


def setup_argparser():
    parser = argparse.ArgumentParser(
            description="Script for scraping aftermarket parts websites for "
            "parts for a particular make/model of car."
    )
    parser.add_argument(
            "-y",
            "--year",
            help="Year of the vehicle.",
    )
    parser.add_argument(
            "-ma",
            "--make",
            help="Make of the vehicle.",
    )
    parser.add_argument(
            "-mo",
            "--model",
            help="Model of the vehicle.",
    )
    parser.add_argument(
            "-t",
            "--trim",
            help="Trim of the vehicle, if applicable.",
    )
    return parser

if __name__=="__main__":
    parser = setup_argparser()
    args = parser.parse_args()
    quantify_mod(year=args.year, make=args.make, model=args.model, trim=args.trim)
