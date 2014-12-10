import matplotlib.pyplot as plt
import os.path
import csv

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
		if output_file not in outs1:
			outs1.append(output_file)
		if output_file not in outs:
			outs.append(output_file)
		command = "\n\nsim:\n\t./RUNgcc ../../simplesim-3.0/sim-outorder ../../spec2000binaries/gcc00.peak.ev6  -max:inst 50000000 -fastfwd 20000000 -cache:dl2 ul2:"+chn+":"+chb+":4:l -wbuffer "+wbuf+" -ndbi "+nd+"     -dbipolicy "+dpol+" -dramcol "+dcol+" -redir:sim "+output_file+" -bpred 2lev -bpred:2lev 1 256 4 0 -bpred:ras 8 -bpred:btb 64 2"+"\n\ncompile:\n\t$(MAKE) -C ../../simplesim-3.0 clean\n\t$(MAKE) -C ../../simplesim-3.0 config-alpha\n\t$(MAKE) -C ../../simplesim-3.0\n\nrun: compile sim"
		if not os.path.isfile(output_file):
			m=open("Makefile",'w')
			m.write(command)
			m.close()
			os.system("make run")

#			print len(outs1)
"""
param={}
for o in outs1:
        f=open(o,'r')
        #param={}
        for j in range(1,141):
                next(f)
        #f.read(23)
        for line in f:
                #f.read()
                if line.split() :
                        param.update({line.split()[0]:line.split()[1]})
        f.close()
        print param
        writer = csv.writer(open(o+".csv", 'wb'))
	writer.writerow(["ndbi",param])
        for key, value in param.items():
                if value.replace('.','',1).isdigit():
                        writer.writerow([key, value])



"""	
"""
while 1:
	var= raw_input("this is case 1 #####wbuffer vs ndbi ##########\n enter param:")
	if var == "next":
		break
	if not os.path.isfile("case1_"+var+"_ndbi_wbuf_"+".csv"):
		writer1 = csv.writer(open("case1_"+var+"_ndbi_wbuf_"+".csv", 'wb'))
		writer1.writerow([var,"ndbi","wbuf"])
		for o in outs1:
			f=open(o,'r')
			param={}
			for j in range(1,141):
	        		next(f)
			#f.read(23)
			for line in f:
		        	#f.read()
			        if line.split() :
		        	        param.update({line.split()[0]:line.split()[1]})
			f.close()
	#		print param
		
			for key,value in param.items():
#				print key
				if key == var :
					#print key
					n=o.find("_")
					l=o.find("_",7)
					m=o.find("_",l+1)
					writer1.writerow([value,o[l+1:m],o[n+1:l]])


"""

##case2 vary cache_nsets and dbi

dpol="l"
dcol="2048"
chb="64"
wbuf="8"
outs2=[]
for chn in cache_nsets:
	for nd in ndbi:
		output_file=o_file+"_"+wbuf+"_"+nd+"_"+dpol+"_"+dcol+"_"+chn+"_"+chb+"_"+benchmark+"_"
		if output_file not in outs2:
			outs2.append(output_file)
		if output_file not in outs:
			outs.append(output_file)
		command = "\n\nsim:\n\t./RUNgcc ../../simplesim-3.0/sim-outorder ../../spec2000binaries/gcc00.peak.ev6  -max:inst 50000000 -fastfwd 20000000 -cache:dl2 ul2:"+chn+":"+chb+":4:l -wbuffer "+wbuf+" -ndbi "+nd+"     -dbipolicy "+dpol+" -dramcol "+dcol+" -redir:sim "+output_file+" -bpred 2lev -bpred:2lev 1 256 4 0 -bpred:ras 8 -bpred:btb 64 2"+"\n\ncompile:\n\t$(MAKE) -C ../../simplesim-3.0 clean\n\t$(MAKE) -C ../../simplesim-3.0 config-alpha\n\t$(MAKE) -C ../../simplesim-3.0\n\nrun: compile sim"
		if not os.path.isfile(output_file):
			m=open("Makefile",'w')
			m.write(command)
			m.close()
			os.system("make run")
print len(outs2)









