class Solution:
    def myAtoi(self, s):
        # atoi means string to integer
        sign, index, result, n = 1, 0, 0, len(s)
        
        # Step 1: Remove/ignore leading whitespaces
        while s[index] == ' ':
            index = index + 1  # Move the index to the next non-space character
            
        # Step 2: Check if a sign ('+' or '-') is present
        if index < n and (s[index] == '-' or s[index] == '+'):
            sign = -1 if s[index] == '-' else 1 
            index = index + 1  # Move to the next character after the sign 
            
        # Step 3: Convert digits to result until a non-digit character is encountered
        while index < n and ('0' <= s[index] <= '9'):
            # Convert the current character to an integer by using ASCII values
            # ord() converts the character to its ASCII value
            # Subtracting ord('0') from ord(s[index]) gives the corresponding integer value of the digit
            result = result * 10 + (ord(s[index]) - ord('0'))
            
            # Overflow/underflow handling: if the result exceeds INT_MAX or is less than INT_MIN
            if result > (2**31 - 1):
                return sign * (2**31 - 1) if sign == 1 else -2**31
            
            index = index + 1  # Increment index for the while loop
    
        # Return the result with the correct sign
        return sign * result
