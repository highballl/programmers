info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# result = [1,1,1,1,2,4]

from collections import Counter, defaultdict, deque

def solution(info, query):

    requirements = []

    # 정보가 들어오는 순서가 일치한다
    # 다만 쿼리에는 인포보다 정보가 몇 개 적게 들어가 있다
    # 정보를 1:1매칭하면서 지원자 수 카운트를 하면 n * m 시간복잡도 발생할 것
        # 적당히 필터링 하더라도 결국 n * m 복잡도가 발생하면 효율성 테스트 미통과
        # 효율성 테스트 실패 사례:
        # 일정 점수 이상인 사람들 중(n개의 자료 조회)
        # 쿼리에 있는 조건을 모두 만족하는 사람을 찾자(m개의 쿼리문 조회)

    # 이중 for를 피하려면,
    # 각 자료를 최소한의 조회가 발생하게 전처리 한 다음 비교 작업을 수행해보자
    # 하지만 찾아보니 문자열에 replace를 적용하면 시간초과가 발생한다고 한다.
    # 문자열 전처리에 드는 시간도 최소화하자.
    # replace 함수를 버렸다. 

    # 1:1 매칭 및 문자열 비교 도전 - 
        # 조건 4가지에 해당하는 문자을 압축해보자.
        # 각 조건에 맞는 경우를 코드화하여 문자열 -> 정수형 변환 후 연산을 해보자.

    # requirements - person_info >= 0 : pass
        

    # language = ['cpp', 'java', 'python', '-']
    # field = ['backend', 'frontend', '-']
    # career = ['junior', 'senior', '-']
    # food = ['chicken', 'pizza', '-']


    from collections import deque, defaultdict
    from functools import reduce

