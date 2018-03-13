
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

cmap = matplotlib.cm.Dark2
subjects = ("Group-A", "Group-B", "Group-C", "Group-D", "Group-E", "Group-F")
data = [
	[0.0532, 0.0394, 0.0454, 0.0705, 0.1208, 0.0531],
	[0.1037, 0.0783, 0.1159, 0.1024, 0.0879, 0.1132],
	[0.1518, 0.1199, 0.1599, 0.1561, 0.2345, 0.1287],
	[0.0818, 0.1097, 0.1126, 0.0724, 0.0396, 0.0978],
	[0.2211, 0.2192, 0.2097, 0.1815, 0.1461, 0.1829],
	[0.1403, 0.1109, 0.1169, 0.1413, 0.1849, 0.1396],
	[0.0225, 0.0463, 0.0362, 0.0298, 0.0064, 0.0334],
	[0.0745, 0.1389, 0.0844, 0.0885, 0.0339, 0.0861],
	[0.1023, 0.0991, 0.0859, 0.0993, 0.0745, 0.1034],
	[0.0488, 0.0493, 0.0339, 0.0586, 0.0714, 0.0623]
]

bars = ("01", "02","03","04","05","06","07","08","09","10")


# number of bars per subject
n = 10
# x-positions for the bars
x = np.arange(len(subjects))

# width for plotting (number of bars)
width = 1.0/(1+n) 

for i, data[i] in enumerate(data):
    plt.bar(x+i*width, data[i], width, color = cmap(i / float(10)) )
    plt.legend(bars, ncol=1, loc = 'center left', shadow=True, prop={'size':11}, fancybox=True, bbox_to_anchor = (1.0, 0.5))

# add labels
plt.grid(color = '#778899', linestyle = '-.', linewidth=0.2)
plt.xticks(x+n/2.* width, subjects, fontsize = 9, rotation = 20)
plt.ylabel('Relative Frequency.', fontsize = 9)
plt.title('Plot Title.', fontsize = 10)
# plt.savefig('GroupBarChart.png', dpi = 500)
plt.show()