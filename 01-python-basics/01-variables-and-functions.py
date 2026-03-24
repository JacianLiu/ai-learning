name: str = 'Hello World'
age: int = 13

print(f"{name}, age is {age}")

if age > 18:
    print("成年")
elif age < 18 and age > 0:
    print("未成年")
else:
    print("啊？")


# arr: list | None - 是 list 也可以是 None 类型，默认值是 None
# split 是 str 类型，默认值是 ","
def traverse_array(arr: list | None = None, split: str = ",") -> None:
    if arr == None:
        return
    for item in arr:
        print(f"{item}{split}", end="")
    print("")
    for i, item in enumerate(arr):
        if i == len(arr) - 1:
            print(f"{item}")
        else:
            print(f"{item}{split}", end="")
    print(split.join(arr))

fruits = ["Apple", "Banana", "Cherry"]

h = traverse_array(fruits)
print(h)


def bmi(weight: float, height: float) -> float:
    result = weight / pow(height, 2)

    if result < 18.5:
        print("偏瘦")
    elif 18.5 <= result < 24:
        print("正常")
    else:
        print("偏重")

    return result

print(bmi(63, 1.82))