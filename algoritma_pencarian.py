import random

# Dictionary berisi data hero beserta atributnya
heroes = {
    "Alucard": {"role": "Fighter", "type": "Physical"},
    "Lancelot": {"role": "Assassin", "type": "Physical"},
    "Gord": {"role": "Mage", "type": "Magic"},
    "Lunox": {"role": "Mage", "type": "Magic"},
    "Franco": {"role": "Tank", "type": "Physical"},
    "Frendrin": {"role": "Tank", "type": "Physical"},
    "Lylia": {"role": "Mage", "type": "Magic"},
    "Yu Zhong": {"role": "Fighter", "type": "Physical"},
    "Karina": {"role": "Assassin", "type": "Magic"},
    "Arlot": {"role": "Fighter", "type" : "Physical"},
    "Ruby": {"role": "Fighter", "type" : "Physical"},
    "Karie": {"role": "Marksman", "type": "Physical"},
    "Hanabi": {"role": "Marksman", "type": "Physical"},
    "Layla": {"role": "Marksman", "type": "Phsyical"}
    # Tambahkan hero lainnya beserta atributnya
}

# Fungsi untuk mencari komposisi hero terbaik
def find_best_composition(team_size, roles_needed, types_needed):
    # Menginisialisasi semua kombinasi hero yang mungkin
    all_combinations = []
    for hero1 in heroes:
        for hero2 in heroes:
            if hero2 != hero1:
                for hero3 in heroes:
                    if hero3 != hero1 and hero3 != hero2:
                        for hero4 in heroes:
                            if hero4 != hero1 and hero4 != hero2 and hero4 != hero3:
                                for hero5 in heroes:
                                    if hero5 != hero1 and hero5 != hero2 and hero5 != hero3 and hero5 != hero4:
                                        all_combinations.append([hero1, hero2, hero3, hero4, hero5])
    
    # Mengacak urutan kombinasi hero
    random.shuffle(all_combinations)
    
    # Memilih kombinasi terbaik dari kombinasi yang sudah diacak
    best_score = -1
    best_composition = []
    for composition in all_combinations:
        score = calculate_score(composition, roles_needed, types_needed)
        if score > best_score:
            best_score = score
            best_composition = composition
    
    return best_composition

# Fungsi untuk menghitung skor komposisi hero
def calculate_score(composition, roles_needed, types_needed):
    score = 0
    for hero in composition:
        # Menambahkan skor berdasarkan kebutuhan role
        if heroes[hero]["role"] in roles_needed:
            score += 1
        # Menambahkan skor berdasarkan kebutuhan tipe
        if heroes[hero]["type"] in types_needed:
            score += 1
    return score

# Main program
if __name__ == "__main__":
    team_size = 5  # Jumlah hero dalam satu tim
    roles_needed = ["Tank", "Mage", "Fighter", "Assassin", "Marksman"]  # Role yang diperlukan dalam tim
    types_needed = ["Magic", "Physical", "Marksman", "Tank", "Assassin"]  # Tipe hero yang diperlukan dalam tim

    best_composition = find_best_composition(team_size, roles_needed, types_needed)
    print("Komposisi terbaik (urutan acak):", best_composition)
