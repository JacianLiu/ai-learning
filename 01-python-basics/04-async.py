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


'''

模拟翻译 API，每次耗时 1 秒
要求：

1. 写一个 `async def translate(word: str) -> str` 函数，用 `asyncio.sleep(1)` 模拟耗时，从 `translate_db` 查找翻译，找不到返回 `f"{word}: 未找到"`

2. 写一个 `async def batch_translate(words: list) -> None` 函数，接收单词列表，用 `asyncio.gather()` 并发翻译所有单词，打印每个翻译结果

3. 在 `main()` 里调用 `batch_translate()`，传入 `["hello", "world", "python", "java", "gather"]`

4. 打印总耗时——5 个单词并发，应该接近 1 秒而不是 5 秒

期望输出类似：
```
hello → 你好
world → 世界
python → 蟒蛇
java → 未找到
gather → 聚合
总耗时：1.00 秒
'''

translate_db = {
    "hello": "你好",
    "world": "世界",
    "python": "蟒蛇",
    "async": "异步",
    "gather": "聚合",
}

async def translate(word: str) -> str:
    await asyncio.sleep(1)
    res = translate_db.get(word)
    # 对比 None 使用is
    # is 对比地址值；== 对比值
    if res is None:
        return f"{word} 未找到"
    return res

async def batch_translate(words: list) -> None:
    tasks = [translate(w) for w in words]
    res = await asyncio.gather(*tasks)
    print(res)

async def main():
    names = ["Alice", "Bob", "Charlie"]
    tasks = [fetch_score(n) for n in names]
    result  = await asyncio.gather(*tasks)
    print(result)

    # 第二题
    await batch_translate(["hello", "python", "async", "gather", "java"])

time1 = time.time()
asyncio.run(main())
time2 = time.time()
print(f"总耗时 {time2 - time1:.2f}秒")