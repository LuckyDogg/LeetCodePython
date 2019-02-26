from math import sqrt
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        for i in points:
            i.append(sqrt(i[0]*i[0]+i[1]*i[1]))

        points=sorted(points, key=lambda s: s[2])
        for i in points:
            del(i[2])

        return points[:K]


if __name__ == '__main__':
    t = Solution()
    points = [[2, -2], [1, 3]]
    K = 1
    print(t.kClosest(points, K))