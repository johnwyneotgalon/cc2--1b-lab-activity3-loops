print(''' Otgalon, John Wyne B.                   CITcS- 1B
 CC2 - LabAct1                           Date:09.08.23 ''')
print("=" * 69)
weight_in_pounds = 69
length_in_miles = 69
temperature_in_fahrenheit = 6900

def pounds_to_kilograms(pounds):
    return pounds * 0.45359237

def miles_to_kilometers(miles):
    return miles * 1.60934

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


student_ages = [18, 19, 21, 22, 23, 24, 14, 25, 19, 18]
average_age = sum(student_ages) / len(student_ages)


adventurers = [
    {"name": "Eldric", "power": "Pyromancy", "weapon": "Flaming Sword"},
    {"name": "Lyanna", "power": "Aerokinesis", "weapon": "Gale Bow"},
    {"name": "Thalassa", "power": "Hydrokinetics", "weapon": "Tidal Trident"},
    {"name": "Draven", "power": "Terramancy", "weapon": "Stone Hammer"},
    {"name": "Seraphina", "power": "Chronomagic", "weapon": "Sands of Time"}
]

villain = {
    "name": "Morgaroth the Malevolent",
    "dark_power": "Necromancy",
    "weapon": "Cursed Scythe",
    "minions": ["Shadow Reapers", "Soul Drainers", "Night Phantoms"]
}


print(f"Weight in Pounds (lbs): {weight_in_pounds}")
print(f"Weight converted to Kilograms (kg): {pounds_to_kilograms(weight_in_pounds):.2f}")
print("=" * 47)
print(f"Length in Miles (mi): {length_in_miles}")
print(f"Length converted to Kilometers (km): {miles_to_kilometers(length_in_miles):.2f}")
print("=" * 47)
print(f"Temperature in Fahrenheit(°F): {temperature_in_fahrenheit}")
print(f"Temperature converted to Celsius (°C): {fahrenheit_to_celsius(temperature_in_fahrenheit):.2f}")
print("=" * 47)


print("\nAges of Students:")
for i, age in enumerate(student_ages, start=1):
    print(f"Age of Student {i}: {age}")

print(f"The average age of the students is: {average_age:.1f}")


print("\nFantasy Story:")
print(f"In the mystical realm of Eloria, a great evil has arisen. {villain['name']}, a master of {villain['dark_power']},")
print("has unleashed his malevolent power upon the land, raising an army of darkness:")

for minion in villain['minions']:
    print(f"- {minion}")

print("To thwart this dark threat, five brave adventurers have come forward, each harnessing the power of an element:")

for adventurer in adventurers:
    print(f"- {adventurer['name']}, master of {adventurer['power']}, armed with the mighty {adventurer['weapon']}")

print(f"{villain['name']}'s sinister laughter echoes through the land as he wields the {villain['weapon']} and")
print("summons the power of the void. The fate of Eloria now hangs in the balance as the battle between light")
print("and darkness is about to unfold.")

print("Will the adventurers' elemental powers be enough to vanquish the malevolent Morgaroth and restore peace to Eloria?")
