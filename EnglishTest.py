from tkinter import *
from PIL import ImageTk
root = Tk() 
root.title('EnglisgTest')
root.geometry('1300x800')
icon = PhotoImage(file='new-logo.png')
root.iconphoto(True,icon)
img = PhotoImage(file = "FonTest.png")


canvas = Canvas(root, width=1920, height = 1080)
fon = canvas.create_image(0, 0, image = img, anchor = NW)


ball = 0 

def funct101():
    global ball
    canvas.delete(can60)
    ball+=1
    if ball >= 50:
         canvas.create_text(650, 200, text = 'Excellent!\nYou scored '+ str(ball) +' points\nYour level is "C1 and higher"',font=('Helvetica', 60, 'bold'))
    elif ball >= 40:
         canvas.create_text(650, 200, text = 'Cool!\nYou scored '+ str(ball) +' points\nYour level is "B2"',font=('Helvetica', 60, 'bold'))
    elif ball >= 30:
          canvas.create_text(650, 200, text = 'Good!\nYou scored '+ str(ball) +' points\nYour level is "B1"',font=('Helvetica', 60, 'bold'))
    elif ball >= 20:
         canvas.create_text(650, 200, text = 'Not bad!\nYou scored '+ str(ball) +' points\nYour level is "A2"',font=('Helvetica', 60, 'bold'))
    elif ball >= 10:
         canvas.create_text(650, 200, text = 'You have to study harder\nYou scored '+ str(ball) +' points\nYour level is "A1"',font=('Helvetica', 60, 'bold'))
    elif ball < 10:
          canvas.create_text(650, 200, text = 'You scored '+ str(ball) +' points\nSign up for our classes soon!',font=('Helvetica', 60, 'bold'))
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
def funct100():
    canvas.delete(can60)
    if ball >= 50:
          canvas.create_text(650, 200, text = 'Excellent!\nYou scored '+ str(ball) +' points\nYour level is "C1 and higher"',font=('Helvetica', 60, 'bold'))
    elif ball >= 40:
          canvas.create_text(650, 200, text = 'Cool!\nYou scored '+ str(ball) +' points\nYour level is "B2"',font=('Helvetica', 60, 'bold'))
    elif ball >= 30:
          canvas.create_text(650, 200, text = 'Good!\nYou scored '+ str(ball) +' points\nYour level is "B1"',font=('Helvetica', 60, 'bold'))
    elif ball >= 20:
          canvas.create_text(650, 200, text = 'Not bad!\nYou scored '+ str(ball) +' points\nYour level is "A2"',font=('Helvetica', 60, 'bold'))
    elif ball >= 10:
          canvas.create_text(650, 200, text = 'You have to study harder\nYou scored '+ str(ball) +' points\nYour level is "A1"',font=('Helvetica', 60, 'bold'))
    elif ball < 10:
          canvas.create_text(650, 200, text = 'You scored '+ str(ball) +' points\nSign up for our classes soon!',font=('Helvetica', 60, 'bold'))
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()


# def funct()
#      canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = ''
#      b1.config(text = '', command = )
#      b2.config(text = '', command = )
#      b3.config(text = '', command = )
#      b4.config(text = '', command = )


def funct99():
    global can60, ball
    canvas.delete(can59)
    ball+=1
    can60=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I feel very _____. I`m going to go to bed!')
    b1.config(text = 'nap', command = funct100)
    b2.config(text = 'asleep', command = funct100)
    b3.config(text = 'sleepy', command = funct101)
    b4.config(text = 'sleeper', command = funct100)
def funct98():
    global can60
    canvas.delete(can59)
    can60=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I feel very _____. I`m going to go to bed!')
    b1.config(text = 'nap', command = funct100)
    b2.config(text = 'asleep', command = funct100)
    b3.config(text = 'sleepy', command = funct101)
    b4.config(text = 'sleeper', command = funct100)
def funct97():
    global can59, ball
    canvas.delete(can58)
    ball+=1
    can59=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I phoned her _____ I heard the news.')
    b1.config(text = 'minute', command = funct98, width = 16)
    b2.config(text = 'during', command = funct98, width = 16)
    b3.config(text = 'by the time', command = funct98, width = 16)
    b4.config(text = 'the moment', command = funct99, width = 16)
def funct96():
    global can59
    canvas.delete(can58)
    can59=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I phoned her _____ I heard the news.')
    b1.config(text = 'minute', command = funct98, width = 16)
    b2.config(text = 'during', command = funct98, width = 16)
    b3.config(text = 'by the time', command = funct98, width = 16)
    b4.config(text = 'the moment', command = funct99, width = 16)
def funct95():
    global can58, ball
    canvas.delete(can57)
    ball+=1
    can58=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Come on! Quick! Let`s get _____ !')
    b1.config(text = 'highlight', command = funct96, width = 18)
    b2.config(text = 'cracking', command = funct97, width = 18)
    b3.config(text = 'massive', command = funct96, width = 18)
    b4.config(text = 'with immediate effect', command = funct96, width = 18)
def funct94():
    global can58
    canvas.delete(can57)
    can58=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Come on! Quick! Let`s get _____ !')
    b1.config(text = 'highlight', command = funct96, width = 18)
    b2.config(text = 'cracking', command = funct97, width = 18)
    b3.config(text = 'massive', command = funct96, width = 18)
    b4.config(text = 'with immediate effect', command = funct96, width = 18)
