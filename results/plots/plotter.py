import matplotlib.pyplot as plt
with open("results1.csv",'r') as f:
	lines = f.readlines()
lines = lines[1:]
steps = []
lengths = []
sublengths = []
substeps = []
for line in lines:
	# print(line)
	tokens = line.split(',')
	# print(tokens)
	sublengths.append(float(tokens[0]))
	substeps.append(float(tokens[8]))

	if len(substeps) >=  100:
		print(substeps)
		print(sublengths)
		
		lengths.append(sum(sublengths)/len(sublengths))
		steps.append(sum(substeps)/len(substeps))
		substeps = []
		sublengths = []

lengths.append(sum(sublengths)/len(sublengths))
steps.append(sum(substeps)/len(substeps))
plt.plot(steps,lengths,label='baseline')

with open("results2.csv",'r') as f:
	lines = f.readlines()
lines = lines[1:]
steps = []
lengths = []
sublengths = []
substeps = []
for line in lines:
	# print(line)
	tokens = line.split(',')
	# print(tokens)
	sublengths.append(float(tokens[0]))
	substeps.append(float(tokens[8]))

	if len(substeps) >=  100:
		print(substeps)
		print(sublengths)
		
		lengths.append(sum(sublengths)/len(sublengths))
		steps.append(sum(substeps)/len(substeps))
		substeps = []
		sublengths = []

lengths.append(sum(sublengths)/len(sublengths))
steps.append(sum(substeps)/len(substeps))
plt.plot(steps,lengths,label='punishment on death')

with open("results3.txt",'r') as f:
	lines = f.readlines()
lines = lines[40:]
steps = []
lengths = []
sublengths = []
substeps = []
for line in lines:
	# print(line)
	tokens = line.split()
	# print(tokens)
	sublengths.append(float(tokens[13]))
	substeps.append(float(tokens[2]))

	if len(substeps) >=  100:
		print(substeps)
		print(sublengths)
		
		lengths.append(sum(sublengths)/len(sublengths))
		steps.append(sum(substeps)/len(substeps))
		substeps = []
		sublengths = []

lengths.append(sum(sublengths)/len(sublengths))
steps.append(sum(substeps)/len(substeps))
plt.plot(steps,lengths,label='path optimization')

with open("results4.csv",'r') as f:
	lines = f.readlines()
lines = lines[1:]
steps = []
lengths = []
sublengths = []
substeps = []
for line in lines:
	# print(line)
	tokens = line.split(',')
	# print(tokens)
	sublengths.append(float(tokens[0]))
	substeps.append(float(tokens[8]))

	if len(substeps) >=  100:
		print(substeps)
		print(sublengths)
		
		lengths.append(sum(sublengths)/len(sublengths))
		steps.append(sum(substeps)/len(substeps))
		substeps = []
		sublengths = []

lengths.append(sum(sublengths)/len(sublengths))
steps.append(sum(substeps)/len(substeps))
plt.plot(steps,lengths,label='timeout')




plt.ylabel('Avg. Length')
plt.xlabel('Steps')
plt.legend()
plt.show()