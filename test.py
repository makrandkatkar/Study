def testbit(int_type, offset):
    return((int_type >> offset) & 1)


def complimentbit(int_type, offset):
    mask = 1 << offset
    return(int_type ^ mask)


def reverse(data):
    mk = True
    left = 31
    right = 0
    while(mk):
        if(left <= right):
            mk = False
        if(testbit(data, left) != testbit(data, right)):
            # print(left,testbit(data,left), right, testbit(data,right))
            data = complimentbit(data, left)
            data = complimentbit(data, right)
        # print(bin(data))
        left -= 1
        right += 1
    return data


def find_label_id(data):
    # print(data)
    # print("forward data:",bin(data))
    data = reverse(data)
    # print("reverse data:",bin(data))
    label_id = (data >> 30) & 3
    # print(bin(label_id))
    # print(label_id)
    label_id *= 10
    # print(label_id)
    label_id = label_id + ((data >> 27) & 7)
    # print(label_id)
    label_id *= 10
    label_id = label_id + ((data >> 24) & 7)
    return(label_id)


def find_label_ssm(data):
    return((data >> 29) & 3)


def printlist(temp_list):
    print("list=")
    for i in temp_list:

        print(i)
        print("++++++++++++++++++++++++++++++++")

list_name=['VOR Ground Station ID #2']

data= 0x20000125
temp=[]
mk=[]

list_data=[['name', 'Label'],    ['type', 'Label'],   ['bitStart', '0'],  ['numBits', '8'], ['value', '0o244'],
           ['name', 'SDI'],      ['type', 'SDI'],     ['bitStart', '8'],  ['numBits', '2'],
           ['name', '3rd Char'], ['type', 'ASCII'],   ['bitStart', '10'], ['numBits', '7'], 
           ['name', 'PAD#1'],    ['type', 'Pad'],     ['bitStart', '17'], ['numBits', '1'],
           ['name', '4th Char'], ['type', 'ASCII'],   ['bitStart', '18'], ['numBits', '7'],
           ['name', 'PAD#2'],    ['type', 'Pad'],     ['bitStart', '25'], ['numBits', '1'],
           ['name', 'SPARE'],    ['type', 'Spare'],   ['bitStart', '26'], ['numBits', '3'], 
           ['name', 'SSM'],      ['type', 'SSM_Packed'],
           ['type', 'Parity']]

for index,i in enumerate(list_data):
    # print("index=", index)
    if ((i[0])=='name'):
        temp.append(mk)
        temp.append("####")
    mk.append(i)

print(temp)
