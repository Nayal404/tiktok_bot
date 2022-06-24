import time 
import pyautogui as pg 
import webbot as wb
# creating a class for the bot so that i don't have to repeat the codes again😎
# and also to make the code look simple😁
class TiktokBot:
    def __init__(self, number, msg):
        self.number = number 
        self.msg = msg
    # Logic for autoLiking function👍❤
    def autoLiker(self):
        for i in range(self.number):
            # Coordinate of like button is in x-axis=> 550, & y-axis=>520
            pg.moveTo(550, 520)
            time.sleep(3)
            pg.doubleClick()
            time.sleep(1)
            pg.scroll(-16)
    # Logic for auto commenting functino for tiktok💻🖥🖱
    def autoCommenter(self):
        for i in range(self.number):
            # tiktok comment is in coordinate of x-axis => 937 && y-axis=> 633
            pg.moveTo(937, 633)
            wb.go_to('https://tiktok.com')
            wb.type(f'{message}')
            wb.press(wb.key.Enter)
if __name__ == "__main__":
    comment = int(input('How many Comments to deploy, Enter here: '))
    message = input('Enter your message: ')
    deploy = TiktokBot(comment, f'{message}')
    print('''
Press 1: For autoLiker
Press 2: For autoComment
    ''')
    userChoice = int(input())
    if userChoice == 1:
        deploy.autoLiker()
    elif userChoice == 2:
        deploy.autoCommenter()
    else:
        try:
            print('Invalid Option Error 404*____*')
            quit()
        except ValueError:
            print('Try to type the above options only!')
            print(ValueError)