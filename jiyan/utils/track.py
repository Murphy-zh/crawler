
track_list =  [[-37,-33,0],[0,0,0],[1,0,100],[6,0,114],[11,0,116],[16,0,125],[22,0,132],[30,0,140],[38,0,148],[46,0,158],[54,0,165],[64,0,173],[67,0,180],[81,0,189],[85,0,197],[92,0,206],[97,0,214],[104,0,223],[109,0,231],[114,0,238],[118,0,247],[122,0,255],[124,0,264],[126,0,271],[129,0,281],[131,0,287],[132,0,298],[133,0,304],[134,0,313],[134,0,321],[135,0,330],[135,0,336],[135,0,347],[136,0,559],[136,0,566],[137,0,573],[139,0,581],[140,0,590],[141,0,597],[142,0,606],[143,0,614],[144,0,623],[145,0,632],[146,0,641],[146,0,647],[146,0,658],[147,0,667],[147,0,671],[147,0,682],[147,0,999],[148,0,1101],[148,0,1169],[148,0,1448],[148,0,1457],[149,0,1465],[150,0,1474],[151,0,1482],[152,0,1489],[153,0,1497],[153,0,1505],[154,0,1514],[154,0,1522],[154,0,1532],[155,0,1538],[155,0,1549],[155,0,1565],[155,0,1891],[155,0,1915],[155,0,4968]]

def track(v):
    def m(a, r):
        x, y, z = a[0], a[1], a[2]
        return [int(x * r), int(y * r), int(z * r)]

    r = v / (track_list[-1][0] - 5)
    return [m(i, r) for i in track_list]


"""
用于生成坐标轨迹
"""
import math
import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

class GTrace(object):
    def __init__(self):
        self.__pos_x = []
        self.__pos_y = []
        self.__pos_z = []

    def __set_pt_time(self):
        """
        设置各节点的时间
        分析不同时间间隔中X坐标数量的占比
        统计结果: 1. 80%~90%的X坐标在15~20毫秒之间
                2. 10%~15%在20~200及以上，其中 [-a, 0, x, ...] 这里x只有一个，取值在110~200之间
                    坐标集最后3~5个坐标取值再50~400之间，最后一个坐标数值最大

        滑动总时间的取值规则: 图片宽度260，去掉滑块的宽度剩下200;
                        如果距离小于100，则耗时1300~1900之间
                        如果距离大于100，则耗时1700~2100之间
        """
        __end_pt_time = []
        __move_pt_time = []
        self.__pos_z = []

        total_move_time = self.__need_time * random.uniform(0.8, 0.9)
        start_point_time = random.uniform(110, 200)
        __start_pt_time = [0, 0, int(start_point_time)]

        sum_move_time = 0

        _tmp_total_move_time = total_move_time
        while True:
            delta_time = random.uniform(15, 20)
            if _tmp_total_move_time < delta_time:
                break

            sum_move_time += delta_time
            _tmp_total_move_time -= delta_time
            __move_pt_time.append(int(start_point_time+sum_move_time))

        last_pt_time = __move_pt_time[-1]
        __move_pt_time.append(last_pt_time+_tmp_total_move_time)

        sum_end_time = start_point_time + total_move_time
        other_point_time = self.__need_time - sum_end_time
        end_first_ptime = other_point_time / 2

        while True:
            delta_time = random.uniform(110, 200)
            if end_first_ptime - delta_time <= 0:
                break

            end_first_ptime -= delta_time
            sum_end_time += delta_time
            __end_pt_time.append(int(sum_end_time))

        __end_pt_time.append(int(sum_end_time + (other_point_time/2 + end_first_ptime)))
        self.__pos_z.extend(__start_pt_time)
        self.__pos_z.extend(__move_pt_time)
        self.__pos_z.extend(__end_pt_time)

    def __set_distance(self, _dist):
        """
        设置要生成的轨迹长度
        """
        self.__distance = _dist

        if _dist < 100:
            self.__need_time = int(random.uniform(500, 1500))
        else:
            self.__need_time = int(random.uniform(1000, 2000))

    def __get_pos_z(self):
        return self.__pos_z

    def __get_pos_y(self):
        _pos_y = [random.uniform(-40, -18), 0]
        point_count = len(self.__pos_z)
        x = np.linspace(-10, 15, point_count - len(_pos_y))
        arct_y = np.arctan(x)

        for _, val in enumerate(arct_y):
            _pos_y.append(val)

        return _pos_y

    def __get_pos_x(self, _distance):
        """
        绘制标准的数学函数图像: 以 tanh 开始 以 arctan 结尾
        根据此模型用等比时间差生成X坐标
        """
        # first_val = random.uniform(-40, -18)
        # _distance += first_val
        _pos_x = [random.uniform(-40, -18), 0]
        self.__set_distance(_distance)
        self.__set_pt_time()

        point_count = len(self.__pos_z)
        x = np.linspace(-1, 19, point_count-len(_pos_x))
        ss = np.arctan(x)
        th = np.tanh(x)

        for idx in range(0, len(th)):
            if th[idx] < ss[idx]:
                th[idx] = ss[idx]

        th += 1
        th *= (_distance / 2.5)

        i = 0
        start_idx = int(point_count/10)
        end_idx = int(point_count/50)
        delta_pt = abs(np.random.normal(scale=1.1, size=point_count-start_idx-end_idx))
        for idx in range(start_idx, point_count):
            if idx*1.3 > len(delta_pt):
                break

            th[idx] += delta_pt[i]
            i+=1

        _pos_x.extend(th)
        return _pos_x[-1], _pos_x

    def get_mouse_pos_path(self, distance):
        """
        获取滑动滑块鼠标的滑动轨迹坐标集合
        """
        result = []
        _distance, x = self.__get_pos_x(distance)
        y = self.__get_pos_y()
        z = self.__get_pos_z()

        for idx in range(len(x)):
            result.append([int(x[idx]), int(y[idx]), int(z[idx])])

        return int(_distance), result

if __name__ == "__main__":
    _color = ["blue", "green", "red", "cyan", "magenta"]
    trace = GTrace()

    # # for idx in range(0, 10):
    # distance = random.uniform(70, 150)
    # print("长度为: %d , 坐标为: \n" % distance)
    # distance, mouse_pos_path = trace.get_mouse_pos_path(distance)
    # print("长度为: %d , 坐标为: " % distance, mouse_pos_path)
