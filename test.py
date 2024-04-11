"""
Goal :

"["1","10"]"
["1","1","0"]

"""

listboostBought = "[]"

print(listboostBought)
if listboostBought == "[]":
    listboostBought = []
else:
    listboostBought = listboostBought[2:-2]
    listboostBought.split("', '")

print(listboostBought)
print(type(listboostBought))