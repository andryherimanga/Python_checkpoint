sequence=input("Enter a list of numbers separated by a comma: ")
seq_split=sequence.split(sep=',')
C=50
H=30
result=[]
for n in range(0,len(seq_split)):
    D=int(seq_split[n])
    Q=round(((2*C*D)/H)**0.5)
    result.append(Q)
str_result=[str(item) for item in result]
final_res=",".join(str_result)
print("The final result from the given formula is :",final_res)
