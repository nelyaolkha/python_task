previous = 0
for i in range(11):
    sum = previous + i
    print("Поточне число", i, "Попереднє число ", previous, " Сума: ", sum)
    previous = i
