
# #                                                     # risivibg data from mongodb server ###

# import pymongo
# uri = "mongodb://127.0.0.1:27017"       # 127.0.0.1 is machine ip and 27017 is port
# client = pymongo.MongoClient(uri) 
# database = client['fullstack']
# collection = database['student']

# students = collection.find({})

# for student_var in students:
#     print(student_var)


import pymongo
uri = "mongodb://127.0.0.1:27017"       # random trying
client = pymongo.MongoClient(uri) 
database = client['fullstack']
collection = database['student']

students = [student_key ['name'] for student_key in collection.find({})]                 # list comprihention
print(students)

# student_list = []
# for student_var in students:
#     student_list.append(student_var)
