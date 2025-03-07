class Sensor:
    def __init__(self):
        self.state = "normal"
    
    def activate_alert(self):
        self.state = "alert"
    
    def reset(self):
        self.state = "normal"

class Room:
    def __init__(self):
        self.zombie_count = 0
        self.sensor = Sensor()

    def add_zombie(self, count=1):
        self.zombie_count += count
        self.sensor.activate_alert()
    
    def remove_zombies(self):
        self.zombie_count = 0
        self.sensor.reset()

    def __str__(self):
        return f"Zombies: {self.zombie_count}" if self.zombie_count > 0 else "Empty"

class Building:
    def __init__(self, x, m, n):
        self.x = x
        self.m = m
        self.n = n
        self.floors = [[[Room() for _ in range(n)] for _ in range(m)] for _ in range(x)]
    
    def show_state(self):
        for floor_index, floor in enumerate(self.floors):
            print(f"Floor {floor_index}:")
            for row in floor:
                print(" ".join("Z" if room.zombie_count > 0 else "-" for room in row))
            print("")

    def reset_building(self):
        for floor in self.floors:
            for row in floor: 
                for room in row:
                    room.remove_zombies()
                    room.sensor.reset()

    def to_dict(self):
        return {
            "x": self.x,
            "m": self.m,
            "n": self.n,
            "floors": [[[room.zombie_count for room in row] for row in floor] for floor in self.floors]
        }
    
    @classmethod
    def from_dict(cls, data):
        print(cls)
        building = cls(data["x"], data["m"], data["n"])
        print(building)
        print(data)
        for floor_index, floor in enumerate(data["floors"]):
            for row_index, row in enumerate(floor):
                for col_index, zombie_count in enumerate(row):
                    building.floors[floor_index][row_index][col_index].zombie_count = zombie_count
        return building