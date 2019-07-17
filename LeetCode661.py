class Solution:
    def imageSmoother(self, M):
        l=[]
        def struct_list(index1, index2):
            l = []
            for i in range(0, 3):
                for j in range(0, 3):
                    try:
                        print(M[index1+i-2][index2+j-2])
                        l.append(M[index1+i-2][index2+j-2])
                    except Exception as e:
                        pass
            print(sum(l)/len(l))
            return int(sum(l)/len(l))

        for i in range(len(M)):
            l.append([])
            for j in range(len(M[i])):
                l[i][j] = struct_list(i, j)

        return l




if __name__ == '__main__':
    test=Solution()
    s=[[1, 1, 1],
     [1, 0, 1],
     [1, 1, 1]]
    print(test.imageSmoother(s))