def funct93():
    global can57, ball
    canvas.delete(can56)
    ball+=1
    can57=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I think it`s very easy to _____ debt these days.')
    b1.config(text = 'go into', command = funct94)
    b2.config(text = 'become', command = funct94)
    b3.config(text = 'go down to', command = funct94)
    b4.config(text = 'get into', command = funct95)
def funct92():
    global can57
    canvas.delete(can56)
    can57=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I think it`s very easy to _____ debt these days.')
    b1.config(text = 'go into', command = funct94)
    b2.config(text = 'become', command = funct94)
    b3.config(text = 'go down to', command = funct94)
    b4.config(text = 'get into', command = funct95)
def funct91():
    global can56, ball
    canvas.delete(can55)
    ball+=1
    can56=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'They`re coming to our house _____ Saturday.')
    b1.config(text='in', command = funct92)
    b2.config(text='at', command = funct92)
    b3.config(text = 'on', command = funct93)
    b4.config(text = 'with', command = funct92)
def funct90():
    global can56
    canvas.delete(can55)
    can56=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'They`re coming to our house _____ Saturday.')
    b1.config(text='in', command = funct92)
    b2.config(text='at', command = funct92)
    b3.config(text = 'on', command = funct93)
    b4.config(text = 'with', command = funct92)
def funct89():
    global can55, ball
    canvas.delete(can54)
    ball+=1
    can55=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Hello, this is Simon. Could I _____ to Jane, please?')
    b1.config(text='say', command = funct90)
    b2.config(text='tell', command = funct90)
    b3.config(text = 'call', command = funct90)
    b4.config(text = 'speak', command = funct91)
def funct88():
    global can55
    canvas.delete(can54)
    can55=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Hello, this is Simon. Could I _____ to Jane, please?')
    b1.config(text='say', command = funct90)
    b2.config(text='tell', command = funct90)
    b3.config(text = 'call', command = funct90)
    b4.config(text = 'speak', command = funct91)
def funct87():
    global can54, ball
    canvas.delete(can53)
    ball+=1
    can54=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'She _____ a lot of her free time reading.')
    b1.config(text = 'does', command = funct88)
    b2.config(text = 'spends', command = funct89)
    b3.config(text = 'has', command = funct88)
    b4.config(text = 'makes', command = funct88)
def funct86():
    global can54
    canvas.delete(can53)
    can54=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'She _____ a lot of her free time reading.')
    b1.config(text = 'does', command = funct88)
    b2.config(text = 'spends', command = funct89)
    b3.config(text = 'has', command = funct88)
    b4.config(text = 'makes', command = funct88)
def funct85():
    global can53, ball
    canvas.delete(can52)
    ball+=1
    can53=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Paul will look _____ our dogs while we`re on holiday.')
    b1.config(text = 'at', command = funct86)
    b2.config(text = 'for', command = funct86)
    b3.config(text = 'into', command = funct86)
    b4.config(text = 'after', command = funct87)
def funct84():
    global can53
    canvas.delete(can52)
    can53=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Paul will look _____ our dogs while we`re on holiday.')
    b1.config(text = 'at', command = funct86)
    b2.config(text = 'for', command = funct86)
    b3.config(text = 'into', command = funct86)
    b4.config(text = 'after', command = funct87)
def funct83():
    global can52, ball
    canvas.delete(can51)
    ball+=1
    can52=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'It`s cold so you should _____ on a warm jacket.')
    b1.config(text = 'put', command = funct85)
    b2.config(text = 'wear', command = funct84)
    b3.config(text = 'dress', command = funct84)
    b4.config(text = 'take', command = funct84)
def funct82():
    global can52
    canvas.delete(can51)
    can52=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'It`s cold so you should _____ on a warm jacket.')
    b1.config(text = 'put', command = funct85)
    b2.config(text = 'wear', command = funct84)
    b3.config(text = 'dress', command = funct84)
    b4.config(text = 'take', command = funct84)
def funct81():
    global can51, ball
    canvas.delete(can50)
    ball+=1
    can51=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'You may not like the cold weather here,\nbut you`ll have to _____, I`m afraid.')
    b1.config(text = 'tell it off', command = funct82)
    b2.config(text = 'sort itself out', command = funct82)
    b3.config(text = 'put up with it', command = funct83)
    b4.config(text = 'put it off', command = funct82)
def funct80():
    global can51
    canvas.delete(can50)
    can51=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'You may not like the cold weather here,\nbut you`ll have to _____, I`m afraid.')
    b1.config(text = 'tell it off', command = funct82)
    b2.config(text = 'sort itself out', command = funct82)
    b3.config(text = 'put up with it', command = funct83)
    b4.config(text = 'put it off', command = funct82)
def funct79():
    global can50, ball
    canvas.delete(can49)
    ball+=1
    can50=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Was it Captain Cook _____ New Zealand?')
    b1.config(text = 'who discovered', command = funct81)
    b2.config(text = 'discovered', command = funct80)
    b3.config(text = 'that discover', command = funct80)
    b4.config(text = 'who was discovering', command = funct80)
def funct78():
    global can50
    canvas.delete(can49)
    can50=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Was it Captain Cook _____ New Zealand?')
    b1.config(text = 'who discovered', command = funct81)
    b2.config(text = 'discovered', command = funct80)
    b3.config(text = 'that discover', command = funct80)
    b4.config(text = 'who was discovering', command = funct80)
