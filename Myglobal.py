from configparser import ConfigParser
from MyLog import cTime
from Mypath import init
import pendant

class cGlobal():
    def __init__(self):
        pass
    def Initailize_System(self):
        config = ConfigParser()
        config['System'] = {}
        config['System']['host'] = '127.0.0.1'
        config['System']['port'] = '8080'
        config['System']['fontsizes'] = '5'
        config['System']['resizes'] = '1'
        with open('System.ini', 'w') as configfile:
            config.write(configfile)
    
    def Set_HostPort(self,host,port):
        config = ConfigParser()
        config['System'] = {}
        config['System']['host'] = host
        config['System']['port'] = port
        config['System']['fontsizes'] = str(cGlobal.get_Fontsizes(self))
        config['System']['resizes'] = str(cGlobal.get_Resizes(self))
        with open('System.ini', 'w') as configfile:
            config.write(configfile)
            
    def Set_SafetyZone(self,x,y,z):
        config = ConfigParser()
        config['System'] = {}
        config['System']['host'] = str(cGlobal.get_HostPort(self)[0])
        config['System']['port'] = str(cGlobal.get_HostPort(self)[1])
        config['System']['fontsizes'] = str(cGlobal.get_Fontsizes(self))
        config['System']['resizes'] = str(cGlobal.get_Resizes(self))
        with open('System.ini', 'w') as configfile:
            config.write(configfile)
    
###
    def get_HostPort(self):
        try:
            config = ConfigParser()
            config.read('System.ini',encoding='utf-8')
            config.sections()
            h = config['System']['host']
            p = config['System']['port']
            return h,p
        except:
            cTime.Log_Write(self,'Get Failed HostPort. Initail system resourse')
            cGlobal.Initailize_System(self)
            cGlobal.get_HostPort(self)
        

    def get_Fontsizes(self):
        try:
            config = ConfigParser()
            config.read('System.ini',encoding='utf-8')
            config.sections()
            f = config['System']['fontsizes']
            return int(f)
        except:
            cTime.Log_Write(self,'Get Failed Fontsizes. Initail system resourse')
            cGlobal.Initailize_System(self)
            cGlobal.get_HostPort(self)
        

    def get_Resizes(self):
        try:
            config = ConfigParser()
            config.read('System.ini',encoding='utf-8')
            config.sections()
            r = config['System']['resizes']
            return float(r)
        except:
            cTime.Log_Write(self,'Get Failed Resizes. Initail system resourse')
            cGlobal.Initailize_System(self)
            cGlobal.get_HostPort(self)
        
    
if __name__=='__main__':
    app =  pendant.QtWidgets.QApplication(pendant.sys.argv)
    main = pendant.Main()
    main.show()
    pendant.sys.exit(app.exec_())