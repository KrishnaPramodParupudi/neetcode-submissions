class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        for cha in s:
            if cha == '[' or cha== '{' or cha == '(' :
                stack_list.append(cha)
            else :
                if cha == ']' :
                    if len(stack_list)!=0 and stack_list[-1] == '[' :
                        stack_list.pop()
                    else :
                        stack_list.append(cha)
                if cha == '}' :
                    if len(stack_list)!=0 and stack_list[-1] == '{' :
                        stack_list.pop()
                    else :
                        stack_list.append(cha)
                if cha == ')' :
                    if len(stack_list)!=0 and stack_list[-1] == '(' :
                        stack_list.pop()
                    else :
                        stack_list.append(cha)
        if len(stack_list) != 0:
            return False
        return True
        