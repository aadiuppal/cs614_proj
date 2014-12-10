import matplotlib.pyplot as plt
import os.path

################
"""
f=open("output_new.txt",'r')
param={}
for j in range(1,141):
	next(f)
#f.read(23)
for line in f:
	#f.read()
	if line.split() :
		param.update({line.split()[0]:line.split()[1]})
#print param
f.close()
f=open("output_new.txt",'r')
param1={}
for j in range(1,141):
	next(f)
#f.read(23)
for line in f:
	#f.read()
	if line.split() :
		param1.update({line.split()[0]:line.split()[1]})
print param
"""




################## updating the make file here and running the code varing the params#######################

#basic_comm="./RUNgcc ../../simplesim-3.0/sim-outorder ../../spec2000binaries/gcc00.peak.ev6  -max:inst 50000000 -fastfwd 20000000 -wbuffer 8 -ndbi 32     -dbipolicy m -dramcol 2048 -redir:sim output_new.txt -bpred 2lev -bpred:2lev 1 256 4 0 -bpred:ras 8 -bpred:btb 64 2"
##the varying params
wbuffer=["4","8","16"]
ndbi=["0","8","16","24","32","40","48"]
dbipolicy=['m','l','r']
dramcols=["2048","4096"]
o_file= "output"
cache_nsets=["1024","2048"]
cache_bsize=["64","128"]
benchmark="gcc"
outs=[]


##case1 vary wbuf and ndbi
dpol="l"
dcol="2048"
chn="1024"
chb="64"
outs1=[]



for wbuf in wbuffer:
	for nd in ndbi:
		output_file=o_file+"_"+wbuf+"_"+nd+"_"+dpol+"_"+dcol+"_"+chn+"_"+chb+"_"+benchmark+"_"
		if output_file not in oust1:
			outs1.append(output_file)
		if output_file not in outs:
			outs.append(output_file)
		command = "\n\nsim:\n\t./RUNgcc ../../simplesim-3.0/sim-outorder ../../spec2000binaries/gcc00.peak.ev6  -max:inst 50000000 -fastfwd 20000000 -cache:dl2 ul2:"+chn+":"+chb+":4:l -wbuffer "+wbuf+" -ndbi "+nd+"     -dbipolicy "+dpol+" -dramcol "+dcol+" -redir:sim "+output_file+" -bpred 2lev -bpred:2lev 1 256 4 0 -bpred:ras 8 -bpred:btb 64 2"
		if not os.path.isfile(output_file):
			m=open("Makefile",'w')
			m.write(command)
#			os.system("make run")

print len(outs1)
	

##case2 vary cache_nsets and dbi

dpol="l"
dcol="2048"
chb="64"
wbuf="8"
outs2=[]
for chn in cache_nsets:
	for nd in ndbi:
		output_file=o_file+"_"+wbuf+"_"+nd+"_"+dpol+"_"+dcol+"_"+chn+"_"+chb+"_"+benchmark+"_"
		if output_file not in oust2:
			outs2.append(output_file)
		if output_file not in outs:
			outs.append(output_file)
		command = "\n\nsim:\n\t./RUNgcc ../../simplesim-3.0/sim-outorder ../../spec2000binaries/gcc00.peak.ev6  -max:inst 50000000 -fastfwd 20000000 -cache:dl2 ul2:"+chn+":"+chb+":4:l -wbuffer "+wbuf+" -ndbi "+nd+"     -dbipolicy "+dpol+" -dramcol "+dcol+" -redir:sim "+output_file+" -bpred 2lev -bpred:2lev 1 256 4 0 -bpred:ras 8 -bpred:btb 64 2"
		if not os.path.isfile(output_file):
			m=open("Makefile",'w')
			m.write(command)
#			os.system("make run")
print len(outs2)

##case3 vary cache_bsize and dbi

