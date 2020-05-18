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
    sum_electricity = sitting_room + north_room + south_room + bedroom      #总电量
    sitting_room_money = sitting_room/sum_electricity * sum_money           #客厅实际费用
    north_room_money = north_room /sum_electricity * sum_money              #北次卧实际费用
    south_room_money = south_room /sum_electricity * sum_money              #南主卧实际费用
    bedroom_money = bedroom /sum_electricity * sum_money                    #南次卧实际用费用

    print("方案一")
    print("北卧应付: {}".format(north_room_money + (sitting_room_money/5) * 1))      #1人
    print("南主卧应付: {}".format(south_room_money + (sitting_room_money/5) * 2))    #2人
    print("南次卧应付: {}".format(bedroom_money + (sitting_room_money/5) * 2))       #2人
    print()
    print("---------------- >>>>>>下面是方案二 ------------------------>>>>>>")
    print()

def electricity_avg_two(sitting_room,north_room,south_room,bedroom,sum_money):
    """
    公摊用电量分摊到每个房间里面
    :param sitting_room:    客厅实际用电量
    :param north_room:      北卧实际用电量
    :param south_room:      南主卧实际用电量
    :param public:          南次卧实际用电量
    :param sum_money:       总钱数
    :return:
    """
    sum_electricity = sitting_room + north_room + south_room + bedroom      #总电量
    sitting_room_money = sitting_room/sum_electricity * sum_money           #客厅实际费用
    north_room_money = (north_room + ((sitting_room/5)*1)) /sum_electricity * sum_money              #北次卧实际费用
    south_room_money = (south_room + ((sitting_room/5)*2))/sum_electricity * sum_money              #南主卧实际费用
    bedroom_money = (bedroom + ((sitting_room/5)*2)) /sum_electricity * sum_money                    #南次卧实际用费用

    print("方案二")
    print("公摊实际费用：{}".format(sitting_room_money))
    print("北卧应付: {}".format(north_room_money))      #1人
    print("南主卧应付: {}".format(south_room_money))    #2人
    print("南次卧应付: {}".format(bedroom_money))       #2人

electricity_avg(50,60,70,20,300)
electricity_avg_two(50,60,70,20,300)