import pyproj

t = open("GO_CONS_SST_PRD_2I_20130901T205944_20130903T025943_0001.IDF")
l = t.readlines()
t.close()

tab = []

lon=[]
lat=[]
alt=[]

x=[]
y=[]
z=[]


c = []
cl = []

#print(l[24][0])

for i in range(0,len(l)):
    if l[i][0] == "P":
        cl.append(l[i])

        
for i in range(0,len(cl)):
    c = cl[i].split()

    x.append(float(c[1]))
    y.append(float(c[2]))
    z.append(float(c[3]))

    
        
#print(x)

ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')

for i in range(0,len(x)):
    xi, yi, zi = pyproj.transform(ecef, lla, x[i], y[i], z[i], radians= False)
    lon.append(xi)
    lat.append(yi)
    alt.append(zi)

print (lon)
print (lat)
print (alt)