def funct77():
    global can49, ball
    canvas.delete(can48)
    ball+=1
    can49=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I don`t remember mentioning\n _____ dinner together tonight.')
    b1.config(text = 'go for', command = funct78)
    b2.config(text = 'you going to', command = funct78)
    b3.config(text = 'to go for', command = funct78)
    b4.config(text = 'going for', command = funct79)
def funct76():
    global can49
    canvas.delete(can48)
    can49=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I don`t remember mentioning\n _____ dinner together tonight.')
    b1.config(text = 'go for', command = funct78)
    b2.config(text = 'you going to', command = funct78)
    b3.config(text = 'to go for', command = funct78)
    b4.config(text = 'going for', command = funct79)
def funct75():
    global can48, ball
    canvas.delete(can47)
    ball+=1
    can48=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Do you think you _____ with my mobile phone soon?\nI need to make a call.')
    b1.config(text = 'finish', command = funct76)
    b2.config(text = 'are finishing', command = funct76)
    b3.config(text = 'will have finished', command = funct77)
    b4.config(text = 'are finished', command = funct76)
def funct74():
    global can48
    canvas.delete(can47)
    can48=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Do you think you _____ with my mobile phone soon?\nI need to make a call.')
    b1.config(text = 'finish', command = funct76)
    b2.config(text = 'are finishing', command = funct76)
    b3.config(text = 'will have finished', command = funct77)
    b4.config(text = 'are finished', command = funct76)
def funct73():
    global can47, ball
    canvas.delete(can46)
    ball+=1
    can47=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'If I hadn`t replied to your email,\n I _____ here with you now.')   #47-ой вопрос
    b1.config(text = 'can`t be', command = funct74)
    b2.config(text = 'wouldn`t be', command = funct75)
    b3.config(text = 'won`t be', command = funct74)
    b4.config(text = 'haven`t been', command = funct74)
def funct72():
    global can47
    canvas.delete(can46)
    can47=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'If I hadn`t replied to your email,\n I _____ here with you now.')   #47-ой вопрос
    b1.config(text = 'can`t be', command = funct74)
    b2.config(text = 'wouldn`t be', command = funct75)
    b3.config(text = 'won`t be', command = funct74)
    b4.config(text = 'haven`t been', command = funct74)
def funct71():
    global can46, ball
    canvas.delete(can45)
    ball+=1
    can46=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'We won`t catch the plane _____ we leave home now!\nPlease hurry up!')
    b1.config(text = 'if', command = funct72)
    b2.config(text = 'providing that', command = funct72)
    b3.config(text = 'except', command = funct72)
    b4.config(text = 'unless', command = funct73)
def funct70():
    global can46
    canvas.delete(can45)
    can46=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'We won`t catch the plane _____ we leave home now!\nPlease hurry up!')
    b1.config(text = 'if', command = funct72)
    b2.config(text = 'providing that', command = funct72)
    b3.config(text = 'except', command = funct72)
    b4.config(text = 'unless', command = funct73)
def funct69():
    global can45, ball
    canvas.delete(can44)
    ball+=1
    can45=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'She _____ for her pet for two days when she finally\n found it in the garage.')
    b1.config(text = 'looked', command = funct70)
    b2.config(text = 'had been looked', command = funct70)
    b3.config(text = 'had been looking', command = funct71)
    b4.config(text = 'were looking', command = funct70)
def funct68():
    global can45
    canvas.delete(can44)
    can45=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'She _____ for her pet for two days when she finally\n found it in the garage.')
    b1.config(text = 'looked', command = funct70)
    b2.config(text = 'had been looked', command = funct70)
    b3.config(text = 'had been looking', command = funct71)
    b4.config(text = 'were looking', command = funct70)
def funct67():
    global can44, ball
    canvas.delete(can43)
    ball+=1
    can44=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'What I like more than anything else _____ at weekends.')
    b1.config(text = 'playing golf', command = funct68)
    b2.config(text = 'to play golf', command = funct68)
    b3.config(text = 'is playing golf', command = funct69)
    b4.config(text = 'is play golf', command = funct68)
def funct66():
    global can44
    canvas.delete(can43)
    can44=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'What I like more than anything else _____ at weekends.')
    b1.config(text = 'playing golf', command = funct68)
    b2.config(text = 'to play golf', command = funct68)
    b3.config(text = 'is playing golf', command = funct69)
    b4.config(text = 'is play golf', command = funct68)
def funct65():
    global can43, ball
    canvas.delete(can42)
    ball+=1
    can43=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ this great book and I can`t wait to see how it ends.')
    b1.config(text = 'I don`t read', command = funct66)
    b2.config(text = 'I`ve read', command = funct66)
    b3.config(text = 'I`ve been reading', command = funct67)
    b4.config(text = 'I read', command = funct66)
def funct64():
    global can43
    canvas.delete(can42)
    can43=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ this great book and I can`t wait to see how it ends.')
    b1.config(text = 'I don`t read', command = funct66)
    b2.config(text = 'I`ve read', command = funct66)
    b3.config(text = 'I`ve been reading', command = funct67)
    b4.config(text = 'I read', command = funct66)
def funct63():
    global can42, ball
    canvas.delete(can41)
    ball+=1
    can42=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Take a warm coat, _____ you might get very cold outside')
    b1.config(text = 'otherwise', command = funct65)
    b2.config(text = 'in case', command = funct64)
    b3.config(text = 'so that', command = funct64)
    b4.config(text = 'in order to', command = funct64)
def funct62():
    global can42
    canvas.delete(can41)
    can42=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Take a warm coat, _____ you might get very cold outside')
    b1.config(text = 'otherwise', command = funct65)
    b2.config(text = 'in case', command = funct64)
    b3.config(text = 'so that', command = funct64)
    b4.config(text = 'in order to', command = funct64)
