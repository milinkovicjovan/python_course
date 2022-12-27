# 1
names = ['Max', 'Anna', 'Manuel', 'Chris', 'Stephen']

for name in names:
    print(name)
    print(len(name))

# 2
print('-' * 30)
for name in names:
    if len(name) > 5:
        print(name)
        print(len(name))

# 3
print('-' * 30)
for name in names:
    if len(name) > 5 and ('N' in name or 'n' in name):
        print(name)
        print(len(name))

# 4
print('-' * 30)
while len(names) >= 1:
    print(names.pop())

print(names)
