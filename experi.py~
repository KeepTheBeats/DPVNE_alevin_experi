#coding:utf-8

import re

if __name__=="__main__":
#	print("hello world!")

#	Open the files and write the start of "import.xml".
	a=open("data\sub.txt","r")
	b=open("data\import.xml","w")
	#print(a.name)

	b.writelines("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n")
	b.writelines("<Scenario\n")
	b.writelines("xsi:schemaLocation=\"http://sourceforge.net/projects/alevin/ ./Alevin.xsd\"\n")
	b.writelines("xmlns=\"http://sourceforge.net/projects/alevin/\"\n")
	b.writelines("xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\n")
	b.writelines(">\n")
	b.writelines("<SubstrateNetwork>\n")

#	Get the substratenetwork's node-number and link-number.
	r1 = a.readline()
	r1c = re.split(" ",r1)
	

	#for i in r1c:
	#print(len(r1c))	

	numSN=int(r1c[0])
	numSL=int(r1c[1])

	#print(numSN+1,numSL)

#	Transform the substratenetwork's node-information from "sub.txt" to "import.xml"
	
	b.writelines("<SubstrateNodes>\n")

	i = 0
	while(i<numSN):
		r=a.readline()
		rc = re.split("\n",r)
		b.writelines("<SubstrateNode coordinateX=\"0\" coordinateY=\"0\" id=\""+str(i+1)+"\">\n")
		b.writelines("<Resource type=\"CpuResource\">\n")
		b.writelines("<Parameter name=\"Cycles\" type=\"Double\" value=\""+rc[0]+"\"/>\n")
		b.writelines("</Resource>\n</SubstrateNode>\n")
		i=i+1

	b.writelines("</SubstrateNodes>\n")



	a.close()
	b.close()
