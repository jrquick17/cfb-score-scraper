
from scrapers.cfb.teams import scrape, compile_rankings

############################################################################################################################################

# Specify week and year ranges

# week_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
year_range = [2016]

final = scrape(1, 15, 2018)

compile_rankings(final)
