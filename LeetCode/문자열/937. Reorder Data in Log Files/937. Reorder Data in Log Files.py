class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []
        for i in logs:
            if i.split()[1].isdigit():
                digits.append(i)
            else:
                letters.append(i)
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
