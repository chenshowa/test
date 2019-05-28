natural_numbers_list = [l for l in range(1000)]
output = []

for i in natural_numbers_list:
  if((i%3==0) or (i%5==0)):
    output.append(i)

print(sum(output))  #print 233168