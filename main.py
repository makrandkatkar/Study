import test
data = [0x3FD5013E,0xA2000138,0x20000145,0x20000125,0xA2000138,0x20000145,0x20000125,0x82000177,0x200001CD,0xBFA401DE,0x257D0149,0x200001CD,0xBFA401DE,0x257D0149,0xA000012D,0x220001D8,0xB4283177,0xD24D4D37,0xA000012D,0x220001D8,0xB4283177,0xD24D4D37,0x3FE0013E,0x3FE0013E,0x3F1D01DE,0x23630149,0x3F1D01DE,0x23630149]

for i in data:
    print("ID=",test.find_label_id(i),"ssm=",test.find_label_ssm(i))
    # print(test.find_label_ssm(i))
