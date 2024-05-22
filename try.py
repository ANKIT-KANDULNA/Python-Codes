results={"akash":240,"bharti":340,"chetna":350,"deepak":280,"ishita":370}
print(results.values())

for i in results:
    if results[i]>250:
        print(i)
    
results["chetna"]=450
print(results)

s=0
for j in results:
    s=s+results[i]

avg=s/len(results)
print(avg)

results.pop("chetna")
print(results)
