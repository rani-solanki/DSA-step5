def knapSack(W, weight, values, n):

   if n == 0 or W == 0:
      return 0

   if (weight[n-1] > W):
      return knapSack(W, wt, val, n-1)
   else:
      return max(values[n-1] + knapSack(W-weight[n-1], weight, values, n-1),
        knapSack(W, weight, values, n-1))

values  = [60,100,120]
weight = [10, 20, 30]

W = 50
n = len(values)

print (knapSack(W, weight, values, n))


