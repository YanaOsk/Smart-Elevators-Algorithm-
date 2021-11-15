class CallForElevator:
    def __init__(self,elv:str,time:float,src:int,dest:int,elv_pos:int,alloc:int):
        self.elv = elv
        self.time = time
        self.src = src
        self.dest = dest
        self.elv_pos = elv_pos
        self.alloc = alloc

    def __str__(self):
        return f"{self.elv} {self.time} {self.src} {self.dest} {self.elv_pos} {self.alloc}"

    def __repr__(self):
        return f"{self.elv} {self.time} {self.src} {self.dest} {self.elv_pos} {self.alloc}"