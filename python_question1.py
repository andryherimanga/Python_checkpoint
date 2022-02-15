result_list=[]
for number in range(2000,3201):
    if number%7==0:
        if number%5!=0:
            result=number
            result_list.append(result)
print(result_list)