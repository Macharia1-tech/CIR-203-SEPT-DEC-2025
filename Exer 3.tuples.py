patient=("steve",34,"122/80",71)
print("\nPatient's records:",patient)
print("\nPatient's age:",patient[1])
print("\nPatient's heart rate:",patient[3])
Explain=""" Tuples are imutable meaning the data cannot be accidentally changed.
patients vitals are sensitive information that should not be altered once recorded.
Tuples also allow grouping different data types into one structure.
"""
print("Explanation",Explain)
Patient=list(patient)
print(Patient)
Patient[3]=75
print(Patient)
patient=tuple(Patient)
print(patient)
patients=(
    ("John",30,"119/80",69),
    ("Becky",19,"121/80",72),
    ("James",25,"120/80",71),
    ("Mary",35,"117/70",70),
    ("Macharia",20,"123/80",73),
)
names=[patient[0] for patient in patients]
print("\nPatient names:",names)