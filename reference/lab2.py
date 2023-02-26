

np.random.seed(12023)

def Gen_RandLine(length,dims=2):
    lineData = np.empty((dims,length))
    lineData[:,0] = np.random.rand(dims)
    for i in range(1,length):
        step = ((np.random.rand(dims)-0.5)*0.1)
        lineData[:,index] = lineData[:,index-1]+step
        
    return lineData

def update_lines(num,dataLines,lines):
    for line,data in zip(lines,dataLines):
        line.set_data(data[0:2,:num])
        line.set_3d_properties(data[2,:num])
    return lines

def update_lines(num,dataLines,lines):
    for line, data in zip(lines,dataLines):
        line.set_data(data[0:2,:num])
        line.set_3d_properties(data[2,num])
    return lines

fig = plg.figure()
ax = p3.Axes3D(fig)

# data = []
# for i in range(50):
#     data.append(Gen_RandLine(25,3))
data = [Gen_RandLine(25,3) for i in range(50)]

lines = [ax.plot(data)]