dpol="l"
dcol="2048"
chn="1024"
wbuf="8"
outs3=[]
for chb in cache_bsize:
	for nd in ndbi:
		output_file=o_file+"_"+wbuf+"_"+nd+"_"+dpol+"_"+dcol+"_"+chn+"_"+chb+"_"+benchmark+"_"
		if output_file not in oust3:
			outs3.append(output_file)
		if output_file not in outs:
			outs.append(output_file)
		command = "\n\nsim:\n\t./RUNgcc ../../simplesim-3.0/sim-outorder ../../spec2000binaries/gcc00.peak.ev6  -max:inst 50000000 -fastfwd 20000000 -cache:dl2 ul2:"+chn+":"+chb+":4:l -wbuffer "+wbuf+" -ndbi "+nd+"     -dbipolicy "+dpol+" -dramcol "+dcol+" -redir:sim "+output_file+" -bpred 2lev -bpred:2lev 1 256 4 0 -bpred:ras 8 -bpred:btb 64 2"
		if not os.path.isfile(output_file):
			m=open("Makefile",'w')
			m.write(command)
#			os.system("make run")
print len(outs3)


##case4 vary dramcols and dbi

dpol="l"
chn="1024"
chb="64"
wbuf="8"
outs4=[]
for dcol in dramcols:
	for nd in ndbi:
		output_file=o_file+"_"+wbuf+"_"+nd+"_"+dpol+"_"+dcol+"_"+chn+"_"+chb+"_"+benchmark+"_"
		if output_file not in oust4:
			outs4.append(output_file)
		if output_file not in outs:
			outs.append(output_file)
		command = "\n\nsim:\n\t./RUNgcc ../../simplesim-3.0/sim-outorder ../../spec2000binaries/gcc00.peak.ev6  -max:inst 50000000 -fastfwd 20000000 -cache:dl2 ul2:"+chn+":"+chb+":4:l -wbuffer "+wbuf+" -ndbi "+nd+"     -dbipolicy "+dpol+" -dramcol "+dcol+" -redir:sim "+output_file+" -bpred 2lev -bpred:2lev 1 256 4 0 -bpred:ras 8 -bpred:btb 64 2"
		if not os.path.isfile(output_file):
			m=open("Makefile",'w')
			m.write(command)
#			os.system("make run")
print len(outs4)

##case5 vary dbipolicy and dbi

dcol="2048"
chn="1024"
chb="64"
wbuf="8"
outs4=[]
for dpol in dbipolicy:
	for nd in ndbi:
		output_file=o_file+"_"+wbuf+"_"+nd+"_"+dpol+"_"+dcol+"_"+chn+"_"+chb+"_"+benchmark+"_"
		if output_file not in oust5:
			outs5.append(output_file)
		if output_file not in outs:
			outs.append(output_file)
		command = "\n\nsim:\n\t./RUNgcc ../../simplesim-3.0/sim-outorder ../../spec2000binaries/gcc00.peak.ev6  -max:inst 50000000 -fastfwd 20000000 -cache:dl2 ul2:"+chn+":"+chb+":4:l -wbuffer "+wbuf+" -ndbi "+nd+"     -dbipolicy "+dpol+" -dramcol "+dcol+" -redir:sim "+output_file+" -bpred 2lev -bpred:2lev 1 256 4 0 -bpred:ras 8 -bpred:btb 64 2"
		if not os.path.isfile(output_file):
			m=open("Makefile",'w')
			m.write(command)
#			os.system("make run")
print len(outs5)

############################done running the codes####################

"""
for o in outs:
	f=open(o,'r')
	param={}
	for j in range(1,141):
        	next(f)
	#f.read(23)
	for line in f:
        	#f.read()
	        if line.split() :
        	        param.update({line.split()[0]:line.split()[1]})
	print param
	f.close()
"""




"""
x=[]
y=[]
for j in param:
#	if j== "sim_CPI":
#	if isinstance(param[j],int):
	x.append(int(param[j]))
#	if j== "sim_IPC":
#		y.append(param[j])
print x
for j in param1:
#	if j== "sim_CPI":
#		x.append(param1[j])
#	if j== "sim_IPC":
	if isinstance(param1[j],(long,int)):
		y.append(param1[j])
plt.hist(x,bins=5)
plt.show()
"""
