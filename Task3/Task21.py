# Напишите программу для печати всех уникальных значений в словаре. 

# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}



my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
           {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]
final_set = set()
for i in my_list:
    for j in i:
        final_set.add(i[j].strip())
print(final_set)

