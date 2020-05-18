def electricity_avg(sitting_room,north_room,south_room,bedroom,sum_money):
    """
    （（每个房间的用电量/实际总电量)*总钱数） + 公摊人均电费
    :param sitting_room:    客厅实际用电量
    :param north_room:      北卧实际用电量
    :param south_room:      南主卧实际用电量
    :param public:          南次卧实际用电量
    :param sum_money:       总钱数
    :return:
    """
    sum_electricity = sitting_room + north_room + south_room + bedroom
    sitting_room_money = sitting_room/sum_electricity * sum_money
    north_room_money = north_room /sum_electricity * sum_money
    south_room_money = south_room /sum_electricity * sum_money
    bedroom_money = bedroom /sum_electricity * sum_money

    print("北卧应付: {}".format(north_room_money + (sitting_room_money/5) * 1))      #1人
    print("南主卧应付: {}".format(south_room_money + (sitting_room_money/5) * 2))    #2人
    print("南次卧应付: {}".format(bedroom_money + (sitting_room_money/5) * 2))       #2人

electricity_avg(50,60,70,20,300)