def solution(info, query):


    # query preprocessing
    requirements = []
    #requirements = defaultdict(list)
    for q in query:
        que = deque(sorted(Counter(q.split())))
        #base_score = 0
        print(que)
        while que:
            if que[0] == '-':
                que.popleft()
            elif que[0].isnumeric():
                base_score = que[0]
                que.popleft()
            elif que[0] == 'and':
                que.popleft()
                break
            #que.popleft()
        requirements.append([set(que), int(base_score)])
        #requirements[set(que)].append(int(base_score))
    
    #applicants = []
    applicants = defaultdict(list)
    for p in info:
        person = deque(sorted(Counter(p.split())))
        score = person[0]
        person.popleft()
        #applicants.append([set(person), score])
        applicants[set(person)].append(int(score))

    
    answer = []
    for r in enumerate(requirements):
        sum = 0
        standard = r[1]
        if r[0] == applicants[r]:
            applicants[r].sort()
            mid = len(applicants) // 2
            pivot = applicants[mid]
        
            if pivot > requirements[1]
        # for applicant in applicants:
        #     #print(set(r[0]), "and", set(applicant[0]))
        #     if applicant[1] >= r[1] and len(r[0] - applicant[0]) == 0:
        #         sum += 1
        answer.append(sum)
        
    return answer
        



    # query preprocessing
    # requirements = []
    # for q in query:
    #     deq = deque(q)
    #     q_code = ""
    #     base_score = ""
    #     word = ""
    #     while deq:
    #         if deq[0].isalpha() and len(word) <= 1 and word.startswith('a') is False:
    #             word += deq[0]
    #             deq.popleft()
    #         elif deq[0].isalpha() and len(word) > 1:
    #             deq.popleft()
    #         elif deq[0] == " ":
    #             if word == "a":
    #                 word = ""
    #             elif word != "":
    #                 q_code += word
    #                 print("q_code", q_code)
    #                 word = ""
    #             deq.popleft()
    #         elif deq[0].isnumeric():
    #             base_score += deq[0]
    #             deq.popleft()
    #         else:
    #             deq.popleft()
        
    #     requirements.append([q_code, int(base_score)])

    # # info preprocessing
    # applicants = []
    # for person in info:
    #     dep = deque(person)
    #     p_code = ""
    #     score = ""
    #     word = ""
    #     while dep:
    #         if dep[0].isalpha() and len(word) <= 1:
    #             word += dep[0]
    #             dep.popleft()
    #         elif dep[0].isalpha() and len(word) > 1:
    #             dep.popleft()
    #         elif dep[0] == " ":
    #             p_code += word
    #             print("p_code", p_code)
    #             word = ""
    #             dep.popleft()
    #         elif dep[0].isnumeric():
    #             score += dep[0]
    #             dep.popleft()
    #         else:
    #             dep.popleft()
        
    #     applicants.append([p_code, int(score)])

        
        
    # answer = []
    # for r in requirements:
    #     sum = 0
    #     for applicant in applicants:
    #         #print(set(r[0]), "and", set(applicant[0]))
    #         if applicant[1] >= r[1] and len(set(r[0]) - set(applicant[0])) == 0:
    #             sum += 1
    #     answer.append(sum)
        
    # return answer


    # # query preprocessing
    # requirements = []
    # for q in query:
    #     deq = deque(q.split())
    #     q_code = ""
    #     while deq:
    #         if deq[0] == "and":
    #             deq.popleft()
    #         elif deq[0] in language:
    #             q_code += str(language.index(deq[0])+1)
    #             deq.popleft()
    #         elif deq[0] in field:
    #             q_code += str(field.index(deq[0])+1)
    #             deq.popleft()
    #         elif deq[0] in career:
    #             q_code += str(career.index(deq[0])+1)
    #             deq.popleft()
    #         elif deq[0] in food:
    #             q_code += str(food.index(deq[0])+1)
    #         elif deq[0].isnumeric():
    #             base_score = int(deq[0])
    #             deq.popleft()
    #         else:
    #             deq.popleft()
    #     requirements.append([int(q_code), base_score])
    
    # # info preprocessing
    # applicants = []
    # for person in info:
    #     p = deque(person.split())
    #     p_code = ""
    #     while p:
    #         if p[0] in language:
    #             p_code += str(language.index(p[0])+1)
    #             p.popleft()
    #         elif p[0] in field:
    #             p_code += str(field.index(p[0])+1)
    #             p.popleft()
    #         elif p[0] in career:
    #             p_code += str(career.index(p[0])+1)
    #             p.popleft()
    #         elif p[0] in food:
    #             p_code += str(food.index(p[0])+1)
    #         elif p[0].isnumeric():
    #             score = int(p[0])
    #             p.popleft()
    #         else:
    #             p.popleft()
    #     applicants.append([int(p_code), score])

    
    # # filtering
    # answer = []
    # for r in requirements:
    #     sum = 0
    #     for applicant in applicants:
    #         print(applicant[1], r[1], r[0], applicant[0])
    #         if applicant[1] >= r[1] and r[0] - applicant[0] >= 0:
    #             sum += 1
    #     answer.append(sum)
    #     print(sum)
    # return answer     


    # for q in query:
    #     deq = deque(q)
    #     q_code = ""
    #     base_score = ""
    #     word = ""
    #     while deq:
    #         if deq[0].isalpha() and len(word) <= 1 and word.startswith('a') is False:
    #             word += deq[0]
    #             deq.popleft()
    #         elif deq[0].isalpha() and len(word) > 1:
    #             deq.popleft()
    #         elif deq[0] == " ":
    #             if word == "a":
    #                 word = ""
    #             elif word != "":
    #                 q_code += word
    #                 word = ""
    #             deq.popleft()
    #         elif deq[0].isnumeric():
    #             base_score += deq[0]
    #             deq.popleft()
    #         else:
    #             deq.popleft()
        
    #     requirements.append([q_code, int(base_score)])

    # # info preprocessing
    # applicants = []
    # for person in info:
    #     dep = deque(person)
    #     p_code = ""
    #     score = ""
    #     word = ""
    #     while dep:
    #         if dep[0].isalpha() and len(word) <= 1:
    #             word += dep[0]
    #             dep.popleft()
    #         elif dep[0].isalpha() and len(word) > 1:
    #             dep.popleft()
    #         elif dep[0] == " ":
    #             p_code += word
    #             word = ""
    #             dep.popleft()
    #         elif dep[0].isnumeric():
    #             score += dep[0]
    #             dep.popleft()
    #         else:
    #             dep.popleft()
        
    #     applicants.append([p_code, int(score)])

    # info preprocessing
    # applicants = []
    # for person in info:
    #     person_info = person.split()
    #     score = int(person_info[-1])
    #     person_info.pop()
    #     applicants.append([set(person_info), score])


    # requirements = []
    # for q in query:
    #     q_list = deque(q.split())
    #     base_score = 0
    #     #print("initial", q_list)
    #     while q_list:
    #         if q_list[0] == "and" or q_list[0] == "-":
    #             q_list.popleft()
    #             #print("is pop")
    #             #print(q_list)
    #         # score is the last element    
    #         elif q_list[0].isnumeric():
    #             base_score = int(q_list.popleft())
    #             #print("base_score", base_score)
    #             break
    #         else:
    #             q_list.rotate(-1)
    #     #q_list = q.replace('and', ' ').replace('-', '').split()
    #     #base_score = int(q_list[-1])
    #     #requirements.append([set(q_list[:-1]), base_score])
    #     #print(set(q_list))
    #     requirements.append([set(q_list), base_score])


    
    # # info preprocessing
    # applicants = []
    # for person in info:
    #     person_info = person.split()
    #     score = int(person_info[-1])
    #     applicants.append([set(person_info[:-1]), score])
        
     
    # # filtering
    
    # answer = []
    # for r in requirements:
    #     sum = 0
    #     for applicant in applicants:
    #         print(applicant[1], r[1], r[0], applicant[0])
    #         if applicant[1] >= r[1] and len(set(r[0]) - set(applicant[0])) == 0:
    #             sum += 1
    #     answer.append(sum)
    #     print(sum)
    # return answer

    # for q in query:
    #     q_list = q.replace('and', ' ').replace('-', '').split()
    #     base_score = int(q_list[-1])
    #     requirements = q_list[:-1]
    #     sum = 0
    #     for val in info:
    #         applicant = val.split(' ')
    #         score = int(applicant[-1])
    #         if score >= base_score and len(set(requirements) - set(applicant[:-1])) == 0:
    #             sum += 1
    #     answer.append(sum)


    # applicants = Counter()

    # for val in info:
    #     applicant = val.split(' ')
    #     score = int(applicant[-1])
    #     applicant_info = Counter(applicant[:-1])
    #     applicants += applicant_info


    # # info search
    # for idx, base_score in enumerate(criteria):
    #     sum = 0
    #     for val in info:
    #         applicant = val.split(' ')
    #         score = int(applicant[-1])
    #         if score >= base_score and len(set(requirements[idx]) - set(applicant[:-1])) == 0:
    #             #temp = Counter(applicant[:-1])
    #             #temp = Counter(applicant[:-1]) & Counter(requirements[i])
    #             #count += temp
    #             sum += 1
    #     answer.append(sum)
    



    # return answer


print(solution(info, query))