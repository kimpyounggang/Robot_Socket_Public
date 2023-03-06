import os
import glob

path = r'C:\\Users\\fgdr1\\Desktop\\HIT\\ECT\\CODE\\tags\\ECT\\ECT_vX\\mfc\\vtk9.2\\lib'

# 해당 경로의 모든 파일을 가져옵니다.
files = glob.glob(os.path.join(path, '*'))
res = ''
# 파일 이름을 출력합니다.
for file in files:
    res+=os.path.basename(file)+';'
    
print(res)