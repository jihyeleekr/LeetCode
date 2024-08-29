class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        if len(list1) < len(list2):
            min_index = math.inf
            ind_sum = math.inf + 1
            for i in range(len(list1)):
                if list1[i] in list2:
                    ind_sum = i + list2.index(list1[i])
                    if ind_sum < min_index:
                        min_index  = ind_sum
                        ans = []
                        ans.append(list1[i])
                    elif ind_sum == min_index:
                        ans.append(list1[i])
                    else:
                        pass
                       
        else:
            min_index = math.inf
            ind_sum = math.inf + 1
            for i in range(len(list2)):
                if list2[i] in list1:
                    ind_sum = i + list1.index(list2[i])
                    if ind_sum < min_index:
                        min_index  = ind_sum
                        ans = []
                        ans.append(list2[i])
                    elif ind_sum == min_index:
                        ans.append(list2[i])
                    else:
                        pass
                

                        
        return ans
        