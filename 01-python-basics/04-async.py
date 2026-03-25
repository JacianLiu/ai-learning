'''
模拟同时查询三个学生的成绩（每次查询需要 1 秒），要求：

写一个 async def fetch_score(name) 函数，用 asyncio.sleep(1) 模拟耗时，返回 f"{name}: 90"
用 asyncio.gather() 并发查询 Alice、Bob、Charlie 三个人
打印总耗时——并发应该接近 1 秒，而不是 3 秒
'''

import asyncio
import time

students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 58},
    {"name": "Charlie", "score": 75},
    {"name": "Diana", "score": 88},
    {"name": "Eve", "score": 45},
]

students_score = {s["name"]: s["score"] for s in students}

async def fetch_score(name: str) -> str:
    await asyncio.sleep(1)
    return f"{name}: {students_score[name]}"


async def main():
    names = ["Alice", "Bob", "Charlie"]
    tasks = [fetch_score(n) for n in names]
    result  = await asyncio.gather(*tasks)
    print(result)

time1 = time.time()
asyncio.run(main())
time2 = time.time()
print(f"总耗时 {time2 - time1:.2f}秒")