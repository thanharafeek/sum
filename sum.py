num=12345
sum=0
for i in range(len(str(num))):   #integer convert to string to find the length
    temp=num%10       #12345%10=5 it gives 5 to sum
    num=num//10
    sum+=temp          #sum will add that
print(sum)              #print sum=15