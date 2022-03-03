def func(s: str, num: int):
    # 计算每个分组的字符数
    group = num-2+num
    # 如果分组数为零就改到1
    if group == 0:
        group = 1
    # 用整除计算有多少分组
    group_num = len(s)//group
    # 用列表来装分组
    all_list = []
    for i in range(0, group_num):
        all_list.append(s[i*group:(i+1)*group])
    # 将不足一个分组的字符分为最后一组
    fin_group = s[(group_num*group):]
    # 用占位符补齐分组，便于后续处理
    fin_group = fin_group + (group-len(fin_group)) * "-"
    # 加入分组列表
    all_list.append(fin_group)
    # 将分组转化为字符串
    new_str = ""
    # 分组遍历
    for i in range(0, num):
        # 如果为分组最想或最下的逻辑
        if i == 0 or i == num-1:
            for ii in all_list:
                new_str = new_str + ii[i]
        # 为中间则添加两个的逻辑
        else:
            for ii in all_list:
                new_str = new_str + ii[i] + ii[group-i]
    # 定义最后的结果
    fin_str = ""
    # 清除占位符
    for i in new_str:
        if i != "-":
            fin_str = fin_str + i
    return fin_str


if __name__ == '__main__':
    print(func("A", 1))
