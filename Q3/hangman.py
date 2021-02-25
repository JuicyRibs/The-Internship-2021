ans = list(map(int, (input().split(" "))))
out = ["_"]*12
wrong = []
score  = 0

def print_ans(ans, wrong):
    for i in ans:
        print(i, end=" ")
    for i in wrong:
        print(i, end=" ")
    print("")

for i in range(5):
    num = int(input())
    if (num in ans):
        for n in range(len(ans)):
            if(num == ans[n]):
                out[n] = str(num)
                score += 1
    else:
        wrong.append(num)
        
    print_ans(out, wrong)
print(score)