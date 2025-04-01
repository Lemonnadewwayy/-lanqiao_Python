# 100 万元转换为 1000000 元
money = 1000000
# 初始化份数
ans = 0

while money > 0:
    # 获取 7 进制下当前位的数字
    remainder = money % 7
    ans += remainder
    money //= 7

print(ans)
