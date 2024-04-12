my_projects = {
    "free_employees": [
        {"name": "Lukas", "surname": "Armonas", "position": "team lead"},
        {"name": "Giedrė", "surname": "Rutkauskaitė", "position": "programmer"},
        {"name": "Algimantas", "surname": "Ruteikis", "position": "programmer"},
        {"name": "Algimantas", "surname": "Ruteikis", "position": "programmer"},
    ],
    "projects": [{
        "name": "Wind Turbine program",
        "description": "Vėjo jėgainių programa",
        "deadline": 6.5,
        "responsible": {"name": "Donatas", "surname": "Noreika"},
        "employees": [
            {"name": "Domas", "surname": "Rakauskas", "position": "programmer"},
            {"name": "Laura", "surname": "Dambrauskaitė", "position": "tester"},
            {"name": "Rokas", "surname": "Rutkauskas", "position": "team leader"},
        ]
    },
        {
            "name": "Website",
            "description": "Svetainė naujam klientui",
            "deadline": 3,
            "responsible": {"name": "Rokas", "surname": "Rutkauskas"},
            "employees": [
                {"name": "Lauras", "surname": "Tuminas", "position": "programmer"},
                {"name": "Andrius", "surname": "Dambrauskas", "position": "tester"},
            ]
        }
    ]
}

print(my_projects['projects'][0]['deadline'])
