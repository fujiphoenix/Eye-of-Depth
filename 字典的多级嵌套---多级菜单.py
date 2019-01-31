#!/usr/bin/env python
# coding: utf-8

# In[ ]:


menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '电子厂':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{
            '陆家嘴':{
                'apple store':{}
            }
        },
    },
    '广州':{
        '黄埔':{
            "科学城":{
                '地铁口':{}
            }
        },
        '天河':{
            '火车东站':{
                '希尔顿':{}
            }
        },
    },
}

exit_flag = False  # 设置全局变量，用来退出循环，实现任意一级菜单都可以退出
while not exit_flag:
    
    for i1 in menu:  # 读取第一级菜单
        print(i1)
    choice = input('选择进入第1层，按q退出：')
    if choice in menu:
        while not exit_flag:
            for i2 in menu[choice]:  # 读取第二级菜单
                print(i2)
            choice2 = input('选择进入第2层,按b返回上一级，按q退出：')
            if choice2 in menu[choice]:
                while not exit_flag:
                    for i3 in menu[choice][choice2]:  # 读取第三级菜单
                        print(i3)
                    choice3 = input('选择进入第3层,按b返回上一级，按q退出：')
                    if choice3 in menu[choice][choice2]:
                        for i4 in menu[choice][choice2][choice3]:
                            print(i4)
                        choice4 = input('最后一层，按b返回上一级，按q退出：')
                        if choice4 == 'b':
                            break
                        if choice4 == 'q':
                            exit_flag = True
                    if choice3 == 'b':
                        break
                    if choice3 == 'q':
                        exit_flag = True
            if choice2 == 'b':
                break
            if choice2 == 'q':
                exit_flag = True
    if choice == 'q':
        exit_flag = True


