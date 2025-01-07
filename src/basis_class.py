import numpy as np
class Basis():

    def __init__(self, dimensions):
        if (dimensions % 2 != 0) or (dimensions <=0) or (type(dimensions) is not int):
            raise Exception("Only positive even integers allowed!")
        else:
            self._dimensions = dimensions

    @property
    def dimension(self):
        return self._dimensions

    
    def create_basis_vectors(self, index):
        if index < 0: 
            raise Exception("Index can't be less than zero!")
        else:
            vector = np.zeros(self._dimensions)
            vector[index] = 1
        return vector
    
    def create_single_symmetric_basis_matrix(self, first_index, second_index):
        
        if second_index >= first_index:
            raise Exception("first_index must be larger than second_index!")
        else:
            first_index_vector = self.create_basis_vectors(first_index)
            second_index_vector = self.create_basis_vectors(second_index)
            matrix = 0.5*(np.outer(second_index_vector, first_index_vector) + np.outer(first_index_vector, second_index_vector))
            return matrix
        
    def create_single_antisymmetric_basis_matrix(self, first_index, second_index):
        
        if second_index >= first_index:
            raise Exception("first_index must be larger than second_index!")
        else:
            first_index_vector = self.create_basis_vectors(first_index)
            second_index_vector = self.create_basis_vectors(second_index)
            matrix = -0.5j*(np.outer(second_index_vector, first_index_vector) - np.outer(first_index_vector, second_index_vector))
            return matrix

    




    

