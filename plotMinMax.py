
# coding: utf-8

# In[ ]:


def MinMaxPlot():
    f=download(50089, 2015)
    s=download(27211, 2016)
    v=download(50430, 2015)
    
    
    df = f.iloc[:,[0,1,2,3,5,7,9]]
    df1= s.iloc[:,[0,1,2,3,5,7,9]]
    df2= v.iloc[:,[0,1,2,3,5,7,9]]
    
    days=range(0,len(df))
    plt.subplots(figsize=(10,7))
    
    temp_Max = df.iloc[:,[4]]
    plt.subplot(3,1,1)
    ax2=plt.plot(days, temp_Max,label="Maximum Temp")
    temp_Min= df.iloc[:,[5]]
    ax1=plt.plot(days, temp_Min,label="Minimum Temp")
    #plt.xticks([1880,1900,1920,1940,1960,1980,2000],[r'$1880$',r'$1900$',r'$1920$',r'$1940$',r'$1960$',r'$1980$',r'$2000$'])
    plt.xticks([0,30,60,90,120,150,180,210,240,270,300,330,360]),([r'$Jan$',r'$Feb$',r'$Mar$',r'$Apr$',r'$May$',r'$Jun$',r'$Jun2$',r'$Jun3$',r'$Jun4$',r'$Jun5$',r'$Jun6$',r'$Jun7$'])
    plt.xlim([0,360])
    plt.legend()
    
    
    plt.subplot(3,1,2)
    temp_Max1 = df1.iloc[:,[4]]
    temp_Min1= df1.iloc[:,[5]]
    days2 = range(0, len(df1))
    plt.plot(days2, temp_Max1,label="Maximum Temp")
    plt.plot(days2, temp_Min1,label="Minimum Temp")
    #plt.xticks([1880,1900,1920,1940,1960,1980,2000],[r'$1880$',r'$1900$',r'$1920$',r'$1940$',r'$1960$',r'$1980$',r'$2000$'])
    plt.xticks([0,30,60,90,120,150,180,210,240,270,300,330,360]),([r'$Jan$',r'$Feb$',r'$Mar$',r'$Apr$',r'$May$',r'$Jun$',r'$Jun2$',r'$Jun3$',r'$Jun4$',r'$Jun5$',r'$Jun6$',r'$Jun7$'])
    plt.legend()
    
    plt.subplot(3,1,3)
    temp_Max1 = df2.iloc[:,[4]]
    temp_Min1= df2.iloc[:,[5]]
    days3 = range(0, len(df2))
    plt.plot(days3, temp_Max1,label="Maximum Temp")
    plt.plot(days3, temp_Min1,label="Minimum Temp")
    #plt.xticks([1880,1900,1920,1940,1960,1980,2000],[r'$1880$',r'$1900$',r'$1920$',r'$1940$',r'$1960$',r'$1980$',r'$2000$'])
    plt.xticks([0,30,60,90,120,150,180,210,240,270,300,330,360]),([r'$Jan$',r'$Feb$',r'$Mar$',r'$Apr$',r'$May$',r'$Jun$',r'$Jun2$',r'$Jun3$',r'$Jun4$',r'$Jun5$',r'$Jun6$',r'$Jun7$'])
    plt.legend()
    plt.xlim([0,360])
    plt.tight_layout()
    plt.show()
    print(len(df)) 
    
    

