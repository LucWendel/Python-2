Klas9A = (
    ("Luc", 18, "Uithoorn"),
    ("Chris-jan", 17, "Aalsmeer"),
    ("Nelis", 17, "Aalsmeer"),
    ("Corrie", 18, "Aalsmeer"),
    ("Jan", 20, "Amstelveen"),
    ("Wim", 18, "Amsterdam"),
)
for naam, leeftijd, stad in sorted(Klas9A, key=lambda x: x[1]):
    print(
        "Leerling naam is {}, Leerling leeftijd is {} en woont in {} ".format(
            naam, leeftijd, stad
        )
    )
