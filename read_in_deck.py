#!/usr/bin/env python3

from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
import re

def read_deck(file_name):
    cards = {}
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if "//deck" in line:
                continue

            if "//sideboard" in line:
                break

            r = re.match(r"""(\d)(.*)\((.{1,4})\)""", line)
            try:
                num, name, magic_set = r.groups()
            except AttributeError as e:
                print("Error: unable to parse line: {}".format(line))
                raise

            num = int(num)
            name = name.strip()
            # I'm probably going to ditch checking set and just use the first
            matching_cards = Card.where(name=name, set=magic_set).all()
            try:
                assert len(matching_cards) == 1
            except AssertionError:
                print("Error: multiple cards matched for \"{}\"".format(name))
                for card in matching_cards:
                    print(card.__dict__)
            card_details = matching_cards[0]
            assert name not in cards
            cards[name] = {
                "card_details": card_details,
                "number_of_card": num
                }

    return cards
