class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maximum = 0

        for customer in accounts:
            total = 0

            for money in customer:
                total += money
            maximum = max(maximum, total)   

        return maximum    

           