"""

while 1:
	var= raw_input("this is case 2 #####cache_nsets vs ndbi ##########\n enter param:")
	if var == "next":
		break
	if not os.path.isfile("case2_"+var+"_ndbi_cache_nsets_"+".csv"):
		writer1 = csv.writer(open("case2_"+var+"_ndbi_cache_nsets_"+".csv", 'wb'))
		writer1.writerow([var,"ndbi","cache_nsets"])
		for o in outs2:
			f=open(o,'r')
			param={}
			for j in range(1,141):
	        		next(f)
			#f.read(23)
			for line in f:
		        	#f.read()
			        if line.split() :
		        	        param.update({line.split()[0]:line.split()[1]})
			f.close()
	#		print param
		
			for key,value in param.items():
#				print key
				if key == var :
#					print key
					n=o.find("_")#wbuf
					l=o.find("_",7)#ndbi
					m=o.find("_",l+1)#dpol
					p=o.find("_",m+1)#dcol
					q=o.find("_",p+1)#chn
					r=o.find("_",q+1)#chb
					s=o.find("_",r+1)#benchmark
					writer1.writerow([value,o[l+1:m],o[q+1:r]])




"""

##case3 vary cache_bsize and dbi

dpol="l"
dcol="2048"
chn="1024"
wbuf="8"
outs3=[]
for chb in cache_bsize:
	for nd in ndbi:
		output_file=o_file+"_"+wbuf+"_"+nd+"_"+dpol+"_"+dcol+"_"+chn+"_"+chb+"_"+benchmark+"_"
		if output_file not in outs3:
			outs3.append(output_file)
		if output_file not in outs:
			outs.append(output_file)
		command = "\n\nsim:\n\t./RUNgcc ../../simplesim-3.0/sim-outorder ../../spec2000binaries/gcc00.peak.ev6  -max:inst 50000000 -fastfwd 20000000 -cache:dl2 ul2:"+chn+":"+chb+":4:l -wbuffer "+wbuf+" -ndbi "+nd+"     -dbipolicy "+dpol+" -dramcol "+dcol+" -redir:sim "+output_file+" -bpred 2lev -bpred:2lev 1 256 4 0 -bpred:ras 8 -bpred:btb 64 2"+"\n\ncompile:\n\t$(MAKE) -C ../../simplesim-3.0 clean\n\t$(MAKE) -C ../../simplesim-3.0 config-alpha\n\t$(MAKE) -C ../../simplesim-3.0\n\nrun: compile sim"
		if not os.path.isfile(output_file):
			m=open("Makefile",'w')
			m.write(command)
			m.close()
			os.system("make run")
print len(outs3)



"""
while 1:
	var= raw_input("this is case 3 #####cache_bsize vs ndbi ##########\n enter param:")
	if var == "next":
		break
	if not os.path.isfile("case3_"+var+"_ndbi_cache_bsize_"+".csv"):
		writer1 = csv.writer(open("case3_"+var+"_ndbi_cache_bsize_"+".csv", 'wb'))
		writer1.writerow([var,"ndbi","cache_bsize"])
		for o in outs3:
			f=open(o,'r')
			param={}
			for j in range(1,141):
	        		next(f)
			#f.read(23)
			for line in f:
		        	#f.read()
			        if line.split() :
		        	        param.update({line.split()[0]:line.split()[1]})
			f.close()
	#		print param
		
			for key,value in param.items():
#				print key
				if key == var :
#					print key
					n=o.find("_")#wbuf
					l=o.find("_",7)#ndbi
					m=o.find("_",l+1)#dpol
					p=o.find("_",m+1)#dcol
					q=o.find("_",p+1)#chn
					r=o.find("_",q+1)#chb
					s=o.find("_",r+1)#benchmark
					writer1.writerow([value,o[l+1:m],o[r+1:s]])




"""
##case4 vary dramcols and dbi

dpol="l"
chn="1024"
chb="64"
wbuf="8"
outs4=[]
for dcol in dramcols:
	for nd in ndbi:
		output_file=o_file+"_"+wbuf+"_"+nd+"_"+dpol+"_"+dcol+"_"+chn+"_"+chb+"_"+benchmark+"_"
		if output_file not in outs4:
			outs4.append(output_file)
		if output_file not in outs:
			outs.append(output_file)
		command = "\n\nsim:\n\t./RUNgcc ../../simplesim-3.0/sim-outorder ../../spec2000binaries/gcc00.peak.ev6  -max:inst 50000000 -fastfwd 20000000 -cache:dl2 ul2:"+chn+":"+chb+":4:l -wbuffer "+wbuf+" -ndbi "+nd+"     -dbipolicy "+dpol+" -dramcol "+dcol+" -redir:sim "+output_file+" -bpred 2lev -bpred:2lev 1 256 4 0 -bpred:ras 8 -bpred:btb 64 2"+"\n\ncompile:\n\t$(MAKE) -C ../../simplesim-3.0 clean\n\t$(MAKE) -C ../../simplesim-3.0 config-alpha\n\t$(MAKE) -C ../../simplesim-3.0\n\nrun: compile sim"
		if not os.path.isfile(output_file):
			m=open("Makefile",'w')
			m.write(command)
			m.close()
			os.system("make run")
