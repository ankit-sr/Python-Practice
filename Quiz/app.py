from question import Question

prompts = [
    '\nWhat is the capital of India? \n1. Delhi-NCR \n2. Mumbai \n3. Kolkata',
    '\nWhat is the national animal of India? \n1. Cheetah \n2. Tiger \n3. Elephant',
    '\nWhat is the national sport of India? \n1. Cricket \n2. Football \n3. Hockey'
]

questions = [
    Question(prompts[0], 1),
    Question(prompts[1], 2),
    Question(prompts[2], 3)
]

score = 0
for question in questions:
    ans = int(input(question.question + '\nAnswer: '))
    if(ans == question.answer):
        score += 1

print('Congrats on completing the test, your score is ' + str(score) + '/3')