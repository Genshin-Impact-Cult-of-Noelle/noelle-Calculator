Relics_list = {1:'角斗士',2: '逆飞', 3: '华馆'}

def Relics_input():
    print(str('1:角斗士,2: 逆飞, 3: 华馆'))
    #选择圣遗物
    global user_Relics             #用户的圣遗物
    global user_Relics_key

    global All_hurt             #全伤吃满被动
    global defend_on              #防御
    global defend_off

    user_Relics = int(input('请选择你的圣遗物:'))
    assert 1 <= user_Relics <= 3, '圣遗物输入错误！'

    print('该圣遗物为：' + str(Relics_list[user_Relics]))
    if user_Relics == '1':   #角斗士
        All_hurt = 0.35
        defend_on = defend_off = 0

    elif user_Relics == '2': #逆飞
        All_hurt = 0.4
        defend_on = defend_off = 0

    elif user_Relics == '3': #华馆
        All_hurt = 0.24
        defend_on = 0.24
        defend_off = 0

    else:
        All_hurt = 0
        defend_on = defend_off = 0


if __name__=='__main__':
    Relics_input()
    print(str(Relics_list[user_Relics] + '的全伤为：' + str(All_hurt)))
    print(str(Relics_list[user_Relics] + '的防御1为：' + str(defend_on)))
    print(str(Relics_list[user_Relics] + '的防御2为：' + str(defend_off)))
