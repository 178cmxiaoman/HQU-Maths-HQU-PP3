# question 1
sum = 0
for i in range(2, 101, 1):
    if i % 2 == 0:
        sum += i
    else:
        sum -= i

print("问题1的答案是:")
print(sum)

# question 2
msg = input('请输入字符串:')
n = len(msg)
print('字符串的长度为：', n)  # 字符串长度

print('将原字符串转换为小写字符为：', end='')
for num in msg:
    if 65 <= ord(num) <= 90:  # 大写字母
        upper_num = ord(num) + 32
        print(chr(upper_num), end='')
    else:
        print(num, end='')

print()
print('字符串中字符出现情况：')

dict = dict()
for i in msg:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for key, value in dict.items():
    print(key, value)

with open('week3/ex_data1.txt', 'r') as file:
    lines = file.readlines()
data = []
# 循环遍历每行数据
for line in lines:
    parts = line.strip().split()
    if len(parts) == 2:
        name, score = parts[0], int(parts[1])
        data.append((name, score))
n = len(data)


def fun1(score):
    if score < 60:
        return "不及格"
    elif score < 70:
        return "及格"
    elif score < 80:
        return "中等"
    elif score < 90:
        return "良好"
    else:
        return "优秀"


with open('week3/out.txt', 'w') as new_file:
    for i in range(0, n):
        scale = fun1(data[i][1])
        new_file.write(str(data[i][0]) + '\t' + str(data[i][1]) + '\t' + scale + '\n')

    new_file.close()

for i in range(0, n - 1):  # 冒泡排序
    for j in range(0, n - i - 1):
        if (data[j][1] <= data[j + 1][1]):
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp

for i in range(0, 4):
    print('成绩排名第', i + 1, '的同学是：', data[i][0], ',他考了', data[i][1], '分')
