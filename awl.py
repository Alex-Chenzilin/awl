## written by cosmos zhong    plagiarism   by zilin chen
#直接跑就好奶奶都能玩

import getpass, os

num_votes = {5:[2,3,2,3,3],6:[2,3,4,3,3],7:[2,3,3,4,4],8:[3,4,4,5,5],9:[3,4,4,5,5],10:[3,4,4,5,5]}
start = '1'
while start == '1':
    wins = 0
    loses = 0
    stat = []
    print("欢迎来到阿瓦隆")
    player = int(input("请输入玩家人数：(5-10)"))
    num_vote = num_votes[player]
    for i in range(5):
        count = 0
        votes = []
        print("这是第%d轮"%(i+1))

        for j in range(num_vote[i]):
            n = str(j+1)
            print("输入1同意，输入2不同意,然后按回车")
            print("第%d轮"%(i+1)+"第"+ n + "人")
            vote = getpass.getpass("vote:")
            while vote != "1" and vote != "2":
                vote = getpass.getpass("请输入1或2:")
            votes.append(int(vote))
            print("第%d轮"%(i+1)+"第"+ n + "人投票完毕\n\n")
        for k in votes:
            if k == 2:
                count += 1
        if i == 3 and player >= 7:
            if count == 2:
                loses += 1
                print("第%d轮投票失败\n\n\n"%(i+1) * 4)
            else:
                wins += 1
                print("第%d轮投票成功\n\n\n"%(i+1) * 4) 
        else:
            if count == 0:
                wins += 1
                print("第%d轮投票成功\n\n\n"%(i+1) * 4) 
            else:
                loses += 1
                print("第%d轮投票失败\n\n\n"%(i+1) * 4) 

        stat.append(votes)
        if wins == 3:
            print("好人胜利\n" * 10)
            break
        if loses == 3:
            print("坏人胜利\n" * 10)
            break

    print("历史投票为：\n") 
    print(stat)
    start = input("输入1重新开始")
    os.system('clear')