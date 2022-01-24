none = {'1':0,'2': 0, '3': 0, '4': 0, '5': 0}
#全伤
chigu_All_hurt = {'1':0.3,'2': 0.35, '3': 0.4, '4': 0.45, '5': 0.5}
tiankong_All_hurt = {'1':0.08,'2': 0.1, '3': 0.12, '4': 0.14, '5': 0.16}
#攻击
wugong_on_attck = {'1':0.4,'2': 0.5, '3': 0.6, '4': 0.7, '5': 0.8}
wugong_off_attck = {'1':0.2,'2': 0.25, '3': 0.3, '4': 0.35, '5': 0.4}
lang_attck =  {'1':0.4,'2': 0.5, '3': 0.6, '4': 0.7, '5': 0.8}
baiyin_attck =  {'1':0.24,'2': 0.30, '3': 0.36, '4': 0.42, '5': 0.48}
#防御
baiyin_defend = {'1':0.24,'2': 0.30, '3': 0.36, '4': 0.42, '5': 0.48}
#防御特效
chijue_Special_effects = {'1':0.4,'2': 0.5, '3': 0.6, '4': 0.7, '5': 0.8}
#刀波
tiankong_Firm_but_gentle = {'1':0.8,'2': 1, '3': 1.2, '4': 1.4, '5': 1.6}


weapons_list = {'1':'赤角','2': '螭骨', '3': '天空', '4': '白影', '5': '无工', '6': '狼末','7': '黑岩','8': '西风'}

def weapons_input():
    print(str('1:赤角,2: 螭骨, 3: 天空, 4: 白影, 5: 无工, 6: 狼末,7: 黑岩,8: 西风'))
    #选择武器
    global user_weapon             #用户的武器
    global user_weapon_number      #用户的武器的精炼度
    global user_weapon_key
    global user_weapon_number_key

    global All_hurt_on             #全伤吃满被动
    global All_hurt_off            #全伤无被动
    global attck_on                #攻击
    global attck_off
    global defend_on               #防御
    global defend_off
    global Special_effects         #防御特效
    global Firm_but_gentle         #刀波
    global bai_attck


    user_weapon = str(input('请选择你的武器:'))
    user_weapon_key = user_weapon[0:2]

    user_weapon_number = str(input('请输入武器精炼度:'))
    user_weapon_number_key = user_weapon_number[0:2]

    print('该武器为：' + str(weapons_list[user_weapon_key]))
    if  user_weapon == '1':
        bai_attck = 542
        All_hurt_on = All_hurt_off = none
        attck_on = attck_off = none
        defend_on = defend_off = none
        Special_effects = chijue_Special_effects
        Firm_but_gentle = none

    elif user_weapon == '2': #螭骨
        bai_attck = 510
        All_hurt_on = chigu_All_hurt      #螭骨吃满被动

        All_hurt_off = none
        attck_on = attck_off = none
        defend_on = defend_off = none
        Special_effects = none
        Firm_but_gentle = none

    elif user_weapon == '3':   #天空
        bai_attck = 674
        All_hurt_on = All_hurt_off = tiankong_All_hurt
        Firm_but_gentle = tiankong_Firm_but_gentle

        attck_on = attck_off = none
        defend_on = defend_off = none
        Special_effects = none

    elif user_weapon == '4':#白影
        bai_attck = 510
        attck_on = defend_on = baiyin_attck
        attck_off = defend_off = none
        All_hurt_on = All_hurt_off = none
        Special_effects = none
        Firm_but_gentle = none

    elif user_weapon == '5':#无工
        bai_attck = 608
        attck_on = wugong_on_attck
        attck_off = wugong_off_attck

        All_hurt_on = All_hurt_off = none
        defend_on = defend_off = none
        Special_effects = none
        Firm_but_gentle = none
    elif user_weapon == '6':#狼末
        bai_attck = 608
        attck_on = lang_attck

        attck_off = none
        All_hurt_on = All_hurt_off = none
        defend_on = defend_off = none
        Special_effects = none
        Firm_but_gentle = none
    elif user_weapon == '7':#黑岩
        bai_attck = 510
        attck_on = lang_attck

        attck_off = none
        All_hurt_on = All_hurt_off = none
        defend_on = defend_off = none
        Special_effects = none
        Firm_but_gentle = none
    elif user_weapon == '8':#西风
        bai_attck = 510
        attck_on = attck_off = none
        All_hurt_on = All_hurt_off = none
        defend_on = defend_off = none
        Special_effects = none
        Firm_but_gentle = none
    else:
        All_hurt_on = All_hurt_off = none



    global weapon_All_hurt_on  # 全伤吃满被动
    global weapon_All_hurt_off  # 全伤无被动
    global weapon_attck_on  # 攻击
    global weapon_attck_off
    global weapon_defend_on  # 防御
    global weapon_defend_off
    global weapon_Special_effects  # 防御特效
    global weapon_Firm_but_gentle  # 刀波
    global weapon_bai_attck

    weapon_All_hurt_on = All_hurt_on[user_weapon_number_key]
    weapon_All_hurt_off = All_hurt_off[user_weapon_number_key]
    weapon_attck_on = attck_on[user_weapon_number_key]
    weapon_attck_off = attck_off[user_weapon_number_key]
    weapon_defend_on = defend_on[user_weapon_number_key]
    weapon_defend_off = defend_off[user_weapon_number_key]
    weapon_Special_effects = Special_effects[user_weapon_number_key]
    weapon_Firm_but_gentle = Firm_but_gentle[user_weapon_number_key]
    weapon_bai_attck = bai_attck

if __name__=='__main__':
    weapons_input()
    print(str(weapons_list[user_weapon_key] + '的吃满被动的全伤为：' + str(weapon_All_hurt_on)))
    print(str(weapons_list[user_weapon_key] + '的无被动的全伤为：' + str(weapon_All_hurt_off)))
    print(str(weapons_list[user_weapon_key] + '的吃满被动的加的攻击为：' + str(weapon_attck_on)))
    print(str(weapons_list[user_weapon_key] + '的无被动的加的攻击为：' + str(weapon_attck_off)))
    print(str(weapons_list[user_weapon_key] + '的吃满被动的加的防御为：' + str(weapon_defend_on)))
    print(str(weapons_list[user_weapon_key] + '的无被动的加的防御为：' + str(weapon_defend_off)))
    print(str(weapons_list[user_weapon_key] + '的特效防御加伤为：' + str(weapon_Special_effects)))
    print(str(weapons_list[user_weapon_key] + '的刀波为：' + str(weapon_Firm_but_gentle)))
    print(str(weapons_list[user_weapon_key] + '的白值为：' + str(weapon_bai_attck)))

