# Health management module
class HealthModule:
    def __init__(self, initial_health):
        self.max_health = initial_health
        self.current_health = initial_health

    def take_damage(self, amount):
        self.current_health = max(0, self.current_health - amount)

    def heal(self, amount):
        self.current_health = min(self.max_health, self.current_health + amount)


class ShotgunModule:
    pass


class StickModule:
    pass


class DefendModule:
    pass
