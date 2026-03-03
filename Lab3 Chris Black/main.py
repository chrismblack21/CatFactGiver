import requests
import json

BASE_URL = "https://catfact.ninja"

# function to get a random cat fact
def get_random_fact():
    url = f"{BASE_URL}/fact"
    response = requests.get(url)
    data = response.json()

    print("Random Cat Fact:")
    print(data['fact'])

def get_multiple_facts():
    limit = input("How many cat facts would you like? ")
    url = f"{BASE_URL}/facts?limit={limit}"

    response = requests.get(url)
    data = response.json()

    print("\nCat Facts:")
    for fact in data['data']:
        print(f"- {fact['fact']}")

# main menu function
def main():
    while True:
        print("\nMenu:")
        print("1. Get a random cat fact")
        print("2. Get multiple cat facts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            get_random_fact()
            
        elif choice == '2':
            get_multiple_facts()

        elif choice == '3':
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

#run the main function
if __name__ == "__main__":
    main()