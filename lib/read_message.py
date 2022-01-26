import sys
sys.path.append("..")

def read_choose():
    with open('readme.txt', 'r', encoding ='utf-8')as file:
        message = file.read()
        print(message)
        global num
        none = True
        num = int(input('请阅读后选择(1：是,2：不用):'))
        while none:
            if num == 1:
                states = '我已经阅读上述事项'
                print(states)
                none = False
            elif num == 2:
                states = '你必须读！'
                print(states)
                num = int(input('请重新输入:'))
            else:
                num = int(input('请输入正确数字!!!,请重新输入:'))