def funct61():
    global can41, ball
    canvas.delete(can40)
    ball+=1
    can41=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I wasn`t interested in the perfomance very much.\n_____.')
    b1.config(text = 'I didn`t, too', command = funct62)
    b2.config(text = 'Neither was I', command = funct62)
    b3.config(text = 'Nor I did', command = funct63)
    b4.config(text = 'So I wasn`t', command = funct62)
def funct60():
    global can41
    canvas.delete(can40)
    can41=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I wasn`t interested in the perfomance very much.\n_____.')
    b1.config(text = 'I didn`t, too', command = funct62)
    b2.config(text = 'Neither was I', command = funct63)
    b3.config(text = 'Nor I did', command = funct62)
    b4.config(text = 'So I wasn`t', command = funct62)
def funct59():
    global can40, ball
    canvas.delete(can39)
    ball+=1
    can40=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'They _____ to the restaurant before.')
    b1.config(text = 'was never', command = funct60)
    b2.config(text = 'have never been', command = funct61)
    b3.config(text = 'has never been', command = funct60)
    b4.config(text = 'were never been', command = funct60)
def funct58():
    global can40
    canvas.delete(can39)
    can40=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'They _____ to the restaurant before.')
    b1.config(text = 'was never', command = funct60)
    b2.config(text = 'have never been', command = funct61)
    b3.config(text = 'has never been', command = funct60)
    b4.config(text = 'were never been', command = funct60)
def funct57():
    global can39, ball
    canvas.delete(can38)
    ball+=1
    can39=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'She _____ visit the zoo last summer.')
    b1.config(text = 'have not', command = funct58)
    b2.config(text = 'didn’t', command = funct59)
    b3.config(text = 'can', command = funct58)
    b4.config(text = 'wasn’t', command = funct58)
def funct56():
    global can39
    canvas.delete(can38)
    can39=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'She _____ visit the zoo last summer.')
    b1.config(text = 'have not', command = funct58)
    b2.config(text = 'didn’t', command = funct59)
    b3.config(text = 'can', command = funct58)
    b4.config(text = 'wasn’t', command = funct58)
def funct55():
    global can38, ball
    canvas.delete(can37)
    ball+=1
    can38=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Can you speak _____, please!')
    b1.config(text = 'louder', command = funct57)
    b2.config(text = 'fast', command = funct56)
    b3.config(text = 'clever', command = funct56)
    b4.config(text = 'ugly', command = funct56)
def funct54():
    global can38
    canvas.delete(can37)
    can38=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Can you speak _____, please!')
    b1.config(text = 'louder', command = funct57)
    b2.config(text = 'fast', command = funct56)
    b3.config(text = 'clever', command = funct56)
    b4.config(text = 'ugly', command = funct56)
def funct53():
    global can37, ball
    canvas.delete(can36)
    ball+=1
    can37=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'She _____ in 1983.')
    b1.config(text = 'borned', command = funct54)
    b2.config(text = 'was born', command = funct55)
    b3.config(text = 'is born', command = funct54)
    b4.config(text = 'be born', command = funct54)
def funct52():
    global can37
    canvas.delete(can36)
    can37=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'She _____ in 1983.')
    b1.config(text = 'borned', command = funct54)
    b2.config(text = 'was born', command = funct55)
    b3.config(text = 'is born', command = funct54)
    b4.config(text = 'be born', command = funct54)
def funct51():
    global can36, ball
    canvas.delete(can35)
    ball+=1
    can36=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I _____ and can’t go to the disco.')
    b1.config(text = 'tired', command = funct52)
    b2.config(text = 'am tired', command = funct53)
    b3.config(text = 'is tired', command = funct52)
    b4.config(text = 'was tired', command = funct52)
def funct50():
    global can36
    canvas.delete(can35)
    can36=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I _____ and can’t go to the disco.')
    b1.config(text = 'tired', command = funct52)
    b2.config(text = 'am tired', command = funct53)
    b3.config(text = 'is tired', command = funct52)
    b4.config(text = 'was tired', command = funct52)
def funct49():
    global can35, ball
    canvas.delete(can34)
    ball+=1
    can35=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'We have only _____ flowers in the garden this year.')
    b1.config(text = 'much', command = funct50)
    b2.config(text = 'a few', command = funct51)
    b3.config(text = 'a little', command = funct50)
    b4.config(text = 'many', command = funct50)
def funct48():
    global can35
    canvas.delete(can34)
    can35=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'We have only _____ flowers in the garden this year.')
    b1.config(text = 'much', command = funct50)
    b2.config(text = 'a few', command = funct51)
    b3.config(text = 'a little', command = funct50)
    b4.config(text = 'many', command = funct50)
def funct47():
    global can34, ball
    canvas.delete(can33)
    ball+=1
    can34=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'He was in Moscow two years _____')
    b1.config(text = 'after', command = funct48)
    b2.config(text = 'before', command = funct48)
    b3.config(text = 'since', command = funct48)
    b4.config(text = 'ago', command = funct49)
def funct46():
    global can34
    canvas.delete(can33)
    can34=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'He was in Moscow two years _____')
    b1.config(text = 'after', command = funct48)
    b2.config(text = 'before', command = funct48)
    b3.config(text = 'since', command = funct48)
    b4.config(text = 'ago', command = funct49)
