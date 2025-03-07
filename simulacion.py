from estructura import Building
import random
import json

class ZombieMovementStrategy:
    def move_zombies(self, building):
        raise NotImplementedError("Subclasses must implement move_zombies method")

class ExpansionStrategy(ZombieMovementStrategy):
    def move_zombies(self, building):
        new_zombies = []
        for floor_index, floor in enumerate(building.floors):
            for row_index in range(building.m):
                for col_index in range(building.n):
                    room = floor[row_index][col_index]
                    if room.zombie_count > 0:
                        possible_moves = []
                        if row_index > 0:
                            possible_moves.append((floor_index, row_index - 1, col_index))
                        if row_index < building.m - 1:
                            possible_moves.append((floor_index, row_index + 1, col_index))
                        if col_index > 0:
                            possible_moves.append((floor_index, row_index, col_index - 1))
                        if col_index < building.n - 1:
                            possible_moves.append((floor_index, row_index, col_index + 1))
                        if floor_index > 0:
                            possible_moves.append((floor_index - 1, row_index, col_index))
                        if floor_index < building.x - 1:
                            possible_moves.append((floor_index + 1, row_index, col_index))
                        
                        for move in possible_moves:
                            new_zombies.append(move)
        
        for floor, row, col in new_zombies:
            building.floors[floor][row][col].add_zombie()

class MigrationStrategy(ZombieMovementStrategy):
    def move_zombies(self, building):
        new_zombies = []
        for floor_index, floor in enumerate(building.floors):
            for row_index in range(building.m):
                for col_index in range(building.n):
                    room = floor[row_index][col_index]
                    if room.zombie_count > 0:
                        possible_moves = []
                        if row_index > 0:
                            possible_moves.append((floor_index, row_index - 1, col_index))
                        if row_index < building.m - 1:
                            possible_moves.append((floor_index, row_index + 1, col_index))
                        if col_index > 0:
                            possible_moves.append((floor_index, row_index, col_index - 1))
                        if col_index < building.n - 1:
                            possible_moves.append((floor_index, row_index, col_index + 1))
                        if floor_index > 0:
                            possible_moves.append((floor_index - 1, row_index, col_index)) 
                        if floor_index < building.x - 1:
                            possible_moves.append((floor_index + 1, row_index, col_index))
                        
                        if possible_moves:
                            for _ in range(room.zombie_count):
                                move = random.choice(possible_moves)
                                new_zombies.append(move)
                            room.zombie_count = 0  
        
        for floor, row, col in new_zombies:
            building.floors[floor][row][col].add_zombie()

class Simulation:
    def __init__(self, x, m, n, movement_strategy: ZombieMovementStrategy):
        self.building = Building(x, m, n)
        self.movement_strategy = movement_strategy
        self.turn = 0
    
    def advance_turn(self):
        self.movement_strategy.move_zombies(self.building)
        self.turn += 1
    
    def show_state(self):
        print(f"Turno {self.turn}")
        self.building.show_state()
    
    def reset_building(self):
        self.building.reset_building()
        self.turn = 0
    
    def to_dict(self):
        return {
            "building": self.building.to_dict(),
            "strategy": "expansion" if isinstance(self.movement_strategy, ExpansionStrategy) else "migration",
            "turn": self.turn
        }
    
    def from_dict(self, data):
        self.building = Building.from_dict(data["building"])
        self.turn = data["turn"]
        self.movement_strategy = ExpansionStrategy() if data["strategy"] == "expansion" else MigrationStrategy()

    def save_state(self, filename="simulaciones/estado.json"):
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file)
    
    def load_state(self, filename="simulaciones/estado.json"):
        with open(filename, "r") as file:
            data = json.load(file)
            self.from_dict(data)