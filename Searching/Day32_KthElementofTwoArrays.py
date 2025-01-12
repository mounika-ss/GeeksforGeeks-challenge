# User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        n = len(a)
        m = len(b)

        last = 0
        i, j = 0, 0

        for _ in range(k):
            if i < n:
                # if a[i] > b[j] then increment j
                if j < m and a[i] > b[j]:
                    last = b[j]
                    j += 1
                # else increment i
                else:
                    last = a[i]
                    i += 1
            # if reached end of first array then increment j
            elif j < m:
                last = b[j]
                j += 1

        return last


#{ 
 # Driver Code Starts
# Initial Template for Python 3

def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
