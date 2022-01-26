import data.A as A
import data.E as E
import data.Q as Q
import data.weapons as wp
import data.Relics as Re
from calculation import Critical
'''
def star():
    global noelle_number_defend
    user_noelle_number = int(input('请输入你的女仆几命:'))
    assert 0 <= user_noelle_number <= 6, '命座输入错误！'
    if user_noelle_number == 6:
        noelle_number_defend = 0.5
    elif 1 <= user_noelle_number <= 5 :
        noelle_number_defend = 0
'''


def the_noelle_expect():
    global user_aggressivity  #用户的攻击力
    global user_Defensivepower  #用户的防御力
    global user_A_Magnification  #用户的普攻等级
    global user_Q_Magnification  #用户的大招等级
    global Q_data  # Q的防御力转化值
    #  global E_data
    global A1_data  #普攻倍率
    global A2_data
    global A3_data
    global A4_data
    Q_data = Q.Q_Magnification[user_Q_Magnification]
    #  E_data = data.E.E_Magnification[user_E_Magnification]
    A1_data = A.A1_Magnification[user_A_Magnification]
    A2_data = A.A2_Magnification[user_A_Magnification]
    A3_data = A.A3_Magnification[user_A_Magnification]
    A4_data = A.A4_Magnification[user_A_Magnification]
    global noelle_number_defend  #判断是0还是0.5
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
    two = Critical.the_Critical_expect_number
    global max_three #第三乘区
    max_three = ( 1 + Re.All_hurt_on + 0.466 + 0.15 + wp.weapon_All_hurt_on )

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
    min_three = ( 1 + Re.All_hurt_off + 0.466 + 0.15 + wp.weapon_All_hurt_off)

    global A1_hurt_max  #第一刀最大伤害
    global A1_hurt_min
    global A2_hurt_max  #第二刀最大伤害
    global A2_hurt_min
    global A3_hurt_max
    global A3_hurt_min
    global A4_hurt_max
    global A4_hurt_min
    global tiankong_bo
    global tiankong_bo_expect
    tiankong_bo = the_aggressivity_of_Q_data_max * (1 + Critical.user_Critical_damage) * ( 1 + 0.15 + wp.weapon_All_hurt_on) * wp.weapon_Firm_but_gentle
    tiankong_bo_expect = the_aggressivity_of_Q_data_max * two * (1 + 0.15 + wp.weapon_All_hurt_on) * wp.weapon_Firm_but_gentle
    #每刀的实际伤害
    A1_hurt_max = max_A1_one * (1 + Critical.user_Critical_damage) * max_three + tiankong_bo
    A2_hurt_max = max_A2_one * (1 + Critical.user_Critical_damage) * max_three + tiankong_bo
    A3_hurt_max = max_A3_one * (1 + Critical.user_Critical_damage) * max_three + tiankong_bo
    A4_hurt_max = max_A4_one * (1 + Critical.user_Critical_damage) * max_three + tiankong_bo
    A1_hurt_min = min_A1_one * (1 + Critical.user_Critical_damage) * min_three
    A2_hurt_min = min_A2_one * (1 + Critical.user_Critical_damage) * min_three
    A3_hurt_min = min_A3_one * (1 + Critical.user_Critical_damage) * min_three
    A4_hurt_min = min_A4_one * (1 + Critical.user_Critical_damage) * min_three

    global kang  #急冻树抗性(双岩)
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
    the_noelle_expect_max = max_A4_one * two * max_three + tiankong_bo_expect
    print('该女仆的最大输出期望值为：{:.2f}'.format(the_noelle_expect_max*kang))
    the_noelle_expect_min = min_A4_one * two * min_three
    print('该女仆的最小输出期望值为：{:.2f}'.format(the_noelle_expect_min*kang))


