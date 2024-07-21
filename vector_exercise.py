# 1 a - length of vector
import numpy as np
def compute_vector_length(vector):
    vector = np.array(vector)
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector
compute_vector_length([3,4]) # test: result = 5

# 1 b - dot product
def compute_dot_product(vector1,vector2):
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    dot_product = np.dot(vector1,vector2)
    return dot_product
compute_dot_product([1,2],[3,4]) # test: result = 11