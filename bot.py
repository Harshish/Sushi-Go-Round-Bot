from pymouse import PyMouse
import time
import os
from PIL import ImageOps
import numpy as np
import pyscreenshot as ImageGrab

m = PyMouse()
PLAY =  (673,397)
CONTINUE =  (670, 575)
SKIP = (909, 636)
CONTINUE2 = (653, 562)
dir_path = os.path.join(os.getcwd(),'Snaps')

x_pad = 355
y_pad = 187

sushiTypes = {3652:'onigiri', 
              4125:'caliroll',
              3659:'gunkan',}

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

class Blank:
    seat_1 = 8119
    seat_2 = 5986
    seat_3 = 11598
    seat_4 = 10532
    seat_5 = 6782
    seat_6 = 9041

class Cord:
    f_shrimp = (390, 513)
    f_rice = (447, 517)
    f_nori = (391, 569)
    f_roe = (447, 567)
    f_salmon = (393, 626)
    f_unagi = (445, 624)

    phone = (939, 388)
    menu_toppings = (887, 453)

    t_shrimp = (847, 405) #127,127,127
    t_nori = (848, 460) #33 30 11
    t_roe = (929, 460) #127 61 0
    t_salmon = (850, 513) #127 71 47 
    t_unagi = (930, 405) #94 49 8
    t_exit = (952, 515) 
 
    menu_rice = (888, 474)
    buy_rice = (900, 465) #127 127 127
     
    delivery_norm = (844, 475) 

def buyFood(food):
    m.click(Cord.t_exit[0],Cord.t_exit[1])
    time.sleep(2)

    if food == "rice":
        m.click(Cord.menu_rice[0],Cord.menu_rice[1])
        time.sleep(1)
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (127,127,127) :
            print ("Rice is available")
            m.click(Cord.buy_rice[0],Cord.buy_rice[1])
            time.sleep(1)
            m.click(Cord.delivery_norm[0],Cord.delivery_norm[1])
            foodOnHand['rice'] += 10
        else:
            print ("Rice not available")
            m.click(Cord.t_exit[0],Cord.t_exit[1])
            time.sleep(1)
            buyFood(food)

    if food == "nori":
        m.click(Cord.menu_toppings[0],Cord.menu_toppings[1])
        time.sleep(1)
        s = screenGrab()
        if s.getpixel(Cord.t_nori) != (33,30,11) :
            print ("Nori is available")
            m.click(Cord.t_nori[0],Cord.t_nori[1])
            time.sleep(1)
            m.click(Cord.delivery_norm[0],Cord.delivery_norm[1])
            foodOnHand['nori'] += 10
        else:
            print ("Nori not available")
            m.click(Cord.t_exit[0],Cord.t_exit[1])
            time.sleep(1)
            buyFood(food)

    if food == "roe":
        m.click(Cord.menu_toppings[0],Cord.menu_toppings[1])
        time.sleep(1)
        s = screenGrab()
        if s.getpixel(Cord.t_roe) != (127,61,0) :
            print ("Roe is available")
            m.click(Cord.t_roe[0],Cord.t_roe[1])
            time.sleep(1)
            m.click(Cord.delivery_norm[0],Cord.delivery_norm[1])
            foodOnHand['roe'] += 10
        else:
            print ("Roe not available")
            m.click(Cord.t_exit[0],Cord.t_exit[1])
            time.sleep(1)
            buyFood(food)

    #m.click(Cord.t_shrimp[0],Cord.t_shrimp[1])
    #m.click(Cord.t_salmon[0],Cord.t_salmon[1])
    #m.click(Cord.t_unagi[0],Cord.t_unagi[1])
    #m.click(Cord.t_exit[0],Cord.t_exit[1])

def checkFood():
    for i,j in foodOnHand.items():
        if i=='nori' or i=='rice' or i=='roe':
            if j <=4 :
                print ("%s is low and needs to be replenished"%(i))
                buyFood(i)

def clear_tables():
    m.click(436, 388)
    m.click(534, 387)
    m.click(638, 390)
    m.click(729, 390)
    m.click(832, 391)
    m.click(939, 388)
    time.sleep(1)

def foldMat():
    m.click(Cord.f_rice[0] + 40,Cord.f_rice[1])
    time.sleep(.1)

