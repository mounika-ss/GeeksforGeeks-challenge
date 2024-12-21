# User function template for Python
class Solution:
    def addBinary(self, s1, s2):
        # Initialize pointers to the last indices of s1 and s2
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0  # Initialize carry to handle overflow during addition
        result = []  # List to store the binary result bits
        
        # Loop until all bits and carry are processed
        while i >= 0 or j >= 0 or carry:
            # Get the bit value from s1 and s2; use 0 if index is out of range
            bit1 = int(s1[i]) if i >= 0 else 0
            bit2 = int(s2[j]) if j >= 0 else 0
            
            # Compute the sum of bits and carry
            current_sum = bit1 + bit2 + carry
            
            # Append the remainder of division by 2 to result (binary addition result)
            result.append(str(current_sum % 2))
            
            # Update carry by the quotient of division by 2
            carry = current_sum // 2
            
            # Move pointers to the previous bits
            i -= 1
            j -= 1
        
        # Reverse result to get the correct binary order and strip leading zeros
        # Ensure result is not empty and return as a string
        return ''.join(result[::-1]).lstrip('0') or '0'

# Driver code for testing
if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for _ in range(T):
        a = input().strip()  # First binary string
        b = input().strip()  # Second binary string
        ob = Solution()
        answer = ob.addBinary(a, b)  # Get the result of binary addition
        print(answer)  # Output the result
        print("~")  # Mark end of each test case output
