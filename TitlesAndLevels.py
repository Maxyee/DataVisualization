import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x,y, label='First Line') # this is the label
plt.plot(x2,y2, label='Second Line') # this is another label
plt.xlabel('Plot Number')
plt.ylabel('important var')

plt.title('Interesting Graph\nCheck it out') # here is the graph title
plt.legend()
plt.show()
