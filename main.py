import matplotlib.pyplot as plt

# import subprocess
# subprocess.run(["python", "input.py"], capture_output=True, text=True)
#
# from output_file import x_input_values,y_input_values,rhs_input_values,obj_input_values
#
#
# print("Imported x values:", x_input_values)
# print("Imported y values:", y_input_values)
# print("Imported rhs values:", rhs_input_values)
# print("Imported obj values:", obj_input_values)

x_input_values=[4,2]
y_input_values=[3,5]
rhs_input_values=[12,10]
#creating graph

x1=[]
y1=[]
x2=[]
y2=[]

#finding x and y values for plotting
for i in range (0,len(x_input_values)):
    x1.append(rhs_input_values[i]/x_input_values[i])
    y1.append(0)
    x2.append(0)
    y2.append(rhs_input_values[i] / y_input_values[i])

#finding max for graph range
xmax=max(x1)
ymax=max(y2)
if(xmax>=ymax):
    max=xmax
else:
    max=ymax

print("point one values to be plotted: ",x1," ",y1)
print("Point two values to be plotted: ",x2," ",y2)

#plotting lines
for i in range (0,len(x_input_values)):
    j=i+1
    string="line: "+str(j)
    region="region: "+str(j)
    plt.plot([x1[i],y1[i]],[x2[i],y2[i]],marker='o',label=string)
    #shading region below line
    #plt.fill_between([x1[i],y1[i]],[x2[i],y2[i]], alpha=0.3,label=region)
    #shading region above line
    #plt.fill_between([x1[i],y1[i]],[x2[i],y2[i]], max, alpha=0.3,  label=region)


plt.xlim([0, max+5])
plt.ylim([0, max+5])
plt.title("Graphically solving LPP")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.show()