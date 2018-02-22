    def collide(self, other):
        offset = list((other.rect[0] - self.rect[0], other.rect[1] - self.rect[1]))
 
    return self.mask.overlap_area(other.mask, offset) != 0