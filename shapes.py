


class Shape:
    def __init__(self, number):
        grid = []
        lst = [0] * 4
        for i in range(10):
            grid.append(lst)
            self.shape = grid
        
        # Shapes: I, S, Z, J, L, T, O
        if number==0:
            self.shape[3][3] = 1
            self.shape[4][3] = 1
            self.shape[5][3] = 1
            self.shape[6][3] = 1
        elif number==1:
            self.shape[3][1] = 1
            self.shape[3][2] = 1
            self.shape[4][2] = 1
            self.shape[5][3] = 1
        elif number==2:
            self.shape[4][1] = 1
            self.shape[4][2] = 1
            self.shape[4][3] = 1
            self.shape[5][3] = 1
        elif number==3:
            self.shape[4][2] = 1
            self.shape[3][3] = 1
            self.shape[4][3] = 1
            self.shape[5][3] = 1            
        elif number==4:
            self.shape[4][2] = 1
            self.shape[4][2] = 1
            self.shape[5][3] = 1
            self.shape[5][3] = 1   
