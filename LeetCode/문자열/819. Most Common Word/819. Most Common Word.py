import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ary = []
        for i in re.sub('[^\w]', ' ', paragraph).lower().split():
            if i not in banned: ary.append(i)
        return Counter(ary).most_common(1)[0][0]
