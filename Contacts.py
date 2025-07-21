contacts = {
    "number": 4,
    "students":
        [
            {"name":"Lauren Perry","email":"lperrymail@gmail.com"},
            {"name":"Danie Snyman","email":"dsnyman@gmail.com"},
            {"name":"Taylor Wolchuk","email":"taapaige@gmail.com"},
            {"name":"Geoff Coetsee","email":"gcoetsee@gmail.com"}
        ]
}

print("Student email: ")
for student in contacts["students"]:
    print(student["email"])
