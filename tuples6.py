

def main():
    try:
        # Create a tuple of fruits
        fruits = ("apple", "banana", "cherry", "mango", "orange")

        # Display the tuple
        print("Fruits tuple:", fruits)

        # Accessing elements by index
        print("First fruit:", fruits[0])
        print("Last fruit:", fruits[-1])

        # Slicing the tuple
        print("Middle fruits:", fruits[1:4])

        # Checking if an item exists in the tuple
        search_item = input("Enter a fruit to search: ").strip().lower()
        if search_item in fruits:
            print(f"Yes, '{search_item}' is in the tuple.")
        else:
            print(f"No, '{search_item}' is not in the tuple.")

        # Tuple length
        print("Number of fruits:", len(fruits))

    except Exception as e:
        print("An error occurred:", e)

# Run the program
if __name__ == "__main__":
    main()
