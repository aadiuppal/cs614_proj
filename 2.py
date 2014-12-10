import os.path
import csv
import os
import time
import subprocess

dpol="l"
dcol="2048"
chn="1024"
chb="64"
outs=[]
wbuf="8"
nd="32"
o_file="output"
benchmark="gcc"

#for wbuf in wbuffer:
#        for nd in ndbi:
output_file=o_file+"_"+wbuf+"_"+nd+"_"+dpol+"_"+dcol+"_"+chn+"_"+chb+"_"+benchmark+"_"
#                if output_file not in oust1:
#                        outs1.append(output_file)
if output_file not in outs:
	outs.append(output_file)
command = "\n\nsim:\n\t./RUNgcc ../../simplesim-3.0/sim-outorder ../../spec2000binaries/gcc00.peak.ev6  -max:inst 50000000 -fastfwd 20000000 -cache:dl2 ul2:"+chn+":"+chb+":4:l -wbuffer "+wbuf+" -ndbi "+nd+"     -dbipolicy "+dpol+" -dramcol "+dcol+" -redir:sim "+output_file+" -bpred 2lev -bpred:2lev 1 256 4 0 -bpred:ras 8 -bpred:btb 64 2"+"\n\ncompile:\n\t$(MAKE) -C ../../simplesim-3.0 clean\n\t$(MAKE) -C ../../simplesim-3.0 config-alpha\n\t$(MAKE) -C ../../simplesim-3.0\n\nrun: compile sim"
if not os.path.isfile(output_file):
	m=open("Makefile",'w')
	m.write(command)
	m.close()
#	subprocess.call(["make","run"])
	os.system("make run >log_"+output_file)
	time.sleep(5)
#print len(outs1)

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
        print param
        writer = csv.writer(open(o+".csv", 'wb'))
        for key, value in param.items():
                   writer.writerow([key, value])

