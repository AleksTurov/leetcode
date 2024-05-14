class Solution:
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0  
        for customer_accounts in accounts:  
            customer_wealth = sum(customer_accounts)  
            if customer_wealth > max_wealth:  
                max_wealth = customer_wealth
        return max_wealth  
    
solution = Solution()
accounts = [[1,2,3],[3,2,1]]
max_wealth = solution.maximumWealth(accounts)
print(max_wealth)