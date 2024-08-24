# cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "LosAngeles", "Seattle"]
# print("Welcome to " + cities[3])

# mixed_things = [1, "Bob", "Now is"]
# print(mixed_things[0])

enemy_positions = [5, 10, 15]
enemy_positions = [5, 10, 15, 20]
print(enemy_positions)

print(len(enemy_positions))
print(enemy_positions[3])

enemy_positions[0] = 6
print(enemy_positions)

print(enemy_positions[0:2])

enemy_positions.append(25)
print(enemy_positions)

enemy_positions.insert(1,9)
print(enemy_positions)

enemy_positions.remove(6)
print(enemy_positions)

del(enemy_positions[2])
print(enemy_positions)