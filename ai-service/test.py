from orchestrator.master_graph import graph


result = graph.invoke({
    "task": "Create student profile and extract skills",

    "student_data": """
    Name: Akhil
    Branch: Computer Science Engineering
    Year: 2nd year

    Skills:
    C++
    Python
    SQL
    Data Structures

    Interests:
    Artificial Intelligence
    Machine Learning

    Career goal:
    Machine Learning Engineer
    """,

    "student_profile": "",
    "skills": ""
})


print("\n==============================")
print("STUDENT PROFILE")
print("==============================\n")

print(result["student_profile"])


print("\n==============================")
print("EXTRACTED SKILLS")
print("==============================\n")

print(result["skills"])