def solution_station_5(member_name):
    teams = {
        1: ["Mika", "Maria", "Isis", "Rosa", "Maja", "Damaris"],
        2: ["Emily", "Celia", "Carine", "Sabrina", "Gur"],
        3: ["Elisa", "Sari", "Dave", "Dima", "Jesper", "Martyna"],
        4: ["Kelt", "Sebastian", "Quanpu", "Ruben", "Sofia", "Gabriella"],
        5: ["Kian", "Sahir", "Tom", "Gonzalo", "Ameer", "Teun"],
        6: ["Angelica", "Matas", "Caleb", "Angeline", "Raven", "Paulina"],
        7: ["Mate", "Vincent", "Eryk", "Emma"],
        8: ["Hielke", "Liss", "Beatris", "Caio", "Sally", "Sanne"],
        9: ["Atlas", "Elli", "Felix", "Diana", "Yash"],
        10: ["Akanksha", "Charlie", "Andrey", "Max", "Hugo", "Al-fatihi"],
        11: ["Misha", "Ioanna", "Ella", "Cristian", "Alicja", "Vanessa"],
        12: ["Luca", "Rachna", "Jelle", "Karolina", "Yuyue", "Alexia"],
    }
    
    for team_number, team_members in teams.items():
        if member_name in team_members:
            return team_number
    return None