def funct45():
    global can33, ball
    canvas.delete(can32)
    ball+=1
    can33=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Her dress is _____ small.')
    b1.config(text = 'too', command = funct47)
    b2.config(text = 'enough', command = funct46)
    b3.config(text = 'a lot of', command = funct46)
    b4.config(text = 'much', command = funct46)
def funct44():
    global can33
    canvas.delete(can32)
    can33=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Her dress is _____ small.')
    b1.config(text = 'too', command = funct47)
    b2.config(text = 'enough', command = funct46)
    b3.config(text = 'a lot of', command = funct46)
    b4.config(text = 'much', command = funct46)
def funct43():
    global can32, ball
    canvas.delete(can31)
    ball+=1
    can32=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ I come in?')
    b1.config(text = 'Must', command = funct44)
    b2.config(text = 'May', command = funct45)
    b3.config(text = 'Can', command = funct44)
    b4.config(text = 'Have', command = funct44)
def funct42():
    global can32
    canvas.delete(can31)
    can32=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ I come in?')
    b1.config(text = 'Must', command = funct44)
    b2.config(text = 'May', command = funct45)
    b3.config(text = 'Can', command = funct44)
    b4.config(text = 'Have', command = funct44)
def funct41():
    global can31, ball
    canvas.delete(can30)
    ball+=1
    can31=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'You _____ to swim here.')
    b1.config(text = 'are not allowed', command = funct43)
    b2.config(text = 'don’t have', command = funct42)
    b3.config(text = 'can’t be', command = funct42)
    b4.config(text = 'could not', command = funct42)
def funct40():
    global can31
    canvas.delete(can30)
    can31=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'You _____ to swim here.')
    b1.config(text = 'are not allowed', command = funct43)
    b2.config(text = 'don’t have', command = funct42)
    b3.config(text = 'can’t be', command = funct42)
    b4.config(text = 'could not', command = funct42)
def funct39():
    global can30, ball
    canvas.delete(can29)
    ball+=1
    can30=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'He knows _____ she is crying.')
    b1.config(text = 'why', command = funct41)
    b2.config(text = 'which', command = funct40)
    b3.config(text = 'how', command = funct40)
    b4.config(text = 'who', command = funct40)
def funct38():
    global can30
    canvas.delete(can29)
    can30=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'He knows _____ she is crying.')
    b1.config(text = 'why', command = funct41)
    b2.config(text = 'which', command = funct40)
    b3.config(text = 'how', command = funct40)
    b4.config(text = 'who', command = funct40)
def funct37():
    global can29, ball
    canvas.delete(can28)
    ball+=1
    can29=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I’ve _____ been to Paris.')
    b1.config(text = 'ever', command = funct38)
    b2.config(text = 'since', command = funct38)
    b3.config(text = 'for', command = funct38)
    b4.config(text = 'never', command = funct39)
def funct36():
    global can29
    canvas.delete(can28)
    can29=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'I’ve _____ been to Paris.')
    b1.config(text = 'ever', command = funct38)
    b2.config(text = 'since', command = funct38)
    b3.config(text = 'for', command = funct38)
    b4.config(text = 'never', command = funct39)
def funct35():
    global can28, ball
    canvas.delete(can27)
    ball+=1
    can28=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Peter was too _____ to ask her phone number.')
    b1.config(text = 'shy', command = funct37)
    b2.config(text = 'worried', command = funct36)
    b3.config(text = 'selfish', command = funct36)
    b4.config(text = 'polite', command = funct36)
def funct34():
    global can28
    canvas.delete(can27)
    can28=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Peter was too _____ to ask her phone number.')
    b1.config(text = 'shy', command = funct37)
    b2.config(text = 'worried', command = funct36)
    b3.config(text = 'selfish', command = funct36)
    b4.config(text = 'polite', command = funct36)
def funct33():
    global can27, ball
    canvas.delete(can26)
    ball+=1
    can27=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'My clothes need _____')
    b1.config(text = 'to wash', command = funct34)
    b2.config(text = 'washing', command = funct35)
    b3.config(text = 'to be wash', command = funct34)
    b4.config(text = 'wash', command = funct34)
def funct32():
    global can27
    canvas.delete(can26)
    can27=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'My clothes need _____')
    b1.config(text='to wash', command = funct34)
    b2.config(text='washing', command = funct35)
    b3.config(text = 'to be wash', command = funct34)
    b4.config(text = 'wash', command = funct34)
def funct31():
    global can26, ball
    canvas.delete(can25)
    ball+=1
    can26=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Are you good _____?')
    b1.config(text='at', command = funct33)
    b2.config(text='with', command = funct32)
    b3.config(text = 'on', command = funct32)
    b4.config(text = 'of', command = funct32)
def funct30():
    global can26
    canvas.delete(can25)
    can26=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Are you good _____?')
    b1.config(text='at', command = funct33)
    b2.config(text='with', command = funct32)
    b3.config(text = 'on', command = funct32)
    b4.config(text = 'of', command = funct32)
def funct29():
    global can25, ball
    canvas.delete(can24)
    ball+=1
    can25=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'This park looks very _____')
    b1.config(text='hungry', command = funct30)
    b2.config(text='ill', command = funct30)
    b3.config(text = 'beautiful', command = funct31)
    b4.config(text = 'round', command = funct30)
def funct28():
    global can25
    canvas.delete(can24)
    can25=canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'This park looks very _____')
    b1.config(text='hungry', command = funct30)
    b2.config(text='ill', command = funct30)
    b3.config(text = 'beautiful', command = funct31)
    b4.config(text = 'round', command = funct30)
