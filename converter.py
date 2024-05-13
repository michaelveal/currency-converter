# Import the 'requests' library to handle HTTP requests.
import requests

def get_exchange_rate(base_currency, target_currency, api_key):
    """
    Function to fetch the exchange rate between two currencies using an API.
    :param base_currency: str, the currency from which to convert
    :param target_currency: str, the currency to which to convert
    :param api_key: str, your personal API key for accessing the exchange rate API
    :return: float, the exchange rate, or None if the API call fails
    """
    # Construct the API URL with the provided currencies and API key.
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    # Send a GET request to the API URL.
    response = requests.get(url)
    # Convert the response to JSON format.
    data = response.json()
    # Check if the API request was successful.
    if data['result'] == 'success':
        # Return the exchange rate if successful.
        return data['conversion_rate']
    else:
        # Return None if the request was not successful.
        return None

def convert_currency(amount, rate):
    """
    Function to convert an amount of money using an exchange rate.
    :param amount: float, the amount of money to convert
    :param rate: float, the exchange rate to use for conversion
    :return: float, the converted amount of money
    """
    # Calculate the converted amount by multiplying the amount by the exchange rate.
    return amount * rate

def main():
    """
    Main function to handle user input and manage the currency conversion process.
    """
    # Prompt the user to enter their API key.
    api_key = '25ccd77a4117d6ead8af3750'  # Replace with your actual API key
    # Ask the user for the base currency.
    base_currency = input("Enter the base currency (e.g., USD): ")
    # Ask the user for the target currency.
    target_currency = input("Enter the target currency (e.g., EUR): ")
    # Ask the user for the amount to convert.
    amount = float(input("Enter the amount in the base currency: "))

    # Retrieve the exchange rate using the provided currencies and API key.
    rate = get_exchange_rate(base_currency, target_currency, api_key)
    if rate is not None:
        # If the rate was successfully retrieved, perform the currency conversion.
        converted_amount = convert_currency(amount, rate)
        # Print the result of the conversion.
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    else:
        # Inform the user if the currency conversion rate was not retrieved successfully.
        print("Failed to retrieve currency conversion rate.")

# Ensures that the main function is executed only when the script is run directly, not when imported.
if __name__ == "__main__":
    main()
