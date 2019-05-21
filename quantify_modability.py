"""Quantify how modable a car is by scraping a website for parts and returning
the number available (total and per category).
"""

import argparse
import requests


def quantify_mod(year=None, make=None, model=None, trim=None):
    """Given a vehicle, scrape a website to quantify the number of available
    aftermarket parts.
    """
    pass


def setup_argparser():
    parser = argparse.ArgumentParser(
            description="Script for scraping aftermarket parts websites for "
            "parts for a particular make/model of car."
    )
    parser.add_argument(
            "-y",
            "--year",
            desc="Year of the vehicle.",
            type=int
    )
    parser.add_argument(
            "-ma",
            "--make",
            make="Make of the vehicle.",
    )
    parser.add_argument(
            "-mo",
            "--model",
            make="Model of the vehicle.",
    )
    parser.add_argument(
            "-t",
            "--trim",
            make="Trim of the vehicle, if applicable.",
    )

if __name__=="__main__":
    parser = setup_argparser()
    args = parser.parse_args()
    quantify_mod(year=args.year, make=args.make, model=args.model, trim=args.trim)
