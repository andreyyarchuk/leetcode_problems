class Solution(object):
    def addTwoNumbers(self, l1, l2):
        str_l1 = (''.join(map(str,l1)))
        str_l2 = (''.join(map(str, l2)))

        result_sum_str = str(int(str_l1) + int(str_l2))
        result_sum_list = []
        for i in range(len(result_sum_str)):
            result_sum_list.insert(0, int(result_sum_str[i]))
        return result_sum_list
