parking = {}
number_of_cars = int(input())
for car in range(number_of_cars):
    current_driver = input().split()
    command = current_driver[0]
    if command == "register":
        drivers_name = current_driver[1]
        license_plate_number = current_driver[2]
        if drivers_name in parking.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[drivers_name] = license_plate_number
            print(f"{drivers_name} registered {license_plate_number} successfully")
    elif command == "unregister":
        drivers_name = current_driver[1]
        if drivers_name not in parking.keys():
            print(f"ERROR: user {drivers_name} not found")
        else:
            print(f"{drivers_name} unregistered successfully")
            del parking[drivers_name]
for drivers_name, license_plate_number in parking.items():
    print(f"{drivers_name} => {license_plate_number}")
