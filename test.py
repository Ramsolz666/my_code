def count(s):
    num = []
    stack = []
    a = {'+','-','*','/','(',')'}
    for i in s:
        if i in a:
            if i == ')':
                while stack and stack[-1] != '(':
                    num.append(stack.pop())
                stack.pop()
            #     这里的想法有问题，应该是弹至优先级更小为止
            elif i in {'+','-'}:
                if stack and stack[-1] in {'*','/'}:
                    while stack and stack[-1] in {'*','/'}:
                        num.append(stack.pop())
                    num.append(i)
                else:
                    stack.append(i)
            else:
                stack.append(i)
        else:
            num.append(i)
        print(num,stack)
    return num+stack

def count_res(s):
    # num = count(s)
    num = ['1','2','*','5','3','-','1','/','+']
    a = {'+','-','*','/'}
    while num:
        for i in range(len(num)):
            if num[i] in a:
                if len(num) != 3:
                    num = num[:i-2] + [str(eval(num[i-2]+num[i]+num[i-1]))] + num[i+1:]
                    break
                else:
                    return eval(num[i-2]+num[i]+num[i-1])

var = '1*2+(5-3)/1'


res = count_res(var)
print(res)