def funct27():
    global can24, ball
    canvas.delete(can23)
    ball+=1
    can24 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ children like cartoons.')
    b1.config(text='Much',command = funct28)
    b2.config(text='Many',command = funct29)
    b3.config(text = 'A lots of',command = funct28)
    b4.config(text = 'Many of',command = funct28)
def funct26():
    global can24
    canvas.delete(can23)
    can24 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ children like cartoons.')
    b1.config(text='Much',command = funct28)
    b2.config(text='Many',command = funct29)
    b3.config(text = 'A lots of',command = funct28)
    b4.config(text = 'Many of',command = funct28)
def funct25():
    global can23, ball
    canvas.delete(can22)
    ball+=1
    can23 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'They _____ writing a letter.')
    b1.config(text='is', command = funct26)
    b2.config(text='do', command = funct26)
    b3.config(text = 'are', command = funct27)
    b4.config(text = 'can', command = funct26)
def funct24():
    global can23
    canvas.delete(can22)
    can23 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'They _____ writing a letter.')
    b1.config(text='is', command = funct26)
    b2.config(text='do', command = funct26)
    b3.config(text = 'are', command = funct27)
    b4.config(text = 'can', command = funct26)
def funct23():
    global can22, ball
    canvas.delete(can21)
    ball+=1
    can22 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Can you show me the _____ to the post office?')
    b1.config(text='way', command = funct25)
    b2.config(text='road', command = funct24)
    b3.config(text = 'direction', command = funct24)
    b4.config(text = 'trip', command = funct24)
def funct22():
    global can22
    canvas.delete(can21)
    can22 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Can you show me the _____ to the post office?')
    b1.config(text='way', command = funct25)
    b2.config(text='road', command = funct24)
    b3.config(text = 'direction', command = funct24)
    b4.config(text = 'trip', command = funct24)
def funct21():
    global can21, ball
    canvas.delete(can20)
    ball+=1
    can21 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'She’s got _____ bread.')
    b1.config(text='any', command = funct22)
    b2.config(text='some', command = funct23)
    b3.config(text = 'someone', command = funct22)
    b4.config(text = 'never', command = funct22)
def funct20():
    global can21
    canvas.delete(can20)
    can21 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'She’s got _____ bread.')
    b1.config(text='any', command = funct22)
    b2.config(text='some', command = funct23)
    b3.config(text = 'someone', command = funct22)
    b4.config(text = 'never', command = funct22)
def funct19():
    global can20, ball
    canvas.delete(can19)
    ball+=1
    can20 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Have you eaten _____?')
    b1.config(text='yet', command = funct21)
    b2.config(text='already', command = funct20)
    b3.config(text = 'ever', command = funct20)
    b4.config(text = 'just', command = funct20)
def funct18():
    global can20
    canvas.delete(can19)
    can20 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Have you eaten _____?')
    b1.config(text='yet', command = funct21)
    b2.config(text='already', command = funct20)
    b3.config(text = 'ever', command = funct20)
    b4.config(text = 'just', command = funct20)
def funct17():
    global can19, ball
    canvas.delete(can18)
    ball+=1
    can19 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ she like fish?')
    b1.config(text='Do', command = funct18)
    b2.config(text='Dos', command = funct18)
    b3.config(text = 'Is', command = funct18)
    b4.config(text = 'Does', command = funct19)
def funct16():
    global can19
    canvas.delete(can18)
    can19 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ she like fish?')
    b1.config(text='Do', command = funct18)
    b2.config(text='Dos', command = funct18)
    b3.config(text = 'Is', command = funct18)
    b4.config(text = 'Does', command = funct19)
def funct15():
    global can18, ball
    canvas.delete(can17)
    ball+=1
    can18 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'He’s going to the cafe. He’s _____')
    b1.config(text='hungry', command = funct17)
    b2.config(text='lazy', command = funct16)
    b3.config(text = 'tired', command = funct16)
    b4.config(text = 'ugly', command = funct16)
def funct14():
    global can18
    canvas.delete(can17)
    can18 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'He’s going to the cafe. He’s_____')
    b1.config(text='hungry', command = funct17)
    b2.config(text='lazy', command = funct16)
    b3.config(text = 'tired', command = funct16)
    b4.config(text = 'ugly', command = funct16)
def funct13():
    global can17, ball
    canvas.delete(can16)
    ball+=1
    can17 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'She _____ swimming.')
    b1.config(text='go', command = funct14)
    b2.config(text='gos', command = funct14)
    b3.config(text = 'goes', command = funct15)
    b4.config(text = 'going', command = funct14)
def funct12():
    global can17
    canvas.delete(can16)
    can17 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'She _____ swimming.')
    b1.config(text='go', command = funct14)
    b2.config(text='gos', command = funct14)
    b3.config(text = 'goes', command = funct15)
    b4.config(text = 'going', command = funct14)
def funct11():
    global can16, ball
    canvas.delete(can15)
    ball+=1
    can16 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'The sofa is _____ the table and the armchair.')
    b1.config(text='between', height= 2, command = funct13)
    b2.config(text='on', height= 2, command = funct12)
    b3.config(text = 'in', height= 2, command = funct12)
    b4.config(text = 'under', height= 2, command = funct12)
def funct10():
    global can16
    canvas.delete(can15)
    can16 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'The sofa is _____ the table and the armchair.')
    b1.config(text='between', height= 2, command = funct13)
    b2.config(text='on', height= 2, command = funct12)
    b3.config(text = 'in', height= 2, command = funct12)
    b4.config(text = 'under', height= 2, command = funct12)
