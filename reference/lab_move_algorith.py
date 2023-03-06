class Robot:
    def __init__(self):
        self.position = (0, 0, 0)  # 로봇의 위치 초기화
        self.total_distance = 0  # 로봇이 이동한 총 거리 초기화
        self.directions = [(0, 0, 1), (0, 0, -1), 
                           (0, 1, 0), (0, -1, 0), 
                           (1, 0, 0), (-1, 0, 0)]  # 로봇이 이동할 수 있는 방향들

    def move(self, dx, dy, dz):
        # 로봇의 이동 거리 누적
        self.total_distance += abs(dx) + abs(dy) + abs(dz)

        # 현재 위치에서 상대 위치를 더해 새 위치 계산
        new_x = self.position[0] + dx
        new_y = self.position[1] + dy
        new_z = self.position[2] + dz

        # 새 위치가 정육면체 안에 있는지 확인
        if abs(new_x) <= 15 and abs(new_y) <= 15 and abs(new_z) <= 15:
            self.position = (new_x, new_y, new_z)

    def move_to_coordinates(self, x, y, z):
        # 이동할 상대 위치 계산
        dx = x - self.total_distance - self.position[0]
        dy = y - self.total_distance - self.position[1]
        dz = z - self.total_distance - self.position[2]

        # 이동할 상대 위치로 로봇 이동
        self.move(dx, dy, dz)


robot = Robot()

for z in range(4):  # 높이 0~3까지
    for y in range(4):  # 세로 0~3까지
        for x in range(4):  # 가로 0~3까지
            # 주어진 좌표로 로봇 이동
            robot.move_to_coordinates(x, y, z)

