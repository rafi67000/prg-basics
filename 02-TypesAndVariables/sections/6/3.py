###
# A program that prints a university abbreviation
#
university = "Krakow University of Economics"

abbreviation = [c for c in university if c.isupper()]

print("".join(abbreviation))