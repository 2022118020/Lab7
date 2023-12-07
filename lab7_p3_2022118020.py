
class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]
    return sum

class list_D2(list):
    def __init__(self,arr):
        
        ### YOUR CODE HERE ###
        if not (type(arr[0]) == list) :
            raise  not2DError()
        length = len(arr[0])
        for a in arr :
            if not (len(a) == length) :
                raise unevenListError()
    
        ######

        self.extend(arr)

    def __str__(self):

        ### YOUR CODE HERE ###
        m = len(self)
        n = len(self[0])

        result = str(m)+'*'+str(n)    
        return 'list_2D: '+ result

        ######

    def transpose(self):

        ### YOUR CODE HERE ###
        new_list = []
        for j in range(len(self[0])):
            temp_list = []
            for i in range(len(self)):
                temp_list.append(self[i][j])
            new_list.append(temp_list)
        self = list_D2(new_list)
        return self
        
        ######


    def __matmul__(self, others):
        
        ### YOUR CODE HERE ###
        m = len(self[0])
        n = len(others)
        if not (m == n) :
            raise improperMatrixError()
        else :
            new_list = [[0]*len(others[0]) for _ in range(len(self))]
            for i in range(len(self)):
                for j in range(len(others[0])):
                    for k in range(len(self[0])):
                        new_list[i][j] += self[i][k] * others[k][j]
            self = list_D2(new_list)
        return self

        ######

    def avg(self):

        ### YOUR CODE HERE ###
        sum = 0
        count = 0
        for i in self :
            for j in i :
                sum += j
                count += 1
        return sum / count

        ######