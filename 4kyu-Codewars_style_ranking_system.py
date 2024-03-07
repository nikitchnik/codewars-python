class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
    
    def inc_progress(self, rank):
        if rank < -8 or rank == 0 or 8 < rank:
            raise
        
        diff = rank - (rank > 0) - self.rank + (self.rank > 0)
        if diff < -1:
            return
        
        self.progress += {-1:1, 0:3}.get(diff, 10 * diff ** 2)
        while self.progress >= 100 and self.rank < 8:
            self.progress -= 100
            self.rank += 1 + (self.rank == -1)
        
        if self.rank == 8:
            self.progress = 0
