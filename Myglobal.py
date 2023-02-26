from configparser import ConfigParser
from MyLog import cTime
from Mypath import init

class cGlobal():
    def __init__(self):
        pass
    def Initailize_System(self):
        config = ConfigParser()
        config['System'] = {}
        config['System']['Host'] = '127.0.0.1'
        config['System']['Port'] = '8080'
        config['System']['Fontsizes'] = '6'
        config['System']['Resizes'] = '1'
        with open('System.ini', 'w') as configfile:
            config.write(configfile)
    
    def Set_HostPort(self,host,port):
        config = ConfigParser()
        config['System'] = {}
        config['System']['Host'] = host
        config['System']['Port'] = port
        with open('System.ini', 'w') as configfile:
            config.write(configfile)
    
###
    def get_HostPort(self):
        try:
            config = ConfigParser()
            config.read('System.ini',encoding='utf-8')
            config.sections()
            h = config['System']['Host']
            p = config['System']['Port']
            return h,p
        except:
            cTime(Mode='Log_Write',
                              Sector='Myglobal.cGlobal.get_HostPort',
                              Contents ='Get Failed HostPort. Initail system resourse',
                              SavePath=init())
            cGlobal.Initailize_System(self)
            cGlobal.get_HostPort(self)
        

    def get_Fontsizes(self):
        try:
            config = ConfigParser()
            config.read('System.ini',encoding='utf-8')
            config.sections()
            f = config['System']['Fontsizes']
            return int(f)
        except:
            cTime(Mode='Log_Write',
                              Sector='Myglobal.cGlobal.get_Fontsizes',
                              Contents ='Get Failed Fontsizes. Initail system resourse',
                              SavePath=init())
            cGlobal.Initailize_System(self)
            cGlobal.get_HostPort(self)
        

    def get_Resizes(self):
        try:
            config = ConfigParser()
            config.read('System.ini',encoding='utf-8')
            config.sections()
            r = config['System']['Resizes']
            return float(r)
        except:
            cTime(Mode='Log_Write',
                              Sector='Myglobal.cGlobal.get_Resizes',
                              Contents ='Get Failed Resizes. Initail system resourse',
                              SavePath=init())
            cGlobal.Initailize_System(self)
            cGlobal.get_HostPort(self)
        
    
if __name__=='__main__':
    
    cGlobal()
