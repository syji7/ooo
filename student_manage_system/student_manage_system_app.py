student_list = [{'name': '张三', 'id': '2', 'gender': '男'}]  # TODO 这玩意有问题,循环到这里数据存不上去


def append_student():
    student_dict = {}
    while True:
        if input('add or 输入任意键退出:'"\n") == 'add':
            student_dict['name'] = input('请输入姓名:')
            # ToDo 不能辨别传入的学号是不是已经存在:Student_list没有新增的学生字典
            for i in student_list:
                id_num = input('请输入学号:')
                print(i.values())
                if id_num not in i.values():
                    student_dict['id'] = id_num
                else:
                    print('学号输入重复,请重新确认')
            student_dict['gender'] = input('请输入性别:')
            student_dict = student_list.append(student_dict)
        else:
            break


def remove_student():
    # 删除列表里面的字典,那字典有什么特殊符号吗
    # 用name代表字典,删除name一样的字典{}
    # 先遍历列表student_list,如果输入的名字与键值相等,就 删除这个字典
    id_num = input('请输入你要删除的对象(以学号为准):')
    for i in student_list:
        if i['id'] == id_num:
            student_list.remove(i)
            print('删除成功')
            break


def xiugai_student():
    # 修改的其实是字典里面的键值,先调用列表的字典,然后根据[键值名]=''修改
    id_num = input('要修改的对应学号:')
    for i in student_list:
        if i['id'] == id_num:
            i['name'] = input('请输入姓名:')
            i['id'] = input('请输入学号:')
            i['gender'] = input('请输入性别:')
            print('修改成功')
            break


def find_student():
    id_num = input('请输入你要查询的对象(以学号为准):')
    for i in student_list:
        if i['id'] == id_num:
            print(f"姓名:{i['name']} 学号:{i['id']} 性别:{i['gender']}")
            break


def show_student_list():
    for i in student_list:
        print(f"姓名:{i['name']} 学号:{i['id']} 性别:{i['gender']}")


student_list = [{'name': '张三', 'id': '2', 'gender': '男'}]  # TODO 这玩意有问题,循环到这里数据存不上去
while True:

    print('------1.添加学生信息-------')
    print('------2.删除学生信息-------')
    print('------3.修改学生信息-------')
    print('------4.查询学生信息-------')
    print('------5.学生整体信息-------')
    print('------6.退出学生系统-------')
    i = int(input('选择操作:'))

    if i == 1:
        append_student()
    elif i == 2:
        remove_student()
    elif i == 3:
        xiugai_student()
    elif i == 4:
        find_student()
    elif i == 5:
        show_student_list()
    elif i == 6:
        exit('退出成功!')
    else:
        print('输入无效,请重新输入')
