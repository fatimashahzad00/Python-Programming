class GameObject:
    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def move(self, x_amount, y_amount):
        self.x_pos += x_amount
        self.y_pos += y_amount

class Enemy(GameObject):
    def __init__(self, name, x_pos, y_pos, health):
        super().__init__(name, x_pos, y_pos)
        self.health = health

    def takeDamage(self, amount):
        self.health -= amount


gameObject = GameObject('Enemy', 1, 2)
enemy = Enemy("Enemy", 5, 10, 100)


print(gameObject.name)
print(enemy.name)

enemy.takeDamage(20)
print(enemy.health)

