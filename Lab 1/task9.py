class MultiplyMatrices:
    def multiply_matrices(self, matrix1, matrix2):
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                element = 0
                for k in range(len(matrix2)):
                    element += matrix1[i][k] * matrix2[k][j]
                row.append(element)
            result.append(row)
        return result
    
mat = MultiplyMatrices()

res = mat.multiply_matrices([[1,2,3,4,5],[6,7,8,9,10]], [[1,2,3,4,5],[6,7,8,9,10]])

print(res)