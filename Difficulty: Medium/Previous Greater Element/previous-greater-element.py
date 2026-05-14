class Solution:
	def preGreaterEle(self, arr):
	    
        stack = []
        dict = {}

        n = len(arr)

        for i in range(0,len(arr)):

            while stack and stack[-1] <= arr[i % n]:
                stack.pop()

            if not stack:
                dict[i % n] = -1
            else:
                dict[i % n] = stack[-1]

            stack.append(arr[i % n])

        ans = []

        for i in range(n):
            ans.append(dict[i])

        return ans
