
while True:
    user_input = input('Type "q" or "Q" to quit: ')
    if user_input.upper() == "Q":
        break

for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)
