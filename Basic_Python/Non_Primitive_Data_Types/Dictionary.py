# Dictionary {key:value}
# it store the value
# Here Key's can't be dublicate , but value can be dublicate


mark={"Math":99,"Physics":98,"Chemistry":97}

print(mark,type(mark))

# Access indivisual value , using key's
print(mark["Physics"])

# Modufy existing values
mark["Physics"]=85
print(mark["Physics"])

# Add extra key's
mark["English"]=92
print(mark["English"])

# print using loop, but here i only take key's
for i in mark:
    print(i,mark[i])
