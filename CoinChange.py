'''You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.'''


# DP solution using bottom-up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize a dp array to be the length of amount + 1 since we're going from 0 to the value of amount
        # set the default value inside to be amount + 1; aka the max value
        dp = [amount + 1] * (amount + 1)
        # set base case; if desired amount is 0, it'll just take 0 coins
        dp[0] = 0

        # for every number in the range of 1 to amount + 1...
        for num in range(1, amount + 1):
            # for every coin in our list of coins
            for coin in coins:
                # if the result is non-negative
                if num - coin >= 0:
                    # update the min to itself since this might be a possible solution
                    # for ex: if coin's val was 4 and our amount was 7, dp[7] = min(dp[7], 1 + dp[7-4])
                    dp[num] = min(dp[num], 1 + dp[num-coin])

        # return the amount if it is not equal to the default value,
        # otherwise we have to return -1 since we couldnt compute this amount with the given coins
        return dp[amount] if dp[amount] != amount + 1 else -1


# Time: O(amount * len(coins)) 'big o of amount and the number of coins we're given'
# Space: O(amount) since we have a dp array that we're having a potential value for every single amount