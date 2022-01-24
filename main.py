import data.A
import data.E
import data.Q
import data.weapons as wp
import data.Relics as Re


class noelle:
    message = '欢迎来到女仆诺艾尔的尾刀期望计算器v3.0版本-by-bilibili夜雪千沫'
    def __init__(self):
        print(noelle.message)
noelle()

#输入
def input_1():
    #用户的攻击力
    global user_aggressivity    #用户的攻击力
    global user_Defensivepower  #用户的防御力
    global user_noelle_number #命座
    global noelle_number_defend #6命的50%防御力
    global Q_Magnification_key
    global A_Magnification_key
    global E_Magnification_key

    user_aggressivity = int(input('请输入你的女仆的攻击力:'))
    user_Defensivepower = int(input('请输入你的女仆的防御力:'))
    user_noelle_number = int(input('请输入你的女仆几命:'))
    if user_noelle_number == 6:
        noelle_number_defend = 0.5
    elif 1 <= user_noelle_number <= 5 :
        noelle_number_defend = 0

    user_A_Magnification = str(input('请输入你的女仆的普攻倍率等级:'))
  #  user_E_Magnification = str(input('请输入你的女仆的E倍率等级:'))
    user_Q_Magnification = str(input('请输入你的女仆的大招倍率等级:'))
    A_Magnification_key = user_A_Magnification[0:2]
  #  E_Magnification_key = user_E_Magnification[0:2]
    Q_Magnification_key = user_Q_Magnification[0:2]
    global Q_data   #Q的防御力转化值
  #  global E_data
    global A1_data
    global A2_data
    global A3_data
    global A4_data
    Q_data = data.Q.Q_Magnification[Q_Magnification_key]
  #  E_data = data.E.E_Magnification[E_Magnification_key]
    A1_data = data.A.A1_Magnification[A_Magnification_key]
    A2_data = data.A.A2_Magnification[A_Magnification_key]
    A3_data = data.A.A3_Magnification[A_Magnification_key]
    A4_data = data.A.A4_Magnification[A_Magnification_key]


 #   data.Q.Q_Magnification[da_Magnification_key]

def input_2():
    #双爆
    global user_Critical_hit_rate  #用户的暴击率
    global user_Critical_damage    #用户的暴击伤害
    user_Critical_hit_rate = float(input('请输入暴击率（例：0.82）：'))
    if user_Critical_hit_rate >= 1 or user_Critical_hit_rate <= 0.05:
        raise ValueError('暴击率输入错误！')
    user_Critical_damage = float(input('请输入暴击伤害（例：1.82）：'))
    if user_Critical_damage >= 5 or user_Critical_damage <= 0.5:
        raise ValueError('暴击伤害输入错误！')

def input_weapom():
    #输入用户的武器和导出武器数据
    wp.weapons_input()

def input_Relics():
    Re.Relics_input()


#计算开大后攻击力
def the_aggressivity_of_Q():
    global the_aggressivity_of_Q_data
    the_aggressivity_of_Q_data = user_Defensivepower * ( noelle_number_defend + Q_data ) + user_aggressivity
    print('test女仆开大后攻击力为：' + str(the_aggressivity_of_Q_data))


#计算暴击率*爆伤
def the_Critical_expect():
    global the_Critical_expect_number
    the_Critical_expect_number = ( user_Critical_hit_rate * user_Critical_damage ) + 1
    print('暴击率和爆伤的期望值为：' + str(the_Critical_expect_number))


