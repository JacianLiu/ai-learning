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

print("------------------")

# 用列表推导式取出所有偶数。
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ns = [n for n in numbers if n % 2 == 0]

# 用列表推导式把每个单词转成大写。
words = ["hello", "world", "python", "list"]
b_words = [w.upper() for w in words]


# 取出所有正数，并对它们求平方，存成一个列表。
numbers = [-3, -2, -1, 0, 1, 2, 3]
b_numbers = [pow(n, 2) for n in numbers if n > 0]

# 用字典推导式筛选出价格大于 2 的商品，生成一个新字典。
prices = {"apple": 3, "banana": 1, "cherry": 5, "date": 2}
b_prices = {k: v for k, v in prices.items() if v > 2}
print(b_prices)

# 用列表推导式把二维列表"拍平"成 [1, 2, 3, 4, 5, 6, 7, 8, 9]。
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b_matrix = [n for row in matrix for n in row]
print(b_matrix)

# 这是一个三维列表，用列表推导式把它拍平成：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]],
]
b_cube = [c3 for c1 in cube for c2 in c1 for c3 in c2]
print(b_cube)

# 生成一个字典，key 是学生名字，value 是 "pass" 或 "fail"（score >= 60 为 pass）。
# 期望结果：{"Alice": "pass", "Bob": "fail", "Charlie": "pass"}
students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 58},
    {"name": "Charlie", "score": 75},
]

b_students = {s["name"]: "pass" if s["score"] >= 60 else "fail" for s in students}
print(b_students)