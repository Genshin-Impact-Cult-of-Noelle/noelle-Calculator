import data.A as A
import data.E as E
import data.Q as Q
import data.weapons as wp
import data.Relics as Re
from calculation import Critical
import expect
import inspect
import output
import read_message
import cv2
from retrying import retry

class Noelle:
    message = '欢迎来到女仆诺艾尔的尾刀期望计算器v3.0版本-by-bilibili夜雪千沫'
    def __init__(self):
        print(Noelle.message)
Noelle()

#输入
def input_1():
    #用户的攻击力
#    global user_aggressivity    #用户的攻击力
#    global user_Defensivepower  #用户的防御力
    global user_noelle_number #命座
#  global noelle_number_defend #6命的50%防御力
    user_aggressivity = int(input('请输入你的女仆的攻击力:'))
    expect.user_aggressivity = user_aggressivity
    user_Defensivepower = int(input('请输入你的女仆的防御力:'))
    expect.user_Defensivepower = user_Defensivepower
    user_noelle_number = int(input('请输入你的女仆几命:'))
    assert 0 <= user_noelle_number <= 6, '命座输入错误！'
    if user_noelle_number == 6:
        expect.noelle_number_defend = 0.5
    elif 1 <= user_noelle_number <= 5 :
        expect.noelle_number_defend = 0

#    global user_A_Magnification
 #   global user_Q_Magnification

    expect.user_A_Magnification = int(input('请输入你的女仆的普攻倍率等级:'))
    assert 1 <= expect.user_A_Magnification <= 11,'普攻倍率等级输入错误'
  #  user_E_Magnification = str(input('请输入你的女仆的E倍率等级:'))
    expect.user_Q_Magnification = int(input('请输入你的女仆的大招倍率等级:'))
    assert 1 <= expect.user_A_Magnification <= 13, '大招倍率等级输入错误'

    global Q_data   #Q的防御力转化值
    Q_data = Q.Q_Magnification[expect.user_Q_Magnification]

def input_2():
    Critical.user_Critical_hit_rate = float(input('请输入暴击率（例：0.82）：'))
    assert 0.05 <= Critical.user_Critical_hit_rate <= 1,'暴击率输入错误！'
    Critical.user_Critical_damage = float(input('请输入暴击伤害（例：1.82）：'))
    assert 0.5 <= Critical.user_Critical_damage <= 5,'暴击伤害输入错误！'

def input_weapom():
    #输入用户的武器和导出武器数据
    wp.weapons_input()

def input_Relics():
    #输入用户的圣遗物和导出圣遗物数据
    Re.Relics_input()


#计算开大后攻击力
def the_aggressivity_of_Q():
    print(expect.noelle_number_defend)
    global the_aggressivity_of_Q_data
    the_aggressivity_of_Q_data = expect.user_Defensivepower * ( expect.noelle_number_defend + Q_data ) + expect.user_aggressivity
    print('test女仆开大后攻击力为：' + str(the_aggressivity_of_Q_data))

#启用练度检查模块
def start_inspect():
    inspect_noelle = inspect.Inspect()  #创建实例
    inspect_noelle.inspect_choose()  # 选择
    if inspect.num == 1:
        inspect_noelle.inspect_skill()  # 检查天赋
        inspect_noelle.inspect_expect()  # 检查期望



def error(a):
    none = True
    while none:
        try:
            a()
            none = False
        except ValueError as e1:
            print('请输入整数！', e1)
        except AssertionError as e2:
            print(e2)


if __name__=='__main__':
    read_message.read_choose()
    error(input_1)             #调用输入攻击防御的函数
    error(the_aggressivity_of_Q)  #计算开大攻击
    error(input_2)   #输入暴击率和爆伤
    error(Critical.the_Critical_expect)
    error(input_weapom)  #选择武器
    error(input_Relics)  #选择圣遗物
    expect.the_noelle_expect()  #计算期望
    start_inspect()  #检查练度
    output.ouput_choose()
    print(Noelle.message)


'''
if __name__=='__main__':
    try:            #捕获异常
        input_1()             #调用输入攻击防御的函数
        the_aggressivity_of_Q()  #计算开大攻击
        input_2()   #输入暴击率和爆伤
        Critical.the_Critical_expect()
        input_weapom()  #选择武器
        input_Relics()  #选择圣遗物
    except ValueError as e1:    #处理异常
        print('请输入整数！',e1)
        exit()
    except AssertionError as e2:
        print(e2)
        exit()
    else:
        expect.the_noelle_expect()  #计算期望
        start_inspect()  #检查练度
    finally:
        print(Noelle.message)
'''
