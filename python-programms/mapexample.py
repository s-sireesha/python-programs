import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,7,6])   #the line comes default in staright line
plt.plot([30,35,40,45],[40000,50000,45000,60000],"--",color="red")   #the line comes in dashes line
plt.plot([30,35,40,45],[40000,50000,45000,60000],"oo")   #the line comes in dot line
plt.xlabel("AGE")
plt.ylabel("INCOME")
plt.title("SAMPLE GRAPH")
plt.show()
