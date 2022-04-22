lis = ['first',1,'second',2,'third',3,'fourth',4]

# using dictionary comprehension we can convert list into dictionary
dic1 = {lis[i]:lis[i+1] for i in range(0,len(lis),2) }

dic1['fifth'] = 5
print(dic1)