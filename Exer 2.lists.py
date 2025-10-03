routes=["Nairobi-Mombasa","Nairobi-Kisumu","Mombasa-Kisumu","Nairobi-Eldoret","Thika-Nyeri",
        "Nakuru-Eldoret","Nairobi-Nakuru","Mombasa-Migori","Narok-Nairobi","Eldoret-Narok"]
routes.append("Nairobi-Meru")
print(routes)
routes.sort()
print(routes)
routes.reverse()
print(routes)
N=sum(1 for route in routes if route.startswith("N"))
print("\nNumber of routes starting with letter N:",N)
x=[route for route in routes if len(routes)>10]
print(x)