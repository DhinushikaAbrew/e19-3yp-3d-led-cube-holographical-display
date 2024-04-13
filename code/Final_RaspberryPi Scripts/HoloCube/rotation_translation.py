import numpy as np



def list_to_matrix(lst):
    ls = []
    n = round(len(lst) ** (1/3))
    for j in range(n):
        ls.append([])
        for i in range(n):
            ls[j].append([])
            for k in range(n):
                ls[j][i].append(lst[k + i*n + j*n*n])
    return ls

#[[[1,2],[3,4]],[[5,6],[7,8]]] #outer ==> z axis middle ==> y axis inner ==> x axis
#[[1,2],[3,4]] ==> bottom layer; [[5,6],[7,8]] ==> top layer



#to shift the layers from bottom to top
#there is an error happens when the objects shifts more to get erased; it is not retrieved
def shift_matrix_top(matrix, shift=1):
    ls_shift_top = []
    for i in range(shift):
        ls_shift_top.append((np.array(matrix[i])*0).tolist())
    for i in range(len(matrix)-shift):
        ls_shift_top.append(matrix[i])
    return ls_shift_top


#to shift the layers from top to bottom 
#there is an error happens when the objects shifts more to get erased; it is not retrieved
def shift_matrix_bottom(matrix, shift=1):
    ls_shift_bottom = []
    for i in range(len(matrix)-shift):
        ls_shift_bottom.append(matrix[i+shift])
    for i in range(shift):
        ls_shift_bottom.append((np.array(matrix[i]) * 0).tolist())
    return ls_shift_bottom

#to shift the layers from zero y to positive y
#there is an error happens when the objects shifts more to get erased; it is not retrieved
def shift_matrix_yout(matrix, shift=1):
    ls_shift_yout= []

    for i in range(len(matrix)):
        ls_shift_yout.append([])

    for i in range(shift):
        for j in range(len(matrix)):
            ls_shift_yout[j].append((np.array(matrix[j][i]) * 0).tolist())
    for i in range(len(matrix)-shift):
        for j in range(len(matrix)):
            ls_shift_yout[j].append(matrix[j][i])
    return ls_shift_yout

#to shift the layers from positive y to zero y
#there is an error happens when the objects shifts more to get erased; it is not retrieved
def shift_matrix_yin(matrix, shift=1):
    ls_shift_yin= []

    for i in range(len(matrix)):
        ls_shift_yin.append([])

    for i in range(len(matrix)-shift):
        for j in range(len(matrix)):
            ls_shift_yin[j].append(matrix[j][i+shift])

    for i in range(shift):
        for j in range(len(matrix)):
            ls_shift_yin[j].append((np.array(matrix[j][i]) * 0).tolist())

    return ls_shift_yin


#to shift the layers from zero x to positive x
#there is an error happens when the objects shifts more to get erased; it is not retrieved
def shift_matrix_xout(matrix, shift=1):
    ls_shift_xout= []

    for i in range(len(matrix)):
        ls_shift_xout.append([])
        for j in range(len(matrix[0])):
            ls_shift_xout[i].append([])

    for i in range(shift):
        for j in range(len(matrix[0])):
            for k in range(len(matrix)):
                ls_shift_xout[k][j].append((np.array(matrix[k][j][i]) * 0).tolist())

    for i in range(len(matrix)-shift):
        for j in range(len(matrix[0])):
            for k in range(len(matrix)):
                ls_shift_xout[k][j].append(matrix[k][j][i])

    return ls_shift_xout

#to shift the layers from positive x to zero x
#there is an error happens when the objects shifts more to get erased; it is not retrieved

