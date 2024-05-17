# Health management module
class HealthModule:
    def __init__(self, max_health):
        self.max_health = max_health
        self.current_health = max_health

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def is_alive(self):
        return self.current_health > 0



class ShotgunModule:
    pass


class StickModule:
    pass


class DefendModule:
    pass
