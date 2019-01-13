import tkintertest
data = 0x3FD5013E
data_list=list()
## 0011 1111  1101 0101  0000 0001  0011 1110
def list_len(list_temp):
	for i,j in enumerate(list_temp,1):
		pass
	return i

def get_data(startbit,numbits):
	global data
	temp_var= data
	# temp_var=temp_var>>startbit
	mask=(2**numbits)-1
	temp_var=(temp_var>>startbit)&mask
	# temp_var=(temp_var<<(32-(startbit+numbits)))
	# temp_var=(temp_var>>(32-(startbit+numbits)))
	# temp_var=(temp_var>>startbit)
	# if(temp_var<0):
	# 	temp_var=-temp_var
	return(temp_var)

lis=[
['name', 'Label'],            ['type', 'Label'],    ['bitStart', '0'],  ['numBits', '8'], ['value', '0o174'], 
['name', 'SDI'],              ['type', 'SDI'],      ['bitStart', '8'],  ['numBits', '2'], 
['name', 'Test/Tune Inhibit'],['type', 'UInt'],     ['bitStart', '10'], ['numBits', '1'], 
['name', 'Reserved'],         ['type', 'Reserved'], ['bitStart', '11'], ['numBits', '1'], 
['name', 'PADS'],             ['type', 'Pad'],      ['bitStart', '12'], ['numBits', '4'],
['name', 'DDM'],              ['type', 'BNR'],      ['bitStart', '16'], ['numBits', '13'], ['precision', '0.8 / (2^12)'], 
['name', 'SSM'],              ['type', 'SSM_BNR'],  ['type', 'Parity']]
name=["makrand"]

print(lis[0][0])
##########################################################
#code for list extraction logic
#########################################################
def extract():
	global lis
	mk=0
	small_list=[]
	for i in lis:
		# mk+=1
		small_list.append(i)
		# print("mk=",lis[mk][1])
		#(lis[mk][0]=='name') or
		if((lis[mk][1]=='Parity') or (lis[mk+1][0]=='name')):
			lis=lis[mk+1:]
			break
		mk+=1

	return(small_list)
#########################################################
while(lis):
	precision=0
	small_list=extract()
	if not lis:
		small_list=small_list[:-1]
	print("small_list::",small_list)
	for node in small_list:
		if (node[0]=="name"):
			f_name=node[1]
			data_list.append(f_name)
		if (node[0]=="bitStart"):
			startbit=int(node[1])
			data_list.append(startbit)
		if (node[0]=="numBits"):
			numbits=int(node[1])
			data_list.append(numbits)
		if(node[0]=="precision"):
			precision=eval(node[1])
			
	if(list_len(small_list)>=3):	
		# print("startbit",startbit)
		# print("numbits:",numbits)
		data_bits=get_data(startbit,numbits)
		print("data_bits:",bin(data_bits))
		data_list.append(bin(data_bits))
		if(list_len(small_list) >4):
			print("***************")
			if(precision!=0):
				print("precision:",precision)
				data_list.append(precision)
		# print("data_bits:",bin(data_bits))
		# data_list.append(numbits)
		print("data:",data_bits)
print("#######################################################################")
print("#######################################################################")
print("data_list:",data_list)
tkintertest.show(data_list)
		# tkintertest.show(sendlist)
		# print(bin(data_bits))
	
# print(a_0)
# while True:
# 	if(lis[0][0] == 'name')