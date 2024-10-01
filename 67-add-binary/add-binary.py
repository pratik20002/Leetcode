class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        result = []

        while i >= 0 or j >= 0:
            curr_i = int(a[i]) if i >= 0 else 0
            curr_j = int(b[j]) if j >= 0 else 0

            curr_sum = carry + curr_i + curr_j
            result.append(str(curr_sum % 2))

            carry = curr_sum // 2

            i -= 1
            j -= 1

        if carry:
            result.append(str(carry))

        return "".join(reversed(result))