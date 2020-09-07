

# 常量
total = 16                      # 建筑总数
buildingType = '画室'
waitingTime = 6                 # 等待时长 (分钟)
pro_type_level = 0              # 生产等级
pro_manager = 1                 # 生产者


bias_max = 2                    # 最大偏移像素
drag_distance = 50              # 拖拽距离
safe_point_x = 1765
safe_point_y = 775              # 安全区
cachet_xy = [148, 853]          # 府印
ground_sill_xy = [508, 480]     # 地基
map_choice_xy = [280, 475]      # 地图选项
city_1_in_map_xy = [631, 680]   # 应天府在地图上的坐标(未移动过)
city_2_in_map_xy = [1445, 900]  # 苏州府在地图上的坐标(移动过)
is_tax_station_work = False  # 税课司工作否 工作1 休息0
book_xy = [1148, 465]

# 0级生产选项
# pro_type_x = 770
# pro_type_y = 270
#
# pro_type_x_3 = 1328
# pro_type_y_3 = 602
pro_type = [[770,270], [1320, 270], [770, 630], [1320, 630]]
'''
窗口最大化时
0 2 X:  770
0 1 Y:  270
1 3 X:  1320
2 3 Y:  630  
'''
# 不使用角色
pro_manager_pos = [[765, 260], [1305, 270]]
# pro_manager_x_0 = 765
# pro_manager_y_0 = 260
#
# # 使用第一位角色
# pro_manager_x = 1305
# pro_manager_y = 270



if __name__ == '__main__':
    pass