from polygon import RESTClient

client = RESTClient("APIkey")

details = client.get_ticker_details(
	"AAPL",
	date="2025-07-25"
	)

print(details)
