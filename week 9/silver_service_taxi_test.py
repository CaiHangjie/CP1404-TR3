from silver_service_taxi import SilverServiceTaxi

hummer_taxi = SilverServiceTaxi("Hummer", 200, 2)

hummer_taxi.start_fare()
hummer_taxi.drive(18)

# Print SilverServiceTaxi details
print("SilverServiceTaxi details:")
print(hummer_taxi)


fare = 48.78
assert round(hummer_taxi.get_fare(), 2) == round(fare, 2), f"Test failed! Expected fare: ${fare:.2f}, Actual fare: ${hummer_taxi.get_fare():.2f}"

print(f"Expected fare: ${fare:.2f}")
print(f"Actual fare: ${hummer_taxi.get_fare():.2f}")