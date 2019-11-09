# 练习列表使用方法
# V0.0.1 Auto:WMM
# DATE：Nov 09 2019
# 显示欢迎信息界面


print('-' * 20, '欢迎使用员工信息系统', '-' * 20)
# 显示用户选项
emps = ['\t孙悟空\t18\t男\t花果山']

while True:
    print('请选择要做的操作：')
    print('\t1.显示员工信息表')
    print('\t2.添加员工信息')
    print('\t3.删除员工信息')
    print('\t4.退出系统')
    user_chose = input('请选择[1-4]:')

    # 根据用户的选择来做相关操作
    if user_chose == '1':
        # 查询员工
        # 打印表头
        print('\t序号\t姓名\t年龄\t性别\t住址\t')
        # 创建一个变量
        n = 1

        # 显示员工信息
        for emp in emps:
            print(f'\t{n}\t{emp}')
            n += 1

    elif user_chose == '2':
        # 添加员工
        # 获取添加员工的姓名、年龄、性别、住址信息
        emp_name = input("请输入员工姓名：")
        emp_age = input("请输入员年龄：")
        emp_gender = input("请输入员工性别：")
        emp_addr = input("请输入员工住址：")

        # 创建员工信息
        # 将四个信息拼接成一个字符串，然后插入列表中
        emp = f'\t{emp_name}\t{emp_age}\t{emp_gender}\t{emp_addr}'
        # 显示一个提示信息
        print('以下员工将被添加到系统中：')
        print('-' * 60)
        print('\t姓名\t年龄\t性别\t住址\t')
        print(emp)
        print('-' * 60)
        user_confirm = input('请您确认该操作[Y/N]:')

        # 判断
        if user_confirm == 'yes' or user_confirm == 'y' or user_confirm == 'Y':
            # 插入
            emps.append(emp)
            # 显示提示信息
            print('添加员工信息操作成功！')
        else:
            print('取消添加员工信息操作成功！')

    elif user_chose == '3':
        # 删除员工
        # 根据员工的序号删除
        del_num = int(input('请输入要删除的员工序号:'))

        # 判断序号是否有效
        if 0 < del_num <= len(emps):
            # 输入合法，根据序号删除
            del_i = del_num - 1
            # 显示一个信息
            print('以下员工将从系统中删除：')
            print('-' * 60)
            print('\t序号\t姓名\t年龄\t性别\t住址\t')
            print(f'\t{del_num}\t{emps[del_i]}')
            print('-' * 60)
            user_confirm = input('该操作不可返回，是否确认[Y/N]:')
            if user_confirm == 'yes' or user_confirm == 'y' or user_confirm == 'Y':
                # 删除员工
                emps.pop(del_i)
                print('成功删除！')
            else:
                # 取消操作
                print('操作已经取消！')

        else:
            # 输入有误
            print("您的输入有误！请重新输入")
        # 退出系统
    elif user_chose == '4':
        # 退出
        print("欢迎使用，再见！")
        input("请点击回车键退出！")
        break
    else:
        print("您的输入错误，请重新选择！")
    # 显示员工信息

    # 打印分割线
    print('-' * 60)
