from datetime import datetime

class cTime:
    
    def __init__(self, **kwargs):
        try:
            pSector = kwargs['Sector']
            pContents = kwargs['Contents']
            pPath = kwargs['SavePath']
            pMode = kwargs['Mode']
        except:pass
        if pMode == 'Log_Write':
            self.Log_Write(pSector,pContents, pPath)
        if pMode == 'Log_Read':
            pass
            # self.Log_Read(pContents, pPath, pSector)
    
    def __str__(self):
        return cTime.res
            
    def Log_Write(self, pSector, pContents, pPath):
        now = str(datetime.now())
        try:
            with open(f'{pPath}\\Timelog.ini', 'a') as configfile:
                configfile.write(f'[{now}][{pSector}] {pContents}\n')
        except:
            self.Log_file_check(pSector, pContents, pPath)
            
    def Log_file_check(self,pSector, pContents, pPath):
        now = str(datetime.now())
        with open(f'{pPath}\\Timelog.ini', 'w') as configfile:
            configfile.write(f'[{now}][{pSector}] {pContents}\n')