import random
import matplotlib.pyplot as plt


class animal:

    def __init__(self, type_str: str):
        self.score = 1000
        self.type = type_str

    def score_add(self, score: int):
        self.score += score

    def score_return(self):
        return self.score

    def type_return(self):
        return self.type

    def fight(self, target_type):
        if self.type == "hawk":
            return True

        elif self.type == "pigeon":
            return False

        elif self.type == "avenger":
            if target_type == "hawk":
                return True
            elif target_type == "pigeon" or target_type == "avenger" or target_type == "test_avenger":
                return False

        elif self.type == "bully":
            if target_type == "hawk" or target_type == "avenger" or target_type == "test_avenger" or target_type == "bully":
                return False
            elif target_type == "pigeon":
                return True

        elif self.type == "test_avenger":
            if target_type == "hawk":
                return True
            elif target_type == "pigeon" or target_type == "test_avenger":
                return random.randrange(0, 2)
            elif target_type == "bully" or target_type == "avenger":
                return False


def food_reset(food: list, food_count: int):
    food.clear()
    food_init(food_list, food_count)


def animal_init(animals, hawk, pigeon, avenger, bully, test_avenger):
    notend = True
    while notend:
        if hawk > 0:
            animals.append(animal("hawk"))
            hawk -= 1
        if pigeon > 0:
            animals.append(animal("pigeon"))
            pigeon -= 1
        if avenger > 0:
            animals.append(animal("avenger"))
            avenger -= 1
        if bully > 0:
            animals.append(animal("bully"))
            bully -= 1
        if test_avenger > 0:
            animals.append(animal("test_avenger"))
            test_avenger -= 1
        if pigeon == 0 and hawk == 0 and test_avenger == 0 and bully == 0 and avenger == 0:
            notend = False


def food_init(food: list, food_count: int):
    while food_count > 0:
        food.append([])
        food_count -= 1


def double_check(food, anim, position: int, food_count: int):
    if len(food[position]) >= 2:
        position = random.randrange(0, food_count)
        return double_check(food, anim, position, food_count)
    else:
        food[position].append(anim)
        return


def end_checking(message):
    answer = input(message)
    if answer != "y" and answer != "n":
        return end_checking("문자가 잘못 입력 되었습니다 다시 입력하세요(y/n):")
    else:
        if answer == "y":
            return True
        else:
            return False


def food_list_show(food: list, food_count):
    for cur in range(0, food_count):
        print("{}번째 음식: ".format(cur + 1), end="")
        if len(food[cur]) != 0:
            print("객체1) 타입:{} 점수:{}".format(food[cur][0].type_return(), food[cur][0].score_return()), end="")
            if len(food[cur]) >= 2:
                print(" / 객체2) 타입:{} 점수:{}".format(food[cur][1].type_return(), food[cur][1].score_return()), end="")
        else:
            print("없음", end="")
        print()


def animal_list_show(anim: list):
    for cur in anim:
        print(cur.score_return())


# 매파는 언제나 공격
# 비둘기파는 언제나 도망침

animal_list = []
food_list = []
plot_hawk_list = []
plot_pigeon_list = []
plot_avenger_list = []
plot_bully_list = []
plot_test_avenger_list = []
plot_x_list = []

a = int(input("매파 개체수 입력:"))
b = int(input("비둘기파 개체수 입력:"))
c = int(input("보복자 개체수 입력:"))
d = int(input("불량배 개체수 입력:"))
e = int(input("시험 보복자 개체수 입력:"))
f = int(input("음식 개수 입력:"))

hawkplus = 0
pigeonplus = 0
avengerplus = 0
bullyplus = 0
test_avengerplus = 0

count = 0

daycount = int(input("날짜수 입력:"))

animal_init(animal_list, a, b, c, d, e)
food_init(food_list, f)

print("작업이 진행중입니다. 기다리세요...")

while daycount > 0:
    daycount -= 1
    count += 1
    plot_x_list.append(count)
    # print("{}일차".format(count))

    random.shuffle(animal_list)

    for i in animal_list:
        food_position = random.randrange(0, f)
        double_check(food_list, i, food_position, f)

    # food_list_show(food_list, f)
    # animal_list_show(animal_list)

    for cur in range(0, f):
        container = food_list[cur]
        if len(container) == 0:
            continue
        if len(container) == 1:
            container[0].score_add(80)
            continue
        res0 = container[0].fight(container[1].type_return())
        res1 = container[1].fight(container[0].type_return())
        if res0 == True and res1 == True:  # 둘다 중상, 하지만 한 개체는 먹이로 인해 점수 추가
            container[random.randrange(0, 2)].score_add(80)
            container[0].score_add(-150)
            container[1].score_add(-150)
        elif res0 == False and res1 == True:
            container[0].score_add(0)
            container[1].score_add(80)
        elif res0 == True and res1 == False:
            container[0].score_add(80)
            container[1].score_add(0)
        elif res0 == False and res1 == False:
            container[0].score_add(-10)
            container[1].score_add(-10)

    for i in animal_list:
        if i.type_return() == "hawk":
            hawkplus += i.score_return()
        elif i.type_return() == "pigeon":
            pigeonplus += i.score_return()
        elif i.type_return() == "avenger":
            avengerplus += i.score_return()
        elif i.type_return() == "bully":
            bullyplus += i.score_return()
        elif i.type_return() == "test_avenger":
            test_avengerplus += i.score_return()

    plot_hawk_list.append(hawkplus / a)
    plot_pigeon_list.append(pigeonplus / b)
    plot_avenger_list.append(avengerplus / c)
    plot_bully_list.append(bullyplus / d)
    plot_test_avenger_list.append(test_avengerplus / e)

    hawkplus = 0
    pigeonplus = 0
    avengerplus = 0
    bullyplus = 0
    test_avengerplus = 0

    food_reset(food_list, f)

    # if end_checking("프로그램을 종료합니까?(y/n):"):
    #    break

plt.xlabel('days')
plt.ylabel('average score')
plt.plot(plot_x_list, plot_hawk_list, 'r', label="hawk")
plt.plot(plot_x_list, plot_pigeon_list, 'b', label="pigeon")
plt.plot(plot_x_list, plot_avenger_list, 'g', label="avenger")
plt.plot(plot_x_list, plot_bully_list, 'y', label="bully")
plt.plot(plot_x_list, plot_test_avenger_list, 'c', label="test avenger")


plt.legend()
plt.show()
