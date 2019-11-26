import matplotlib.pyplot as plt
with open("results1.csv",'r') as f:
	lines = f.readlines()
lines = lines[1:]
steps = []
edgecols = []
selfcols = []
subedgecols = []
subselfcols = []
substeps = []

for line in lines:
	# print(line)
	tokens = line.split(',')
	# print(tokens)
	subedgecols.append(float(tokens[1]))
	subselfcols.append(float(tokens[7]))
	substeps.append(float(tokens[8]))

	if len(substeps) >=  100:
		edgecols.append(sum(subedgecols)/len(subedgecols))
		selfcols.append(sum(subselfcols)/len(subselfcols))
		steps.append(sum(substeps)/len(substeps))
		substeps = []
		subedgecols = []
		subselfcols = []

edgecols.append(sum(subedgecols)/len(subedgecols))
selfcols.append(sum(subselfcols)/len(subselfcols))
steps.append(sum(substeps)/len(substeps))
plt.plot(steps,selfcols,label='baseline')


with open("results2.csv",'r') as f:
	lines = f.readlines()
lines = lines[1:]
steps = []
edgecols = []
selfcols = []
subedgecols = []
subselfcols = []
substeps = []

for line in lines:
	# print(line)
	tokens = line.split(',')
	# print(tokens)
	subedgecols.append(float(tokens[1]))
	subselfcols.append(float(tokens[7]))
	substeps.append(float(tokens[8]))

	if len(substeps) >=  100:
		edgecols.append(sum(subedgecols)/len(subedgecols))
		selfcols.append(sum(subselfcols)/len(subselfcols))
		steps.append(sum(substeps)/len(substeps))
		substeps = []
		subedgecols = []
		subselfcols = []

edgecols.append(sum(subedgecols)/len(subedgecols))
selfcols.append(sum(subselfcols)/len(subselfcols))
steps.append(sum(substeps)/len(substeps))
plt.plot(steps,selfcols,label='punishment on death')
# plt.plot(steps,selfcols,label='self collisions')



plt.ylabel('edge collisions')
plt.xlabel('Steps')
plt.legend()
plt.show()