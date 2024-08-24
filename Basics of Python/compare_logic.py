# Comparison and Logical Operators

x_position = 10
end_position = 10


is_at_end = x_position == end_position
print(is_at_end)

is_at_halfway = x_position >= end_position / 2
print(is_at_halfway)


not_is_at_end = not is_at_end
print(not_is_at_end)

# score = 10
# is_game_over = score >= 10 and is_at_end
# print(is_game_over)

score = 5
is_game_over = score >= 10 or is_at_end
print(is_game_over)