def funct9():
    global can15, ball
    canvas.delete(can14)
    ball+=1
    can15 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Can you help me?')
    b1.config(text='Yes, sure!', height= 3, command = funct11)
    b2.config(text='No, I can’t dance!', height= 3, command = funct10)
    b3.config(text = 'Yes, I helped\n him yesterday.', height= 3, command = funct10)
    b4.config(text = 'No, I couldn’t swim\n when I was five.', height= 3, command = funct10)
def funct8():
    global can15
    canvas.delete(can14)
    can15 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Can you help me?')
    b1.config(text='Yes, sure!', height= 3, command = funct11)
    b2.config(text='No, I can’t dance!', height= 3, command = funct10)
    b3.config(text = 'Yes, I helped\n him yesterday.', height= 3, command = funct10)
    b4.config(text = 'No, I couldn’t swim\n when I was five.', height= 3, command = funct10)
def funct7():
    global can14, ball
    canvas.delete(can13)
    ball+=1
    can14 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'What’s the weather like today?')
    b1.config(text='It’s winter.', command = funct8)
    b2.config(text='He’s ill.', command = funct8)
    b3.config(text = 'It’s cold.', command = funct9)
    b4.config(text = 'She’s pretty.', command = funct8)
def funct6():
    global can14
    canvas.delete(can13)
    can14 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'What’s the weather like today?')
    b1.config(text='It’s winter.', command = funct8)
    b2.config(text='He’s ill.', command = funct8)
    b3.config(text = 'It’s cold.', command = funct9)
    b4.config(text = 'She’s pretty.', command = funct8)
def funct5():
    global can13, ball
    canvas.delete(can12)
    ball+=1 
    can13 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'What are you doing?')
    b1.config(text='I’m working.', command = funct7)
    b2.config(text='She’s reading.', command = funct6)
    b3.config(text = 'We don’t work.', command = funct6)
    b4.config(text = 'They are at home.', command = funct6)
def funct4():
    global can13
    canvas.delete(can12)
    can13 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'What are you doing?')
    b1.config(text='I’m working.', command = funct7)
    b2.config(text='She’s reading.', command = funct6)
    b3.config(text = 'We don’t work.', command = funct6)
    b4.config(text = 'They are at home.', command = funct6)
def funct3():
    global can12, ball
    canvas.delete(can11)
    ball+=1
    can12 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Where are you from?')
    b1.config(text='I’m fine, thank you!', command = funct4)
    b2.config(text='I go to school.', command = funct4)
    b3.config(text = 'I’m from Italy.', command = funct5)
    b4.config(text = 'He’s from Japan.', command = funct4)
def funct2():
    global can12
    canvas.delete(can11)
    can12 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Where are you from?')
    b1.config(text='I’m fine, thank you!', command = funct4)
    b2.config(text='I go to school.', command = funct4)
    b3.config(text = 'I’m from Italy.', command = funct5)
    b4.config(text = 'He’s from Japan.', command = funct4)
def funct1():
    global can11
    canvas.delete(can10)
    can11 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'How are you?')
    b1.config(text='I’m ten years old.', command=funct2)
    b2.config(text='I’m fine.', command=funct3)
    b3.config(text = 'We’re British.', command = funct2)
    b4.config(text = 'My name’s Tom.', command = funct2)
def func21():
    global can11, ball
    canvas.delete(can10)
    ball+=1
    can11 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'How are you?')
    b1.config(text='I’m ten years old.', command=funct2)
    b2.config(text='I’m fine.', command=funct3)
    b3.config(text = 'We’re British.', command = funct2)
    b4.config(text = 'My name’s Tom.', command = funct2)
def func11():
    global can10, ball
    canvas.delete(can9)
    ball+=1
    can10 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ you have a car?')
    b1.config(text='Are', command=funct1)
    b2.config(text='Do', command=func21)
    b3.config(text = 'Is', command = funct1)
    b4.config(text = 'Does', command = funct1)
def func20():
    global can10
    canvas.delete(can9)
    can10 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ you have a car?')
    b1.config(text='Are', command=funct1)
    b2.config(text='Do', command=func21)
    b3.config(text = 'Is', command = funct1)
    b4.config(text = 'Does', command = funct1)
def func10():
    global can9, ball
    canvas.delete(can8)
    ball+=1
    can9 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ he play tennis?')
    b3.config(text='Does', command=func11)
    b4.config(text='Do', command=func20)
    b1.config(text = 'Is', command = func20)
    b2.config(text = 'Did', command = func20)
def func19():
    global can9
    canvas.delete(can8)
    can9 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ he play tennis?')
    b3.config(text='Does', command=func11)
    b4.config(text='Do', command=func20)
    b1.config(text = 'Is', command = func20)
    b2.config(text = 'Did', command = func20)
def func9():
    global can8, ball
    canvas.delete(can7)
    ball+=1
    can8 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Wednesday, Thursday, Friday, _____')
    b1.config(text='Monday', command=func19)
    b4.config(text='Saturday', command=func10)
    b3.config(text = 'Sunday', command = func19)
    b2.config(text = 'Tuesday', command = func19)
def func18():
    global can8
    canvas.delete(can7)
    can8 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Wednesday, Thursday, Friday, _____')
    b1.config(text='Monday', command=func19)
    b4.config(text='Saturday', command=func10)
    b3.config(text = 'Sunday', command = func19)
    b2.config(text = 'Tuesday', command = func19)
