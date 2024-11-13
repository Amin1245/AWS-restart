file = open("results.txt", "w")


for num in range(1, 251):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            file.write(str(num) + "\n")

file.close()

print("Prime numbers have been saved to results.txt.")
