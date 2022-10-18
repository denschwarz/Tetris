class Piece:
    def __init__(self, shape_nr):
        self.shape = shape_nr
        # Shape: I
        if self.shape == 0:
            self.pos = [(3,0), (4,0), (5,0), (6,0)]
            self.color = (255,20,20)
        # Shape: S
        elif self.shape == 1:
            self.pos = [(3,-2), (3,-1), (4,-1), (4,0)]
            self.color = (20,255,20)
        # Shape: Z
        elif self.shape == 2:
            self.pos = [(3,0), (3,-1), (4,-1), (4,-2)]
            self.color = (20,20,255)
        # Shape: L
        elif self.shape == 3:
            self.pos = [(4,0), (3,0), (3,-1), (3,-2)]
            self.color = (255,255,20)
        # Shape: J
        elif self.shape == 4:
            self.pos = [(3,0), (4,0), (4,-1), (4,-2)]
            self.color = (20,255,255)
        # Shape: T
        elif self.shape == 5:
            self.pos = [(3,0), (4,0), (5,0), (4,-1)]
            self.color = (100,20,200)
        # Shape: O
        elif self.shape == 6:
            self.pos = [(3,0), (4,0), (4,-1), (3,-1)]
            self.color = (200,255,100) 
        self.lastpos = self.pos    
            

    def fall(self, N=1):
        self.lastpos = self.pos
        x1,y1 = self.pos[0]
        x2,y2 = self.pos[1]
        x3,y3 = self.pos[2]
        x4,y4 = self.pos[3]
        self.pos = [(x1,y1+N), (x2,y2+N), (x3,y3+N), (x4,y4+N)]

    def move(self, dir):
        self.lastpos = self.pos
        x1,y1 = self.pos[0]
        x2,y2 = self.pos[1]
        x3,y3 = self.pos[2]
        x4,y4 = self.pos[3]
        self.pos = [(x1+dir,y1), (x2+dir,y2), (x3+dir,y3), (x4+dir,y4)]        

                    
    def undo_move(self):
        self.pos = self.lastpos
        
    def rotate(self):
        if self.shape==6:
            return
        # Always rotate around self.pos[1]
        x1,y1 = self.pos[0]
        x2,y2 = self.pos[1]
        x3,y3 = self.pos[2]
        x4,y4 = self.pos[3]
        for i, (x,y) in enumerate(self.pos):
            dx = x - x2 
            dy = y - y2
            newdx = -dy
            newdy = dx
            self.pos[i] = (x2+newdx,y2+newdy)
        self.adjust_rotated_position()
        
    def adjust_rotated_position(self):
        x1,y1 = self.pos[0]
        x2,y2 = self.pos[1]
        x3,y3 = self.pos[2]
        x4,y4 = self.pos[3]
        xmin = 10
        xmax = -1
        for (x,y) in self.pos:
            if x > xmax:
                xmax = x 
            if x < xmin:
                xmin = x 
        if xmin < 0:
            self.pos = [(x1-xmin,y1), (x2-xmin,y2), (x3-xmin,y3), (x4-xmin,y4)] 
        if xmax > 9: 
            self.pos = [(x1+xmin,y1), (x2+xmin,y2), (x3+xmin,y3), (x4+xmin,y4)] 

    
        
        
