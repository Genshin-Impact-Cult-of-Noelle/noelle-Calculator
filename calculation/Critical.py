import data.A as A
import data.E as E
import data.Q as Q
import data.weapons as wp
import data.Relics as Re

#计算暴击率*爆伤加1
def the_Critical_expect():
    global user_Critical_hit_rate  # 用户的暴击率
    global user_Critical_damage  # 用户的暴击伤害
    global the_Critical_expect_number
    the_Critical_expect_number = ( user_Critical_hit_rate * user_Critical_damage ) + 1
    print('暴击率和爆伤的期望值为：' + str(the_Critical_expect_number))
