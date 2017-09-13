#! /usr/bin python
import commands
import os
import datetime
import sys
import threading 
import subprocess
import zipfile

downloadThreads = []

thread_num = 16





def dateDiffInHours(t1, t2):
    td = t2 - t1
    return td.days * 24 * 60 + td.seconds/60 + 1 

ntime = '2016-05-20-15-30-00'
#ntime = '2017-09-06-08-30-23'
ds = datetime.datetime.strptime(ntime, '%Y-%m-%d-%H-%M-%S')


#ntimes = '2016-05-21-16-31-26'
#dss = datetime.datetime.strptime(ntimes, '%Y-%m-%d-%H-%M-%S')

#dt = dateDiffInHours(ds,dss)
#print dt 

#id = sys.argv[1]

ptids = []
f = open('./ptid_less.txt','r')
for lines in f.readlines():
        #ptid = f.readline()
	lines = lines.replace("\n","")
	#print lines
	ptids.append(lines)
	f.close()

#print ptids[1:4]

#ptids = ['11361']

count = len(ptids)

def getvalue(ptid,ds,ntime):
	#global ds
	#global ntime
	print ptid
#	com = ["/users/ems/sophic/deployment/bin/rthis/query_simple"]
#	com.append(str(ptid))
#       com.append("1")
#	com.append(ntime)
#	com.append(str(600)) 
	seq = 1
	while ds < datetime.datetime.now():
		#com = ["/users/ems/sophic/deployment/bin/rthis/query_simple"]
        	#com.append(str(ptid))
        	#com.append("1")
        	#com.append(ntime)     
        	#com.append(str(600))
		#print com 
		main = "./query_simple " + ptid + "  1 " +  ntime + " 4320 " + str(seq)
		print "=====" + main
		f = os.popen(main)
		#subprocess.check_call(com)
		#data = f.readlines()
		f.close()
		#print data
        	ds = ds + datetime.timedelta(hours=72)
        	ntime = ds.strftime("%Y-%m-%d-%H-%M-%S")
		seq = seq + 1

        dsz = ds-datetime.timedelta(hours=72)
	ntime = dsz.strftime("%Y-%m-%d-%H-%M-%S")
	dt = dateDiffInHours(dsz,datetime.datetime.now())
	main = "./query_simple " + ptid + "  1 " +  ntime + " "  + str(dt)
	f = os.popen(main)
        #data = f.readlines()
        f.close()
	csv_name = str(ptid) + '.csv'
	zip_name = csv_name + '.zip'
	newZip = zipfile.ZipFile(zip_name, 'w')
	newZip.write(csv_name, compress_type=zipfile.ZIP_DEFLATED)
	newZip.close()
	try:
		os.remove(csv_name)
	except OSError:
		pass


#getvalue(id,ds,ntime)


for i in range(0,count,thread_num):
	for j in range(i,min(count,i+thread_num)):
		downloadThread = threading.Thread(target=getvalue,args=[ptids[j],ds,ntime])
		downloadThreads.append(downloadThread)
		downloadThread.start()
	for downloadThread in downloadThreads:
		downloadThread.join()
	print 'thread end'
	del downloadThreads[:]
		

#for index in range(len(ptids)):
#	print ptids[index]
#	getvalue(ptids[index],ds,ntime)