def shift_matrix_xin(matrix, shift=1):
    ls_shift_xin= []

    for i in range(len(matrix)):
        ls_shift_xin.append([])
        for j in range(len(matrix[0])):
            ls_shift_xin[i].append([])

    for i in range(len(matrix)-shift):
        for j in range(len(matrix[0])):
            for k in range(len(matrix)):
                ls_shift_xin[k][j].append(matrix[k][j][i+shift])

    for i in range(shift):
        for j in range(len(matrix[0])):
            for k in range(len(matrix)):
                ls_shift_xin[k][j].append((np.array(matrix[k][j][i]) * 0).tolist())

    return ls_shift_xin

#to scale the matrix to increase the size of the cube


#to scale the matrix to decrease the size of the cube



#to rotate a 2D plane
def rotate_xy(matrix, angle=10):
    # Rotate the matrix by the specified angle
    rotated_matrix = rotate(matrix, angle, reshape=False)
    rounded_matrix = np.round(rotated_matrix).astype(int)  # Round off values to integers
    return rounded_matrix


#to rotate the matrix in the z axis    
def rotate_matz(matrix, angle=10):
    #rotate a matrix around z axis
    rotated_matrix = []
    for i in range(len(matrix)):
        rotated_matrix.append(rotate_xy(matrix[i], angle).tolist())
    return rotated_matrix

def rotate_matx(matrix, angle=10):
    #repeate for all layers in x axis
    #cteate a plan in x axis
    planed = []
    for i in range(len(matrix)):
        planed.append([])
        for j in range(len(matrix[0])):  
            planed[i].append([])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0][0])):
                planed[i][j].append(matrix[k][j][i])
    #rotate the plan
    matrix = rotate_matz(planed, angle=angle)
    #map the plan to the matrix
    
    planed = []
    for i in range(len(matrix)):
        planed.append([])
        for j in range(len(matrix[0])):  
            planed[i].append([])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0][0])):
                planed[i][j].append(matrix[k][j][i])

    return planed


def rotate_maty(matrix, angle=10):
    #repeate for all layers in y axis
    #cteate a plan in y axis
    planed = []
    for i in range(len(matrix)):
        planed.append([])
        for j in range(len(matrix[0])):  
            planed[i].append([])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0][0])):
                planed[i][j].append(matrix[k][i][j]) 
    #rotate the plan
    matrix = rotate_matz(planed, angle=angle)
    #map the plan to the matrix
    planed = []
    for i in range(len(matrix)):
        planed.append([])
        for j in range(len(matrix[0])):  
            planed[i].append([])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0][0])):
                planed[i][j].append(matrix[j][k][i])
    return planed

def split_and_connect_16x16x16(array_16x16x16):
    # Separate layers of the 16x16x16 array
    layers = [np.array(array_16x16x16)[:, :, i] for i in range(len(array_16x16x16[0][0]))]

    # Divide each layer into 8x8 arrays A, B, C, D
    arrays_A = [layer[:8, :8] for layer in layers]
    arrays_B = [layer[:8, 8:] for layer in layers]
    arrays_C = [layer[8:, :8] for layer in layers]
    arrays_D = [layer[8:, 8:] for layer in layers]

    # Connect all the A, B, C, D matrices into one matrix with 8 columns and 128 rows
    connected_A_matrix = np.concatenate(arrays_A, axis=0)
    connected_B_matrix = np.concatenate(arrays_B, axis=0)
    connected_C_matrix = np.concatenate(arrays_C, axis=0)
    connected_D_matrix = np.concatenate(arrays_D, axis=0)

    # Reshape and convert to lists
    A_array = connected_A_matrix.reshape(16, 64)
    B_array = connected_B_matrix.reshape(16, 64)
    C_array = connected_C_matrix.reshape(16, 64)
    D_array = connected_D_matrix.reshape(16, 64)

    A = A_array.tolist()
    A = [item for sublist in A for item in sublist]
    B = B_array.tolist()
    B = [item for sublist in B for item in sublist]
    C = C_array.tolist()
    C = [item for sublist in C for item in sublist]
    D = D_array.tolist()
    D = [item for sublist in D for item in sublist]

    return A, B, C, D
#print(shift_matrix_bottom(ls, 1))