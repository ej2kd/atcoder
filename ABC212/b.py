pin = [int(n) for n in input()]

if len(list(set(pin))) == 1:
    print("Weak")
elif len([pin[i] for i in range(len(pin)-1) if (pin[i+1] - pin[i] == 1) or (pin[i+1] - pin[i] == -9)]) == 3:
    print("Weak")
else:
    print("Strong")