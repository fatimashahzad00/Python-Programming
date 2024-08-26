position = 0
end_position = 10
enemy_position = 15

while position < end_position:
    position += 1
    print(position)
    if position == enemy_position:
        print("Game Over!")
        break

if position == end_position:
 print("You have reached the end")