def the_noelle_expect():
    global the_noelle_expect_max #最大期望
    global the_noelle_expect_min #最小期望
    global aggressivity_max  #最大攻击
    global aggressivity_min
    global Defensivepower_max  #最大防御
    global Defensivepower_min

    # 算上华馆的被动和武器被动得出最终防御和攻击
    Defensivepower_max = user_Defensivepower + 799 * Re.defend_on + 799 * wp.weapon_defend_on
    Defensivepower_min = user_Defensivepower + 799 * Re.defend_off + 799 * wp.weapon_defend_off
    aggressivity_max = user_aggressivity + ( 191 + wp.weapon_bai_attck ) *  wp.weapon_attck_on
    aggressivity_min = user_aggressivity + ( 191 + wp.weapon_bai_attck ) *  wp.weapon_attck_off

    global max_A1_one #第一乘区
    global max_A2_one #第一乘区
    global max_A3_one #第一乘区
    global max_A4_one #第一乘区
    global the_aggressivity_of_Q_data_max #最大开大攻击力
    the_aggressivity_of_Q_data_max = Defensivepower_max * ( noelle_number_defend + Q_data ) + aggressivity_max
    #print('女仆吃满被动时的开大攻击力为：' + str(the_aggressivity_of_Q_data_max))
    max_A1_one = the_aggressivity_of_Q_data_max * A1_data + Defensivepower_max * wp.weapon_Special_effects
    max_A2_one = the_aggressivity_of_Q_data_max * A2_data + Defensivepower_max * wp.weapon_Special_effects
    max_A3_one = the_aggressivity_of_Q_data_max * A3_data + Defensivepower_max * wp.weapon_Special_effects
    max_A4_one = the_aggressivity_of_Q_data_max * A4_data + Defensivepower_max * wp.weapon_Special_effects
    global two #第二乘区
    two = the_Critical_expect_number
    global max_three #第三乘区
    max_three = ( 1 + Re.All_hurt + 0.466 + 0.15 + wp.weapon_All_hurt_on )

    global min_A1_one
    global min_A2_one
    global min_A3_one
    global min_A4_one  # 第一乘区
    global the_aggressivity_of_Q_data_min  # 最大开大攻击力
    the_aggressivity_of_Q_data_min = Defensivepower_min * (noelle_number_defend + Q_data) + aggressivity_min
    #print('女仆无被动时的开大攻击力为：' + str(the_aggressivity_of_Q_data_min))
    min_A1_one = the_aggressivity_of_Q_data_min * A1_data + Defensivepower_min * wp.weapon_Special_effects
    min_A2_one = the_aggressivity_of_Q_data_min * A2_data + Defensivepower_min * wp.weapon_Special_effects
    min_A3_one = the_aggressivity_of_Q_data_min * A3_data + Defensivepower_min * wp.weapon_Special_effects
    min_A4_one = the_aggressivity_of_Q_data_min * A4_data + Defensivepower_min * wp.weapon_Special_effects
    global min_three  # 第三乘区
    min_three = ( 1 + Re.All_hurt + 0.466 + 0.15 + wp.weapon_All_hurt_off)

    global A1_hurt_max  #第一刀最大伤害
    global A1_hurt_min
    global A2_hurt_max  #第二刀最大伤害
    global A2_hurt_min
    global A3_hurt_max
    global A3_hurt_min
    global A4_hurt_max
    global A4_hurt_min
    global tiankong_bo
    tiankong_bo = the_aggressivity_of_Q_data_max * (1 + user_Critical_damage) * ( 1 + 0.15 + wp.weapon_All_hurt_on)
    #每刀的实际伤害
    A1_hurt_max = max_A1_one * (1 + user_Critical_damage) * max_three
    A2_hurt_max = max_A2_one * (1 + user_Critical_damage) * max_three
    A3_hurt_max = max_A3_one * (1 + user_Critical_damage) * max_three
    A4_hurt_max = max_A4_one * (1 + user_Critical_damage) * max_three
    A1_hurt_min = min_A1_one * (1 + user_Critical_damage) * min_three
    A2_hurt_min = min_A2_one * (1 + user_Critical_damage) * min_three
    A3_hurt_min = min_A3_one * (1 + user_Critical_damage) * min_three
    A4_hurt_min = min_A4_one * (1 + user_Critical_damage) * min_three

    global kang
    kang = 1/2.237216*1.1666666

    print('女仆吃满被动时的开大攻击力为：{:.2f}'.format(the_aggressivity_of_Q_data_max))
    print('女仆第一刀的伤害为：{:.2f}'.format(A1_hurt_max*kang))
    print('女仆第二刀的伤害为：{:.2f}'.format(A2_hurt_max*kang))
    print('女仆第三刀的伤害为：{:.2f}'.format(A3_hurt_max*kang))
    print('女仆第四刀的伤害为：{:.2f}'.format(A4_hurt_max*kang))
    print('女仆无被动时的开大攻击力为：{:.2f}'.format(the_aggressivity_of_Q_data_min))
    print('女仆第一刀的伤害为：{:.2f}'.format(A1_hurt_min*kang))
    print('女仆第二刀的伤害为：{:.2f}'.format(A2_hurt_min*kang))
    print('女仆第三刀的伤害为：{:.2f}'.format(A3_hurt_min*kang))
    print('女仆第四刀的伤害为：{:.2f}'.format(A4_hurt_min*kang))
    the_noelle_expect_max = max_A4_one * two * max_three
    print('该女仆的最大输出期望值为：{:.2f}'.format(the_noelle_expect_max*kang))
    the_noelle_expect_min = min_A4_one * two * min_three
    print('该女仆的最小输出期望值为：{:.2f}'.format(the_noelle_expect_min*kang))


if __name__=='__main__':
    try:                       #捕获异常
        input_1()             #调用输入攻击防御的函数
        the_aggressivity_of_Q()
        input_2()             #调用输入攻击防御的函数
    except ValueError as e1:    #处理异常
        print('请检查输入格式!',e1)
        exit()
    try:
        the_Critical_expect()
    except ValueError as e2:
        print('请检查输入格式!',e2)
        exit()
        input_weapom()
        input_Relics()
        the_noelle_expect()
    finally:
        print(noelle.message)
