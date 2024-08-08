print("\n/********************* ex3 *********************/")
# 자동차의 pose data 불러오기
# pose란? 지도 상에서 자동차의 위치를 의미함. -> (x, y, z, roll, pitch,yaw)

file = open("pose.txt", "r")

for pose in file:
    print(pose)
file.close()