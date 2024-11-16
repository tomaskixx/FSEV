# Logic gates implementation using basic functions
def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def XOR(a, b):
    return a != b

def generate_permutations(elements):
    """
    Generate all permutations of a list manually using recursion.
    """
    if len(elements) <= 1:
        return [elements]
    permutations = []
    for i in range(len(elements)):
        rest = elements[:i] + elements[i+1:]
        for p in generate_permutations(rest):
            permutations.append([elements[i]] + p)
    return permutations

def check_conditions(houses):
    """
    Check the conditions of the riddle based on the state of the houses.
    """
    for house in houses:
        if house['color'] == 'green':
            # The green house must be immediately to the left of the white house
            green_index = next((i for i, h in enumerate(houses) if h['color'] == 'green'), None)
            white_index = next((i for i, h in enumerate(houses) if h['color'] == 'white'), None)
            if white_index is None or NOT(AND(green_index is not None, green_index + 1 == white_index)):
                return False
        if house['nationality'] == 'Brit':
            # The Brit lives in the red house
            if house['color'] != 'red':
                return False
        if house['nationality'] == 'Swede':
            # The Swede keeps dogs as pets
            if house['pet'] != 'dog':
                return False
        if house['nationality'] == 'Dane':
            # The Dane drinks tea
            if house['drink'] != 'tea':
                return False
        if house['color'] == 'yellow':
            # The yellow house's owner smokes Dunhill
            if house['cigar'] != 'Dunhill':
                return False
        if house['drink'] == 'milk':
            # Milk is drunk in the middle house
            if houses.index(house) != 2:
                return False
        if house['nationality'] == 'Norwegian':
            # The Norwegian lives in the first house
            if houses.index(house) != 0:
                return False
    
    # The man who smokes Blend lives next to the one who keeps cats
    blend_index = next((i for i, h in enumerate(houses) if h['cigar'] == 'Blend'), None)
    cat_index = next((i for i, h in enumerate(houses) if h['pet'] == 'cat'), None)
    if blend_index is not None and cat_index is not None:
        if NOT(OR(AND(cat_index == blend_index - 1, cat_index >= 0), AND(cat_index == blend_index + 1, cat_index < 5))):
            return False
    
    # The man who keeps horses lives next to the man who smokes Dunhill
    horse_index = next((i for i, h in enumerate(houses) if h['pet'] == 'horse'), None)
    dunhill_index = next((i for i, h in enumerate(houses) if h['cigar'] == 'Dunhill'), None)
    if horse_index is not None and dunhill_index is not None:
        if NOT(OR(AND(horse_index == dunhill_index - 1, horse_index >= 0), AND(horse_index == dunhill_index + 1, horse_index < 5))):
            return False
    
    # The owner who smokes BlueMaster drinks beer
    if any(h['cigar'] == 'BlueMaster' and h['drink'] != 'beer' for h in houses):
        return False
    
    # The German smokes Prince
    if any(h['nationality'] == 'German' and h['cigar'] != 'Prince' for h in houses):
        return False

    # The Norwegian lives next to the blue house
    norwegian_index = next((i for i, h in enumerate(houses) if h['nationality'] == 'Norwegian'), None)
    blue_index = next((i for i, h in enumerate(houses) if h['color'] == 'blue'), None)
    if norwegian_index is not None and blue_index is not None:
        if NOT(OR(AND(blue_index == norwegian_index - 1, blue_index >= 0), AND(blue_index == norwegian_index + 1, blue_index < 5))):
            return False

    # The man who smokes Blend has a neighbor who drinks water
    water_index = next((i for i, h in enumerate(houses) if h['drink'] == 'water'), None)
    if blend_index is not None and water_index is not None:
        if NOT(OR(AND(water_index == blend_index - 1, water_index >= 0), AND(water_index == blend_index + 1, water_index < 5))):
            return False

    return True

def solve_riddle():
    # Initialize possible attributes
    colors = ['red', 'green', 'white', 'yellow', 'blue']
    nationalities = ['Brit', 'Swede', 'Dane', 'Norwegian', 'German']
    drinks = ['tea', 'coffee', 'milk', 'beer', 'water']
    cigars = ['Pall Mall', 'Dunhill', 'Blend', 'BlueMaster', 'Prince']
    pets = ['dog', 'bird', 'cat', 'fish', 'horse']

    # Generate all permutations manually
    color_perms = generate_permutations(colors)
    nationality_perms = generate_permutations(nationalities)
    drink_perms = generate_permutations(drinks)
    cigar_perms = generate_permutations(cigars)
    pet_perms = generate_permutations(pets)

    # Iterate over all possible permutations for each attribute
    for color_perm in color_perms:
        for nationality_perm in nationality_perms:
            for drink_perm in drink_perms:
                for cigar_perm in cigar_perms:
                    for pet_perm in pet_perms:
                        houses = [
                            {'color': color_perm[i], 'nationality': nationality_perm[i], 'drink': drink_perm[i], 'cigar': cigar_perm[i], 'pet': pet_perm[i]}
                            for i in range(5)
                        ]
                        if check_conditions(houses):
                            for i, house in enumerate(houses):
                                print(f"House {i + 1}: {house}")
                            return


# Solve the riddle
solve_riddle()