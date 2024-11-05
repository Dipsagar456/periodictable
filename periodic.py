import periodictable 

def get_element_information():
    print("welcome to the periodictable...!!!")
    try:
        atomic_no = int(input("Enter Atomic Number:... "))
        element = periodictable.elements[atomic_no]
        print(f"\nElement Details:")
        print(f"Name: {element.name}")
        print(f"Symbol: {element.symbol}")
        print(f"Atomic Mass: {element.mass} u")
        print(f"Density: {element.density} g/cm³ (if available)")
        
    except KeyError:
        print("invalid atomic number. Please enter a number between 1 and 118, so try again...!!!")
    except ValueError:
        print("Please enter a valid integer for the atomic number...!!!")


