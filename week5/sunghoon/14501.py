'''
/*문제 정보 */
14501번 - 퇴사
난이도 - 실버 3
/*풀이 방법 */
dp로 풀었는데 1일차 부터가 아니라 n 일차에서 1일차 역순으로 dp의 최대값을 넣어주고
풀었다. 현재일 + 소요시간이 퇴사일보다 크면 그 다음날 값을 dp에 저장해주고
퇴사일 보다 작거나 같으면 상담을 한경우, 안한 경우 중 최대값을 dp에 저장
'''
import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for i in range(n+1)]
t = []
p = []

for _ in range(n):
    T, P =map(int, input().split())
    t.append(T)
    p.append(P)

for i in range(n-1,-1,-1):
    if t[i] + i > n:  # 상담일 수가 퇴사일을 넘어간다면
        dp[i] = dp[i +1] # 다음 날 값 그대로 가져오기

    else:     # 상담을 한 경우, 안한경우 중 최댓값
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i])

print(dp[0])


'''
/*오답 노트*/
/*느낀 점*/
전에 풀어본 문제라 어느정도 뼈대를 잡을 수 있었다. 이 문제를 풀면서 헷갈린 점이
일수차랑 내가 설정한 i값이 다르다는 것이다. 일수차를 -1 해서 생각하면 이해하는데
어렵지 않았다. 무엇보다 종이에 적어서 천천히 진행해보니 이해하기 쉬웠다.
'''