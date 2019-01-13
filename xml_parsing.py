import xml.etree.ElementTree as ET
import test
xmlfile="a.xml"
tree=ET.parse(xmlfile)
data = 0x3FD5013E  
label_name_list=[]
label_definition_list=[]
temp_list=[]
label_id=test.find_label_id(data)
string_label=str(label_id)
# print("string_label: ", string_label)
if(len(string_label)==2):
    string_label='0'+ string_label
root= tree.getroot()
# print("Root:", root)
Number_of_definitions = 0 # this flag works with(flag_a) is used to identify how many definations are available for Label
for item in root:
    # print("######################################################")
    flag_1=0
    # print("item :",item)
    if item.tag == "labelDefinition":
        flag_a=0
        for tags in item:
            a= tags.attrib
            if (flag_1==0):     
                xml_label=str(a.get('value'))                
                # print("xml_label:", xml_label)
            if(xml_label.find(string_label) != -1):                        
                # print("######################################################")
                # temp_list=[]
                for key in a:
                    temp_list.append([key,a.get(key)])
                    if(a.get(key)=='Parity'):
                        label_definition_list.append(temp_list)
                        temp_list=[]
                    if (flag_a==0):
                        flag_a=1
                        l_name=item.get('name')
                        l_id =item.get('id')
                        label_name_list.append(l_name +" ("+l_id+")") 
                        Number_of_definitions+=1
                        print("----------------------")
                        print("Number_of_definitions",Number_of_definitions)
                        print("----------------------")
                        
                        # test.printlist(temp_list)
                        
                        # test.printlist(temp_list)
                    # print(key ,"==", a.get(key))
                    # test.printlist(temp_list)
            # print("*******")
            flag_1+=1
test.printlist(label_name_list)
test.printlist(label_definition_list)
print("Number_of_definitions",Number_of_definitions)
                # print("----------------------")
        # print("######################################################")
