from collections import defaultdict


class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winners_map = defaultdict(int)
        losers_map = defaultdict(int)

        for match in matches:
            winners_map[match[0]] += 1
            losers_map[match[1]] += 1
            
        zero_losers = [k for k,v in winners_map.items() if k not in losers_map]
        zero_losers.sort()
        lost_1_match_only = [k for k,v in losers_map.items() if v == 1]
        lost_1_match_only.sort()
        print([zero_losers, lost_1_match_only])
        return [zero_losers, lost_1_match_only]