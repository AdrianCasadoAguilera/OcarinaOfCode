import maps, math, data

def e_position(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if(mat[i][j]=="E"):
                input(f"i: {i}, j: {j}")