def makeFood(food):
    if food == 'caliroll':
        print ('Making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        m.click(Cord.f_rice[0],Cord.f_rice[1])    
        time.sleep(.05)
        m.click(Cord.f_nori[0],Cord.f_nori[1])        
        time.sleep(.05)
        m.click(Cord.f_roe[0],Cord.f_roe[1])        
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
     
    elif food == 'onigiri':
        print ('Making a onigiri')
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        m.click(Cord.f_rice[0],Cord.f_rice[1])  
        time.sleep(.05)
        m.click(Cord.f_rice[0],Cord.f_rice[1])
        time.sleep(.05)
        m.click(Cord.f_nori[0],Cord.f_nori[1])
        time.sleep(.1)
        foldMat()
        time.sleep(.05)
        time.sleep(1.5)
 
    elif food == 'gunkan':
        print ('Making a gunkan')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        m.click(Cord.f_rice[0],Cord.f_rice[1])
        time.sleep(.05)
        m.click(Cord.f_nori[0],Cord.f_nori[1])
        time.sleep(.05)
        m.click(Cord.f_roe[0],Cord.f_roe[1])
        time.sleep(.05)
        m.click(Cord.f_roe[0],Cord.f_roe[1])
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
    
def startGame():
    m.click(PLAY[0],PLAY[1])
    time.sleep(1)
    m.click(CONTINUE[0],CONTINUE[1])
    time.sleep(1)
    m.click(SKIP[0],SKIP[1])
    time.sleep(1)
    m.click(CONTINUE2[0],CONTINUE2[1])

def screenGrab():
    #box = (x_pad + 1,y_pad + 1, x_pad + 640,y_pad + 480)
    im = ImageGrab.grab()
    return im

def grab():
    box = (x_pad + 1,y_pad + 1, x_pad + 640,y_pad + 480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = np.array(im.getcolors())
    a = a.sum()
    print (a)
    return im

def get_seat_one():
    box = (384,245,384+63,245+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = np.array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(dir_path + '/seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_two():
    box = (485,245,485+63,245+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = np.array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(dir_path + '/seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_three():
    box = (586,245,586+63,245+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = np.array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(dir_path + '/seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_four():
    box = (687,245,687+63,245+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = np.array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(dir_path + '/seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_five():
    box = (788,245,788+63,245+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = np.array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(dir_path + '/seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_six():
    box = (889,245,889+63,245+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = np.array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(dir_path + '/seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

def check_bubs():
     
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if s1 in sushiTypes:
            print ('table 1 is occupied and needs %s'%(sushiTypes[s1]))
            makeFood(sushiTypes[s1])
        else:
            print ('sushi not found!\n sushiType = %i' % (s1))
 
    else:
        print ('Table 1 unoccupied')
 
    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            print ('table 2 is occupied and needs %s' % (sushiTypes[s2]))
            makeFood(sushiTypes[s2])
        else:
            print ('sushi not found!\n sushiType = %i' % (s2))
 
    else:
        print ('Table 2 unoccupied')
 
    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            print ('table 3 is occupied and needs %s' % (sushiTypes[s3]))
            makeFood(sushiTypes[s3])
        else:
            print ('sushi not found!\n sushiType = %i' % (s3))
 
    else:
        print ('Table 3 unoccupied')
 
    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            print ('table 4 is occupied and needs %s' % (sushiTypes[s4]))
            makeFood(sushiTypes[s4])
        else:
            print ('sushi not found!\n sushiType = %i' % (s4))
 
    else:
        print ('Table 4 unoccupied')
 
    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            print ('table 5 is occupied and needs %s' % (sushiTypes[s5]))
            makeFood(sushiTypes[s5])
        else:
            print ('sushi not found!\n sushiType = %i' % (s5))
 
    else:
        print ('Table 5 unoccupied')
 
    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            print ('table 1 is occupied and needs %s' % (sushiTypes[s6]))
            makeFood(sushiTypes[s6])
        else:
            print ('sushi not found!\n sushiType = %i' % (s6))
 
    else:
        print ('Table 6 unoccupied')
 
    clear_tables()

if __name__ == '__main__':
    startGame()
    while True:
        check_bubs()
