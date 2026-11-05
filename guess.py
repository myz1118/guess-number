import random

answer = random.randint(1, 100)
attempts = 0

print("我想了一个 1～100 的整数，来猜猜吧！输入 q 退出。")

while True:
    text = input("你的答案：").strip()

    if text.lower() == "q":
        print(f"答案是 {answer}，下次再玩！")
        break

    try:
        guess = int(text)
    except ValueError:
        print("请输入整数。")
        continue

    if not 1 <= guess <= 100:
        print("数字要在 1～100 之间哦。")
        continue

    attempts += 1

    if guess < answer:
        print("小了，再大一点！")
    elif guess > answer:
        print("大了，再小一点！")
    else:
        print(f"猜对了！你一共猜了 {attempts} 次。")
        break