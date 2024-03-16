a = [1400000]

for i in range(50):
    a.append(int(a[i]*1.15))

print(a)