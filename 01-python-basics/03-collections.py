# 给你一个学生成绩列表：
# students = [
#     {"name": "Alice", "score": 92},
#     {"name": "Bob", "score": 58},
#     {"name": "Charlie", "score": 75},
#     {"name": "Diana", "score": 88},
#     {"name": "Eve", "score": 45},
# ]
# 用列表推导式完成三件事：
# 取出所有及格（score >= 60）的学生名字，存成一个列表
# 给每个学生的 score 加 5 分，生成新列表（不改原列表）
# 用 dict 推导式把列表转成 {"Alice": 92, "Bob": 58, ...} 的格式

students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 58},
    {"name": "Charlie", "score": 75},
    {"name": "Diana", "score": 88},
    {"name": "Eve", "score": 45},
]

pass_student_names = [s["name"] for s in students if s["score"] >= 60]
print(pass_student_names)

students_new = [{"name": s["name"], "score": s["score"] + 5} for s in students]
print(students_new)

student_dict = {s["name"]: s["score"] for s in students}
print(student_dict)