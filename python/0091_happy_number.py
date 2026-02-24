n = int(input("Enter a number: "))
output_list = [n]
sum = 0
while sum not in output_list[0:-1]:
    sum=0
    for i in range(len(str(output_list[-1]))):
        sum+=((int(str(output_list[-1])[i]))**2)
    output_list.append(sum)
if 1 in output_list: print(f"{n} is a Happy number.")
else: print(f"{n} is not a Happy number.")