"""
Goal :

"["1","10"]"
["1","1","0"]

"""

listboostBought = "['2', '3', '4']"

print(listboostBought)
if listboostBought == "[]":
    listboostBought = []
else:
    listboostBought = listboostBought[2:-2]
    listboostBought = listboostBought.split("""', '""")

print(listboostBought)
print(type(listboostBought))