def func8():
    global can7, ball
    canvas.delete(can6)
    ball+=1
    can7 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'We _____ living in a flat.')
    b2.config(text='are', command=func9)
    b4.config(text='is', command=func18)
    b3.config(text = 'Was', command = func18)
    b1.config(text = 'Were', command = func18)
def func17():
    global can7
    canvas.delete(can6)
    can7 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'We _____ living in a flat.')
    b2.config(text='Are', command=func9)
    b4.config(text='Is', command=func18)
    b3.config(text = 'Was', command = func18)
    b1.config(text = 'Were', command = func18)
def func7():
    global can6, ball
    canvas.delete(can5)
    ball+=1
    can6 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ you like this DVD?')
    b1.config(text='Do', command=func8)
    b4.config(text='Are', command=func17)
    b3.config(text = 'Is', command = func17)
    b2.config(text = 'Does', command = func17)
def func16():
    global can6
    canvas.delete(can5)
    can6 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ you like this DVD?')
    b1.config(text='Do', command=func8)
    b4.config(text='Are', command=func17)
    b3.config(text = 'Is', command = func17)
    b2.config(text = 'Does', command = func17)
def func6():
    global can5, ball
    canvas.delete(can4)
    ball+=1
    can5 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Peter _____ at seven o’clock every day.')
    b1.config(text='get up', command=func16)
    b4.config(text='gets up', command=func7)
    b3.config(text = 'got up', command = func16)
    b2.config(text = 'will get up', command = func16)
def func15():
    global can5
    canvas.delete(can4)
    can5 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'Peter _____ at seven o’clock every day.')
    b1.config(text='get up', command=func16)
    b4.config(text='gets up', command=func7)
    b3.config(text = 'got up', command = func16)
    b2.config(text = 'will get up', command = func16)
def func5():
    global can4, ball
    canvas.delete(can3)
    ball+=1
    can4 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'What do you do? I’m _____ student.')
    b1.config(text='The', command=func15)
    b3.config(text='A', command=func6)
    b4.config(text = '-', command = func15)
    b2.config(text = 'Is', command = func15)
def func14():
    global can4
    canvas.delete(can3)
    can4 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'What do you do? I’m _____ student.')
    b1.config(text='The', command=func15)
    b3.config(text='A', command=func6)
    b4.config(text = '-', command = func15)
    b2.config(text = 'Is', command = func15)
def func4():
    global can3, ball
    canvas.delete(can2)
    ball+=1
    can3 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ are you from?')
    b1.config(text='What',command =func14)
    b4.config(text='Where',command =func5)
    b3.config(text = 'Who', command = func14)
    b2.config(text = 'Why', command = func14)
def func13():
    global can3
    canvas.delete(can2)
    can3 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = '_____ are you from?')
    b1.config(text = 'What', command = func14)
    b4.config(text = 'Where', command = func5)
    b3.config(text = 'Who', command = func14)
    b2.config(text = 'Why', command = func14)    
def func3():
    global can2, ball
    canvas.delete(can1)
    ball+=1
    can2 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'They _____ from Spain.')
    b3.config(text = 'Are', command = func4)
    b1.config(text = 'Is', command = func13)
    b4.config(text = 'Was', command = func13)
    b2.config(text = 'Were', command = func13)
def func2():
    global can2
    canvas.delete(can1)
    can2 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text = 'They _____ from Spain.')
    b1.config(text = 'Was', command = func13)
    b2.config(text = 'Is', command = func13)
    b4.config(text = 'Were', command = func13)
    b3.config(text = 'Are', command = func4)
def func1():
    global can1
    canvas.delete(can0)
    can1 = canvas.create_text(650, 85, font=('Helvetica',35, 'bold'), text='_____ name is Robert.')
    b1.place(relx=0.625, rely=0.25, anchor = 'center')
    b1.config(text = 'My', command=func3, width =16)
    b4.place(relx=0.375, rely=0.25, anchor = 'center')
    b4.config(text='Mine', command= func2, width =16)
    b3.place(relx = 0.12, rely = 0.25, anchor = 'center')
    b3.config(text='I', command = func2, width =16)
    b2.place(relx = 0.88, rely = 0.25, anchor = 'center')
    b2.config(text = 'Me', bg = 'green', activebackground = 'lime', command = func2, width = 16)


can0 = canvas.create_text(650, 85, text = 'Хотите узнать свой уровень\n      знания английского?', font=('Helvetica',35, 'bold'))
b1 = Button(text='ДА', height= 2, width = 10, fg = 'black', bg = 'green', activebackground= 'lime', command = func1, font=('Helvetica', 20, 'bold'))
b2 = Button(text='НЕТ', height= 2, width = 10, fg = 'black', bg = 'red', activebackground= 'orange', command = root.destroy, font=('Helvetica', 20, 'bold'))
b3 = Button(text='ДА', height= 2, width = 10, fg = 'black', bg = 'green', activebackground= 'lime', command = func1, font=('Helvetica', 20, 'bold'))
b4 = Button(text='ДА', height= 2, width = 10, fg = 'black', bg = 'green', activebackground= 'lime', command = func1, font=('Helvetica', 20, 'bold'))
root.resizable(False, False)


canvas.pack(anchor=CENTER, expand=50)
b1.place(relx = 0.7, rely = 0.25, anchor = 'center')
b2.place(relx = 0.3, rely = 0.25, anchor = 'center')
root.mainloop()