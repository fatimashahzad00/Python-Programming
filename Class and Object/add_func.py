class GameObject:
    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def move(self, x_amount, y_amount):
        self.x_pos += x_amount
        self.y_pos += y_amount

gameObject = GameObject('Enemy', 1, 2)
print(gameObject)
print(gameObject.name)
gameObject.name = "Enemy 1"
print(gameObject.name)

print(gameObject.x_pos)
print(gameObject.y_pos)

gameObject.move(5,10)
print(gameObject.x_pos)
print(gameObject.y_pos)

other_game_object = GameObject("Player", 2, 0 )
print(other_game_object.name)
print(other_game_object.x_pos)
print(other_game_object.y_pos)

one_int = 5
another_int = one_int
print(one_int)
print(another_int)

another_int = 10
print(one_int)
print(another_int)

other_game_object.name = "new Name"
print(other_game_object.name)
print(gameObject.name)