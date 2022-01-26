import sys
sys.path.append("..")
import data.A as A
import data.E as E
import data.Q as Q
import data.weapons as wp
import data.Relics as Re
from calculation import Critical
import expect

class Inspect:
    message = '========检查练度模块启动中========'

    def __init__(self):
        print(Inspect.message)


    def inspect_choose(self):
        global num
        none = True
        num = int(input('是否检查你的女仆的练度(1：是,2：不用):'))
        while none:
            if num == 1:
                states = '检查模块启动！开始导入........'
                print(states)
                none = False
            elif num == 2:
                states = '检查模块已停止！'
                print(states)
                none = False
            else:
                num = int(input('请输入正确数字!!!,请重新输入:'))

    def inspect_skill(self):
        if expect.user_A_Magnification < 9:
            print('你的普攻等级过低！')
        if expect.user_Q_Magnification < 12:
            print('你的大招等级过低！')
        if expect.user_A_Magnification < expect.user_Q_Magnification - 3:
            print('先拉普攻！！哼啊啊啊啊啊啊啊啊！')

    def inspect_expect(self):
        kang = expect.kang
        if expect.the_noelle_expect_max*kang < 18000:
            print('你的女仆DPS不及格！')
        elif 18000 < expect.the_noelle_expect_max*kang < 22000:
            print('你的女仆处于及格水平')
        elif 22000 < expect.the_noelle_expect_max*kang < 24000:
            print('你的女仆处于小毕业水平')
        elif 24000 < expect.the_noelle_expect_max*kang:
            print('你的女仆已经毕业啦！')



inspect_noelle = Inspect()
#inspect_noelle.inspect_choose()
#if num == 1:
#    inspect_noelle.inspect_skill()
 #   inspect_noelle.inspect_expect()