#print len(outs4)




"""
while 1:
	var= raw_input("this is case 4 #####dramcols vs ndbi ##########\n enter param:")
	if var == "next":
		break
	if not os.path.isfile("case4_"+var+"_ndbi_dramcols_"+".csv"):
		writer1 = csv.writer(open("case4_"+var+"_ndbi_dramcols_"+".csv", 'wb'))
		writer1.writerow([var,"ndbi","dramcols"])
		for o in outs2:
			f=open(o,'r')
			param={}
			for j in range(1,141):
	        		next(f)
			#f.read(23)
			for line in f:
		        	#f.read()
			        if line.split() :
		        	        param.update({line.split()[0]:line.split()[1]})
			f.close()
	#		print param
		
			for key,value in param.items():
#				print key
				if key == var :
#					print key
					n=o.find("_")#wbuf
					l=o.find("_",7)#ndbi
					m=o.find("_",l+1)#dpol
					p=o.find("_",m+1)#dcol
					q=o.find("_",p+1)#chn
					r=o.find("_",q+1)#chb
					s=o.find("_",r+1)#benchmark
					writer1.writerow([value,o[l+1:m],o[p+1:q]])


"""

##case5 vary dbipolicy and dbi

dcol="2048"
chn="1024"
chb="64"
wbuf="8"
outs5=[]
for dpol in dbipolicy:
	for nd in ndbi:
		output_file=o_file+"_"+wbuf+"_"+nd+"_"+dpol+"_"+dcol+"_"+chn+"_"+chb+"_"+benchmark+"_"
		if output_file not in outs5:
			outs5.append(output_file)
		if output_file not in outs:
			outs.append(output_file)
		command = "\n\nsim:\n\t./RUNgcc ../../simplesim-3.0/sim-outorder ../../spec2000binaries/gcc00.peak.ev6  -max:inst 50000000 -fastfwd 20000000 -cache:dl2 ul2:"+chn+":"+chb+":4:l -wbuffer "+wbuf+" -ndbi "+nd+"     -dbipolicy "+dpol+" -dramcol "+dcol+" -redir:sim "+output_file+" -bpred 2lev -bpred:2lev 1 256 4 0 -bpred:ras 8 -bpred:btb 64 2"+"\n\ncompile:\n\t$(MAKE) -C ../../simplesim-3.0 clean\n\t$(MAKE) -C ../../simplesim-3.0 config-alpha\n\t$(MAKE) -C ../../simplesim-3.0\n\nrun: compile sim"
		if not os.path.isfile(output_file):
			m=open("Makefile",'w')
			m.write(command)
			m.close()
			os.system("make run")
#print len(outs5)


"""
while 1:
	var= raw_input("this is case 5 #####dbipolicy vs ndbi ##########\n enter param:")
	if var == "next":
		break
	if not os.path.isfile("case2_"+var+"_ndbi_dbipolicy_"+".csv"):
		writer1 = csv.writer(open("case2_"+var+"_ndbi_dbipolicy_"+".csv", 'wb'))
		writer1.writerow([var,"ndbi","dbipolicy"])
		for o in outs2:
			f=open(o,'r')
			param={}
			for j in range(1,141):
	        		next(f)
			#f.read(23)
			for line in f:
		        	#f.read()
			        if line.split() :
		        	        param.update({line.split()[0]:line.split()[1]})
			f.close()
	#		print param
		
			for key,value in param.items():
#				print key
				if key == var :
#					print key
					n=o.find("_")#wbuf
					l=o.find("_",7)#ndbi
					m=o.find("_",l+1)#dpol
					p=o.find("_",m+1)#dcol
					q=o.find("_",p+1)#chn
					r=o.find("_",q+1)#chb
					s=o.find("_",r+1)#benchmark
					writer1.writerow([value,o[l+1:m],o[m+1:p]])

"""

############################done running the codes####################


#############export relevant data to csv################

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
	f.close()
#	print param
	if not os.path.isfile(o+".csv"):
		writer = csv.writer(open(o+".csv", 'wb'))
		for key, value in param.items():
			if value.replace('.','',1).isdigit():
				writer.writerow([key, value])

"""
#################irrelevant data here ############
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

#var= raw_input("enter param:")
#for key,value in param.items



