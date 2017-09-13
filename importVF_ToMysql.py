import os
import MySQLdb
import mysql.connector
FileList = []
FileNames = os.listdir('G:\\nhtext')

def fileOperation():
    for filename in FileNames:
        name = filename.split('.')[0][1:]
        #print name
        if(len(name)==5 and name!='05410' and name!='06786' and name!='09409 '):
            file = open(filename,'r')
            lines = file.readlines()
            file.close()
            file = open(filename,'w')
            for k, v in enumerate(lines):
                file.write('%s%s'%(name+',',v))
            file.close()
			
            LoadFile(name)


def LoadFile(name):
	try:
		print(name)
		db = MySQLdb.connect("192.168.100.10","root","220582","manager" )
		cursor = db.cursor()
		sql = "load data local infile 'z" + name + ".TXT' replace into table test character set gb2312  fields terminated by ','  optionally enclosed by '\"' lines terminated by  '\r\n';" 
		print( cursor.execute(sql))
		db.commit()
		db.close()
	except IOError :
		print ("error")
	

def importToMysql():    
    #load data local infile 'G:\\nhtext\\z00001.TXT' replace into table test character set gb2312  fields terminated by ','  optionally enclosed by '"' lines terminated by '\r\n' ;
    os.system("mysql -uroot -h 192.168.100.10 -p220582")
    os.system("use manager")
    #os.system("load data local infile 'G:\\nhtext\\z00001.TXT' replace into table test character set gb2312  fields terminated by ','  optionally enclosed by '"' lines terminated by '\r\n';")
    
    
if __name__ == '__main__':
    #print("OK")
    
    fileOperation()
    #LoadFile("00003")

