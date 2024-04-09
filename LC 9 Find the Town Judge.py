"""
997. Find the Town Judge

In a town, there are n people labeled from 1 to n.
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled
ai trusts the person labeled bi. If a trust relationship does not exist in trust array,
then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
"""


class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        #Объявляем хэш-таблиц
        trust_ai = {}
        trust_bi = {}

        if trust == [] and n == 1:
           return 1
        elif trust == [] and n != 1:
            return -1

        #Заполняем хэш-таблицы из тех кто верит и кому верят
        for i in range(n+1):
            trust_ai[i] = 0
            trust_bi[i] = 0

        # Заполняем хэш-таблицу trust_ai
        for ai in range(len(trust)):
            if trust[ai][0] in trust_ai:
                trust_ai[trust[ai][0]] += 1

        # Заполняем хэш-таблицу trust_bi
        for bi in range(len(trust)):
            if trust[bi][1] in trust_bi:
                trust_bi[trust[bi][1]] += 1

        #Поиск в trust_bi ключа со значением N-1
        for key_trust_bi in range(len(trust_bi)):
            if trust_bi[key_trust_bi] == n-1:
                if trust_ai[key_trust_bi] == 0:
                    return key_trust_bi
        return -1