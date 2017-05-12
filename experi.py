#coding:utf-8

import re
import sys

if __name__=="__main__":
#	print("hello world!")

#	Open the files and write the start of "import.xml".
	reqnum = int(sys.argv[1])
	a=open("data\sub.txt","r")
	b=open("data\\nrxml\import"+str(reqnum)+".xml","w")
	#for test
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
	
#	Transform the substratenetwork's link-information from "sub.txt" to "import.xml"
	
	b.writelines("<SubstrateLinks>\n")

	j = 0
	while(j<numSL):
		r=a.readline()
		rc = re.split(" ",r)
		b.writelines("<SubstrateLink source=\""+str(int(rc[0])+1)+"\" destination=\""+str(int(rc[1])+1)+"\" id=\""+str(i+1)+"\">\n")
		b.writelines("<Resource type=\"BandwidthResource\">\n")

		rc2 = re.split("\n",rc[2])

		b.writelines("<Parameter name=\"Bandwidth\" type=\"Double\" value=\""+str(rc2[0])+"\"/>\n")
		b.writelines("</Resource>\n</SubstrateLink>\n")
		i=i+1;
		b.writelines("<SubstrateLink source=\""+str(int(rc[1])+1)+"\" destination=\""+str(int(rc[0])+1)+"\" id=\""+str(i+1)+"\">\n")
		b.writelines("<Resource type=\"BandwidthResource\">\n")
		b.writelines("<Parameter name=\"Bandwidth\" type=\"Double\" value=\""+str(rc2[0])+"\"/>\n")
		b.writelines("</Resource>\n</SubstrateLink>\n")
		i=i+1;


		j=j+1;


#	for test
	"""
	r=a.readline()
	rc=re.split(" ",r)
	for i in rc:
		print(i)
	print(len(rc))
	"""
	
	b.writelines("</SubstrateLinks>\n")
	b.writelines("</SubstrateNetwork>\n")

	a.close()

#	Transform the virtualnetwork's information from "req?.txt" to "import.xml"
	
	b.writelines("<VirtualNetworks>\n")
	k=0
	while(k<reqnum):
		b.writelines("<VirtualNetwork layer=\""+str(k+1)+"\">\n")
		a=open("data/nr2500/req"+str(k)+".txt","r")
		
		#for test
		#print(a.readline())
		
		r1=a.readline()
		r1c=re.split(" ",r1)
		
		#for test
		#print(str(len(r1c))+" "+r1c[0])
		#print(r1c[0]+" "+r1c[1])

		numVN=int(r1c[0])
		numVL=int(r1c[1])


		i0=i
		
		
		b.writelines("<VirtualNodes>\n")
		j=0
		while(j<numVN):
			#for test
			#print("node:"+str(j+1)+" id:"+str(i+1))
			r = a.readline()
			rc = re.split("\n",r)
			b.writelines("<VirtualNode coordinateX=\"0\" coordinateY=\"0\" id=\""+str(i+1)+"\">\n")
			b.writelines("<Demand type=\"CpuDemand\">\n")
			b.writelines("<Parameter name=\"DemandedCycles\" type=\"Double\" value=\""+str(float(rc[0]))+"\"/>\n")

			b.writelines("</Demand>\n")
			b.writelines("</VirtualNode>\n")
			i=i+1
			j=j+1
		b.writelines("</VirtualNodes>\n")
		
		b.writelines("<VirtualLinks>\n")
		j=0
		while(j<numVL):
			#for test
			#print("link:"+str(j+1)+" id:"+str(i+1))
			r = a.readline()
			rc = re.split(" ",r)
			rc2 = re.split("\n",rc[2])
			b.writelines("<VirtualLink source=\""+str(int(rc[0])+i0+1)+"\" destination=\""+str(int(rc[1])+i0+1)+"\" id=\""+str(i+1)+"\">\n")
			
			b.writelines("<Demand type=\"BandwidthDemand\">\n")

			b.writelines("<Parameter name=\"DemandedBandwidth\" type=\"Double\" value=\""+str(float(rc2[0]))+"\"/>\n")

			b.writelines("</Demand>\n")


			b.writelines("</VirtualLink>\n")
			i=i+1
			b.writelines("<VirtualLink source=\""+str(int(rc[1])+i0+1)+"\" destination=\""+str(int(rc[0])+i0+1)+"\" id=\""+str(i+1)+"\">\n")
			
			b.writelines("<Demand type=\"BandwidthDemand\">\n")

			b.writelines("<Parameter name=\"DemandedBandwidth\" type=\"Double\" value=\""+str(float(rc2[0]))+"\"/>\n")

			b.writelines("</Demand>\n")


			b.writelines("</VirtualLink>\n")
			i=i+1
			j=j+1


		b.writelines("</VirtualLinks>\n")

		a.close()
		b.writelines("</VirtualNetwork>\n")
		k=k+1


	b.writelines("</VirtualNetworks>\n")
	b.writelines("</Scenario>\n")
	b.close()
