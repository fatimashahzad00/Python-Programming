class GameObject:
    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

gameObject = GameObject('Enemy', 1, 2)
print(gameObject)
print(gameObject.name)
gameObject.name = "Enemy 1"
print(gameObject.name)
        