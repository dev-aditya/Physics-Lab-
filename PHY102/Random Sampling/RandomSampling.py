
from numpy import pi,sin
import matplotlib.pyplot as plt
import numpy as np
    
    
class hist_csv(object):
    

    
    def __init__(self,file,values=500,bin_size=1):
        self.values = values
        self.bin_size = bin_size
        self.name = file
        self.file = open(file,'r')
        self.bin_range = np.arange(-9,10,self.bin_size)
        self.point = []
        for i in self.file:
            if i!='\n':
                self.point.append(float(i.strip()))
        self.file.close()
        
        sin = lambda x: 1/(pi*(max(self.point)**2-x**2)**0.5)
        
        plt.figure(figsize=(10,5))
        plt.suptitle(f'Normalized Histogram for {self.values} voltage values')
        plt.title(f'Bin size is {self.bin_size} V')
        plt.hist(self.point[:self.values],bins=self.bin_range,range=None,density=True,weights=None,
                 cumulative=False,bottom=None,histtype='bar',align='mid',
                 orientation='vertical',rwidth=None,log=False,color='slateblue',
                 label='Normalized n(V)',stacked=False)
    
        self.x = np.linspace(-9,10,1000)
    
    
        plt.plot(self.x,[sin(x) for x in self.x],color='green',label='Sine Wave Probability Distribution')
    
        plt.xticks(np.arange(-9,10))
        plt.ylim((0,0.2))
        plt.ylabel('n(V)')
        plt.xlabel('V')
        plt.grid(True)
        plt.legend()
        plt.savefig(f'fig\ {self.bin_size}{self.name} bin size.jpeg')
    

    
class hist_text(object):
    
    
    
    def __init__(self,file,values=500,bin_size=1):
        self.values = values
        self.bin_size = bin_size
        self.name = file
        self.file = open(file,'r')
        self.bin_range = np.arange(-9,10,self.bin_size)
        self.point = []
        for i in self.file:
            self.point.append(float(i.strip('\n')))
        self.file.close()
        
        sin = lambda x: 1/(pi*(max(self.point)**2-x**2)**0.5)
        
        plt.figure(figsize=(10,5))
        plt.suptitle(f'Normalized Histogram for {self.values} voltage values')
        plt.title(f'Bin size is {self.bin_size} V')
        plt.hist(self.point[:self.values],bins=self.bin_range,range=None,density=True,weights=None,
                 cumulative=False,bottom=None,histtype='bar',align='mid',
                 orientation='vertical',rwidth=None,log=False,color='slateblue',
                 label='Normalized n(V)',stacked=False)
    
        self.x = np.linspace(-9,10,1000)
    
    
        plt.plot(self.x,[sin(x) for x in self.x],color='green',label='Sine Wave Probability Distribution')
    
        plt.xticks(np.arange(-9,10))
        plt.ylim((0,0.2))
        plt.ylabel('n(V)')
        plt.xlabel('V')
        plt.grid(True)
        plt.legend()
        plt.savefig(f'fig\ {self.bin_size}{self.name} bin size text.jpeg')
    
    


# In[33]:


for i in [0.1,0.3,0.5,1,1.5]:
    hist_text('Book1.txt',500,i)   #Give the arguments as (file name, no of points, bin size)
    hist_csv('Book1.csv',100,i)
    hist_text('Random AC Sampling.txt',500,i)
    hist_csv('random sampling data.csv',100,i)


# In[8]:


def count(V,N):
    count = 0
    for i in V:
        if i<=N:
            count += 1
    return count
file = open('Book1.txt','r')
point = []
for i in file:
    point.append(float(i.strip('\n')))
file.close()
#point = random.shuffle(point)


file_csv = open("random sampling data.csv",'r')
point_csv = []
for i in file_csv:
    if i!='\n':
        point_csv.append(float(i.strip()))
point_csv
file_csv.close()


list_ = point  #or you can use point_csv list for plotting the wave form

bin_size = 0.5

bin_range = np.arange(-9,10,bin_size)

n_v = []

for i in range(len(bin_range)):
    n_v.append(count(list_,i))

    
V =[]   

for i in n_v:
    V.append(max(point)*np.sin(np.pi*i/500))


# In[9]:



plt.plot(n_v,V,'.',label='Recovered wave form',color='white')
plt.xlabel('N_v')
plt.ylabel('V')
plt.title('Recovered wave form')
plt.legend()
ax = plt.gca()
ax.set_facecolor('black')
plt.savefig('fig\Recovered wave form.jpeg')







