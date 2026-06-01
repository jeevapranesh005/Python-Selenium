class NoMatchException(Exception):
    pass

aadhar_number = input("Aadhar Number: ")
name = input("Name: ")
city = input("City: ")
state = input("State: ")
country = input("Country: ")

try:
    if country != "India":
        raise NoMatchException("Country name does not match 'India'")
    print("Citizen Details:")
    print(f"Aadhar Number: {aadhar_number}")
    print(f"Name: {name}")
    print(f"City: {city}")
    print(f"State: {state}")
    print(f"Country: {country}")
except NoMatchException as error:
    print(error)
