class Solution:
	def nextSmallerEle(self, arr):
		next_greater = [-1]*len(arr)
        stack = []

        for i in range(len(arr) - 1, -1, -1) :
            while stack and stack[-1] >= arr[i]:
                stack.pop()

            if not stack:
                next_greater[i] = -1
            else:
                 next_greater[i] = stack[-1]

            stack.append(arr[i])

        return next_greater
                        

                    