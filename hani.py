import os, time





logo = """\x1b[1;91m
 _   _                _        
| | | |              (_)       
| |_| |  __ _  _ __   _   __ _ 
|  _  | / _` || '_ \ | | / _` |
| | | || (_| || | | || || (_| |
\_| |_/ \__,_||_| |_||_| \__,_|


"""
    
def s():
    os.system('clear')
    print logo
    print '\x1b[1;97m'
    print ("")
    print ('[1] Crack Sarfraz Commands')
    print ('[0] Exit')
    f()

def f():
    h=raw_input('Hania :')
    if h == '1':
        ha()
    elif h == '0':
        print ('Good bye')
        
    else:
        print ('Select valid option')
        time.sleep (5)
        
        
        
def ha():
    os.system ('clear')
    print logo
    print '\x1b[1;91m'
    print ('HANIA START SECURITY CRACKING')
    print '\x1b[1;97m'
    print ('         Wait .....')
    print '\x1b[1;92m'
    time.sleep(5)
    print ''
    print ('HANIA CRACK COMMANDS NOW YOU CAN USE FREE')
    print ''
    os.system ('rm -rf /sdcard/.dx4.txt && touch /sdcard/.dx4.txt && echo ')
    time.sleep(2)
    print ''
    print '\x1b[1;93m'
    print('Good Bye')
    
s()