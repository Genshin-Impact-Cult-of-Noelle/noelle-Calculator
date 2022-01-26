import cv2
import os
import sys
sys.path.append("..")
import expect


def output_index():
    global index_name
    print('\n','='*20,'开始导出数据至本地..... ','\n','='*20)
    index_name = str(input('请输入文件的名称：'))
    file = open(index_name,'w',encoding='utf-8')
    file.write(str('女仆吃满被动时的开大攻击力为：{:.2f}'.format(expect.the_aggressivity_of_Q_data_max))+'\n')
    file.write(str('女仆第一刀的伤害为：{:.2f}'.format(expect.A1_hurt_max*expect.kang))+'\n')
    file.write(str('女仆第二刀的伤害为：{:.2f}'.format(expect.A2_hurt_max * expect.kang))+'\n')
    file.write(str('女仆第三刀的伤害为：{:.2f}'.format(expect.A3_hurt_max * expect.kang))+'\n')
    file.write(str('女仆第四刀的伤害为：{:.2f}'.format(expect.A4_hurt_max * expect.kang))+'\n')
    file.write(str('女仆无被动时的开大攻击力为：{:.2f}'.format(expect.the_aggressivity_of_Q_data_min))+'\n')
    file.write(str('女仆第一刀的伤害为：{:.2f}'.format(expect.A1_hurt_min * expect.kang))+'\n')
    file.write(str('女仆第二刀的伤害为：{:.2f}'.format(expect.A2_hurt_min * expect.kang))+'\n')
    file.write(str('女仆第三刀的伤害为：{:.2f}'.format(expect.A3_hurt_min * expect.kang))+'\n')
    file.write(str('女仆第四刀的伤害为：{:.2f}'.format(expect.A4_hurt_min * expect.kang))+'\n')
    file.write(str('该女仆的最大输出期望值为：{:.2f}'.format(expect.the_noelle_expect_max * expect.kang))+'\n')
    file.write(str('该女仆的最小输出期望值为：{:.2f}'.format(expect.the_noelle_expect_min * expect.kang))+'\n')
    print('\n保存成功\n')
    file.close()

def ouput_choose():
    global num
    none = True
    num = int(input('是否保存到本地？(1：是,2：不用):'))
    while none:
        if num == 1:
            states = '开始保存........'
            print(states)
            output_index()
            none = False
        elif num == 2:
            states = '退出保存'
            print(states)
            none = False
        else:
            num = int(input('请输入正确数字!!!,请重新输入:'))


if __name__=='__main__':
    ouput_choose()
