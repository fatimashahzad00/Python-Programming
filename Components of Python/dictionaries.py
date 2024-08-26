# Dictionaries are like objects which has key value  pairs

actions = {'r': 1, "l":-1}
print(actions)

print(actions["r"])
print(actions.get("g"))

actions["r"] = 2
actions["u"] = 1
print(actions)

print(actions.keys())
print(actions.values())
print(actions.items())

del(actions["u"])
print(actions)

actions.pop("r")
print(actions)

print("l" in actions)


# How to code one
customer_29876 = {"first name": "David", "lastname": "Elliott", "address": "4803 Wellesley St."}


# How to pick information out of them
address_of_customer = customer_29876["address"]
print(address_of_customer)


# The versatility of keys and values
rankings = {5: "Finland", 2: "Norway", 3: "Sweden",
7: "Iceland"}
second_ranking_country = rankings[2]
print(second_ranking_country)
print(rankings[5])

country_ranks_so_far = {"Finland": 5, "Norway": 2,
"Sweden": 3, "Iceland": 7}
norway_ranking = country_ranks_so_far["Norway"]
print(norway_ranking)
print(country_ranks_so_far["Sweden"])


things_to_remember = {
 0: "the lowest number",
 "a dozen": 12,
 "snake eyes": "a pair of ones",
 13: "a baker's dozen",
 }


# Adding items
customer_29876["city"] = "Toronto"
print(customer_29876)

things_to_remembers = {}
things_to_remembers[0] = "the lowest number"
things_to_remembers["a dozen"] = 12
print(things_to_remembers)