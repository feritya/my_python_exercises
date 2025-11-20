student={
    "name": "John",
    "surname": "doe",
    "school_name":"medeniyet universitiy",
    "school_number":19120205052,
    "age":22,
    "department":"computer engineering",
    "lessons":{
        "math":67,
        "physics":78,
        "programming":85,
        "data structures":90,
        "algorithms":88
    },
    "grade":3.50,
}

student["lessons"].update({"algorithms":100})

average=sum(student["lessons"].values())/len(student["lessons"])
student["grade"]=average/25
print("name",student["name"],student["surname"])
print("grade",student["grade"])
print("department",student["department"])
print("school number",student["school_number"])
print("Average of lessons:",average)