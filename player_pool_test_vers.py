import random
import os

class UniquePlayerNamesGenerator:
    def __init__(self, data_file='generated_names.txt'):
        self.first_names = [
        'James', 'Robert', 'John', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles', 
        'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Mark', 'Donald', 'Steven', 'Paul', 'Andrew', 'Joshua', 
        'Kenneth', 'Kevin', 'Brian', 'George', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Ryan', 
        'Jacob', 'Gary', 'Nicholas', 'Eric', 'Jonathan', 'Stephen', 'Larry', 'Justin', 'Scott', 'Brandon', 
        'Benjamin', 'Samuel', 'Gregory', 'Frank', 'Alexander', 'Raymond', 'Patrick', 'Jack', 'Dennis', 
        'Jerry', 'Tyler', 'Aaron', 'Jose', 'Adam', 'Henry', 'Nathan', 'Douglas', 'Zachary', 'Peter', 'Kyle', 
        'Walter', 'Ethan', 'Jeremy', 'Harold', 'Keith', 'Christian', 'Roger', 'Noah', 'Gerald', 'Carl', 
        'Terry', 'Sean', 'Austin', 'Arthur', 'Lawrence', 'Jesse', 'Dylan', 'Bryan', 'Joe', 'Jordan', 'Billy', 
        'Bruce', 'Albert', 'Willie', 'Gabriel', 'Logan', 'Alan', 'Juan', 'Wayne', 'Roy', 'Ralph', 'Randy', 
        'Eugene', 'Vincent', 'Russell', 'Elijah', 'Louis', 'Bobby', 'Philip', 'Johnny'
        ]
        self.surnames = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", 
        "Hernandez", "Lopez", "Gonzales", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", 
        "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", 
        "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", 
        "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", 
        "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy", "Cook", 
        "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", 
        "Kim", "Cox", "Ward", "Richardson", "Watson", "Brooks", "Chavez", "Wood", "James", "Bennet", "Gray", "Mendoza", 
        "Ruiz", "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez"
        ]
        self.positions = [
            'QB', 'HB', 'FB', 'WR', 'TE', 'LT', 'LG', 'C', 'RG', 'RT',
            'DE', 'DT', 'WLB', 'SLB', 'MLB', 'CB', 'FS', 'SS', 'K', 'P', 'LS'
        ]
        self.position_percentages = {
            'QB': 4.166666667, 'HB': 5.833333333, 'FB': 2.5, 'WR': 12.5,
            'TE': 7.5, 'LT': 3.333333333, 'LG': 3.333333333, 'C': 3.333333333,
            'RG': 3.333333333, 'RT': 3.333333333, 'DE': 8.333333333,
            'DT': 7.5, 'WLB': 5, 'SLB': 5, 'MLB': 5, 'CB': 8.333333333,
            'FS': 3.333333333, 'SS': 3.333333333, 'K': 1.666666667, 'P': 1.666666667, 'LS': 1.666666667
        }
        self.min_positions = {'K': 2, 'P': 2, 'LS': 2, 'FB': 2, 'QB': 4, 'HB': 5, 'WR': 6, 'TE': 4, 'LT': 4, 'LG': 4, 'C': 4, 'RG': 4, 'RT': 4,
             'DE': 6, 'DT': 5, 'WLB': 4, 'MLB': 4, 'SLB': 4, 'CB': 6, 'FS': 4, 'S': 4
        }
        self.max_positions = {'K': 3, 'P': 3, 'LS': 3, 'FB': 4, 'QB': 6, 'HB': 8, 'WR': 15, 'TE': 10, 'LT': 5, 'LG': 5, 'C': 5, 'RG': 5, 'RT': 5,
             'DE': 10, 'DT': 9, 'WLB': 4, 'MLB': 4, 'SLB': 4, 'CB': 6, 'FS': 4, 'SS': 4
        }
        self.data_file = data_file
        self.generated_names = set()

        # Load previously generated names from the file
        self.load_generated_names()

    def load_generated_names(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.generated_names = set(file.read().splitlines())

    def save_generated_names(self):
        with open(self.data_file, 'w') as file:
            file.write('\n'.join(self.generated_names))

    def assign_position(self):
        total_percentage = 0
        position_weights = {pos: 0 for pos in self.positions}
        
        # Ensure minimum counts for K, P, LS, FB, SS
        for pos, min_count in self.min_positions.items():
            max_count = self.max_positions.get(pos, 2)
            count = max(min_count, min(max_count, self.min_positions.get(pos, 2)))
            while position_weights.get(pos, 0) < count:
                position = random.choice(self.positions)
                position_weights[position] = position_weights.get(position, 0) + 1

        # Assign names to other positions with at least 4 names
        for pos in self.positions:
            if pos not in self.min_positions:
                while position_weights[pos] < 4:
                    position_weights[pos] += 1

        # Assign positions based on percentages
        while total_percentage < 100:
            position = random.choice(self.positions)
            if position in self.max_positions and position_weights[position] == self.max_positions[position]:
                continue
            position_weights[position] += 1
            total_percentage = sum(self.position_percentages[pos] * position_weights[pos] for pos in self.positions)

        return position


    def generate_unique_player_name(self):
        position = self.assign_position()
        first_name = random.choice(self.first_names)
        surname = random.choice(self.surnames)
        player_name = f"{position} {first_name} {surname}"

        if player_name not in self.generated_names:
            self.generated_names.add(player_name)
            self.save_generated_names()
            return player_name

# Example usage:
generator = UniquePlayerNamesGenerator()

# Generate 10 unique player names
for _ in range(120):
    player_name = generator.generate_unique_player_name()
    print(player_name)



##import random
##import os
##
##class UniquePlayerNamesGenerator:
##    def __init__(self, data_file='generated_names.txt'):
##        self.first_names = [
##        'James', 'Robert', 'John', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles', 
##        'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Mark', 'Donald', 'Steven', 'Paul', 'Andrew', 'Joshua', 
##        'Kenneth', 'Kevin', 'Brian', 'George', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Ryan', 
##        'Jacob', 'Gary', 'Nicholas', 'Eric', 'Jonathan', 'Stephen', 'Larry', 'Justin', 'Scott', 'Brandon', 
##        'Benjamin', 'Samuel', 'Gregory', 'Frank', 'Alexander', 'Raymond', 'Patrick', 'Jack', 'Dennis', 
##        'Jerry', 'Tyler', 'Aaron', 'Jose', 'Adam', 'Henry', 'Nathan', 'Douglas', 'Zachary', 'Peter', 'Kyle', 
##        'Walter', 'Ethan', 'Jeremy', 'Harold', 'Keith', 'Christian', 'Roger', 'Noah', 'Gerald', 'Carl', 
##        'Terry', 'Sean', 'Austin', 'Arthur', 'Lawrence', 'Jesse', 'Dylan', 'Bryan', 'Joe', 'Jordan', 'Billy', 
##        'Bruce', 'Albert', 'Willie', 'Gabriel', 'Logan', 'Alan', 'Juan', 'Wayne', 'Roy', 'Ralph', 'Randy', 
##        'Eugene', 'Vincent', 'Russell', 'Elijah', 'Louis', 'Bobby', 'Philip', 'Johnny'
##        ]
##        self.surnames = [
##        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", 
##        "Hernandez", "Lopez", "Gonzales", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", 
##        "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", 
##        "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", 
##        "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", 
##        "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy", "Cook", 
##        "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", 
##        "Kim", "Cox", "Ward", "Richardson", "Watson", "Brooks", "Chavez", "Wood", "James", "Bennet", "Gray", "Mendoza", 
##        "Ruiz", "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez"
##        ]
##        self.positions = [
##            'FS', 'SS', 'CB', 'DT', 'DE', 'FB', 'K', 'WLB', 'MLB', 'SLB',
##            'LS', 'P', 'QB', 'HB', 'TE', 'WR', 'LT', 'LG', 'C', 'RG', 'RT'
##        ]
##        self.position_percentages = {
##            'FS': 3.333333333, 'SS': 3.333333333, 'CB': 8.333333333,
##            'DT': 7.5, 'DE': 8.333333333, 'FB': 2.5, 'K': 1.666666667,
##            'WLB': 5, 'MLB': 5, 'SLB': 5, 'LS': 1.666666667, 'P': 1.666666667,
##            'QB': 4.166666667, 'HB': 5.833333333, 'TE': 7.5, 'WR': 12.5,
##            'LT': 3.333333333, 'LG': 3.333333333, 'C': 3.333333333,
##            'RG': 3.333333333, 'RT': 3.333333333
##        }
##        self.data_file = data_file
##        self.generated_names = set()
##
##        # Load previously generated names from the file
##        self.load_generated_names()
##
##    def load_generated_names(self):
##        if os.path.exists(self.data_file):
##            with open(self.data_file, 'r') as file:
##                self.generated_names = set(file.read().splitlines())
##
##    def save_generated_names(self):
##        with open(self.data_file, 'w') as file:
##            file.write('\n'.join(self.generated_names))
##
##    def assign_position(self):
##        total_percentage = 0
##        position_weights = {}
##        
##        # Ensure minimum counts for K, P, LS, FB
##        min_positions = {'K': 2, 'P': 2, 'LS': 2, 'FB': 2}
##
##        # Assign positions based on percentages
##        while total_percentage < 120:
##            position = random.choice(self.positions)
##            if position in position_weights:
##                if position in min_positions and position_weights[position] < min_positions[position]:
##                    continue
##                position_weights[position] += 1
##            else:
##                position_weights[position] = 1
##
##            total_percentage = sum(self.position_percentages[pos] * position_weights[pos] for pos in position_weights)
##
##        return position
##
##    def generate_unique_player_name(self):
##        position = self.assign_position()
##        first_name = random.choice(self.first_names)
##        surname = random.choice(self.surnames)
##        player_name = f"{position} {first_name} {surname}"
##
##        if player_name not in self.generated_names:
##            self.generated_names.add(player_name)
##            self.save_generated_names()
##            return player_name
##
### Example usage:
##generator = UniquePlayerNamesGenerator()
##
### Generate 10 unique player names
##for _ in range(120):
##    player_name = generator.generate_unique_player_name()
##    print(player_name)




##import random
##import os
##
##class UniquePlayerNamesGenerator:
##    def __init__(self, data_file='generated_names.txt'):
##        self.first_names = [
##        'James', 'Robert', 'John', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles', 
##        'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Mark', 'Donald', 'Steven', 'Paul', 'Andrew', 'Joshua', 
##        'Kenneth', 'Kevin', 'Brian', 'George', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Ryan', 
##        'Jacob', 'Gary', 'Nicholas', 'Eric', 'Jonathan', 'Stephen', 'Larry', 'Justin', 'Scott', 'Brandon', 
##        'Benjamin', 'Samuel', 'Gregory', 'Frank', 'Alexander', 'Raymond', 'Patrick', 'Jack', 'Dennis', 
##        'Jerry', 'Tyler', 'Aaron', 'Jose', 'Adam', 'Henry', 'Nathan', 'Douglas', 'Zachary', 'Peter', 'Kyle', 
##        'Walter', 'Ethan', 'Jeremy', 'Harold', 'Keith', 'Christian', 'Roger', 'Noah', 'Gerald', 'Carl', 
##        'Terry', 'Sean', 'Austin', 'Arthur', 'Lawrence', 'Jesse', 'Dylan', 'Bryan', 'Joe', 'Jordan', 'Billy', 
##        'Bruce', 'Albert', 'Willie', 'Gabriel', 'Logan', 'Alan', 'Juan', 'Wayne', 'Roy', 'Ralph', 'Randy', 
##        'Eugene', 'Vincent', 'Russell', 'Elijah', 'Louis', 'Bobby', 'Philip', 'Johnny'
##        ]
##        self.surnames = [
##        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", 
##        "Hernandez", "Lopez", "Gonzales", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", 
##        "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", 
##        "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", 
##        "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", 
##        "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy", "Cook", 
##        "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", 
##        "Kim", "Cox", "Ward", "Richardson", "Watson", "Brooks", "Chavez", "Wood", "James", "Bennet", "Gray", "Mendoza", 
##        "Ruiz", "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez"
##        ]
##        
##        self.data_file = data_file
##        self.generated_names = set()
##
##        # Load previously generated names from the file
##        self.load_generated_names()
##
##    def load_generated_names(self):
##        if os.path.exists(self.data_file):
##            with open(self.data_file, 'r') as file:
##                self.generated_names = set(file.read().splitlines())
##
##    def save_generated_names(self):
##        with open(self.data_file, 'w') as file:
##            file.write('\n'.join(self.generated_names))
##
##    def assign_position(self):
##        positions = [
##            'FS', 'SS', 'CB', 'DT', 'DE', 'FB', 'K', 'WLM', 'MLB', 'SLB',
##            'LS', 'P', 'QB', 'RB', 'TE', 'WR', 'LT', 'LG', 'C', 'RG', 'RT'
##        ]
##        probabilities = [
##            3.333333333, 3.333333333, 8.333333333, 7.5, 8.333333333, 2.5,
##            1.666666667, 5, 5, 5, 1.666666667, 1.666666667, 4.166666667,
##            5.833333333, 7.5, 12.5, 3.333333333, 3.333333333, 3.333333333,
##            3.333333333, 3.333333333
##        ]
##
##        return random.choices(positions, weights=probabilities)[0]
##
##    def generate_unique_player_name(self):
##        while True:
##            first_name = random.choice(self.first_names)
##            surname = random.choice(self.surnames)
##            position = self.assign_position()
##            player_name = f"{position} {first_name} {surname}"
##
##            if player_name not in self.generated_names:
##                self.generated_names.add(player_name)
##                self.save_generated_names()
##                return player_name
##
### Example usage:
##generator = UniquePlayerNamesGenerator()
##
### Generate 10 unique player names with positions
##for _ in range(120):
##    player_name = generator.generate_unique_player_name()
##    print(player_name)
