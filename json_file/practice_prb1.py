import json
filename = "/Users/logesh/python_workspace/json_file/data.txt" # the path of the txt file 


# dict1 = {} #resultant dictionary
# fields =['name', 'age', 'gender'] #fields in the sample file
# with open(filename) as fh: 
#     l = 1 #count variable for employee id creation
#     for line in fh:
#         description = list( line.strip().split(None, 3)) #reading line by line from the text file
#         print(description) #to check output 
#         sno ='ID-'+str(l) #for automatic creation of id for each student
#         i = 0 #loop variable
#         dict2 = {} # intermediate dictionary
#         while i<len(fields):
#             dict2[fields[i]]= description[i] #creating dictionary for each employee
#             i = i + 1
#         dict1[sno]= dict2 #appending the record of each employee to the main dictionary
#         l = l + 1
 
out_file = open("data.json", "w")  #creating json file
# json.dump(dict1, out_file, indent = 3)


data = [{7058: 'sravan'}, {7059: 'jyothika'}, 
         {7072: 'harsha'}, {7075: 'deepika'}]

json.dump(data, out_file, indent = 2)
out_file.close()