class Solution:
    def myAtoi(self, s: str) -> int:
        ansString = ""
        isPositive = True
        firstCharacter = True

        for char in s:
            if char.isspace() and firstCharacter:
                continue
            elif (char == "-" or char == "+") and firstCharacter:
                firstCharacter = False
                if char == "-":
                    isPositive = False

            elif char.isnumeric():
                ansString += char
                firstCharacter = False
            else:
                break

        if ansString == "":
            return 0
        if not isPositive:
            ansString = "-" + ansString
        if int(ansString) >= (2 ** 31) - 1:
            return ((2 ** 31) - 1)
        if int(ansString) <= (-2 ** 31):
            return (-2 ** 31)

        return int(ansString)

print(Solution().myAtoi("  0000000000012345678"))