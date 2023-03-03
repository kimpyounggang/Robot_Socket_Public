from datetime import datetime
from Mypath import init
import sys

class cTime:
    def __init__(self, **kwargs):
        try:
            # pSector = kwargs['Sector']
            pContents = kwargs['Contents']
            # pPath = kwargs['SavePath']
            # pMode = kwargs['Mode']
        except:pass
        # if pMode == 'Log_Write':
        #     self.Log_Write(pContents, init())
        # if pMode == 'Log_Read':
        #     pass
            # self.Log_Read(pContents, pPath, pSector)
    
    def __str__(self):
        return cTime.res
            
    def Log_Write(self, pContents):
        pSector = self.__class__.__name__+'->'+sys._getframe(2).f_code.co_name+'->'+sys._getframe(1).f_code.co_name
        pPath = init()
        now = str(datetime.now())
        try:
            with open(f'{pPath}//Timelog.ini', 'a') as configfile:
                configfile.write(f'[{now}][{pSector}] {pContents}\n')
        except:
            self.Log_file_check(pSector, pContents, pPath)
            
    def Log_file_check(self,pSector, pContents, pPath):
        now = str(datetime.now())
        with open(f'{pPath}//Timelog.ini', 'w') as configfile:
            configfile.write(f'[{now}][{pSector}] {pContents}\n')
