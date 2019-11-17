from scrapers.cfb.teams import scrape, compile_rankings

final = scrape(1, 12, 2019)

compile_rankings(final)
