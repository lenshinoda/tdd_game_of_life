from .cell import Cell

class Grid:

    def __init__(self, seed):
        self.seed = seed

    def calculate_neighbors(self, location):
        x = location[0]
        y = location[1]

        neighbors = 0 - self.seed[y][x]

        for i in [-1, 0, 1]:
            for j in [-1, 0 , 1]:
                try:
                    is_neighbor_alive = self.seed[y + i][x + j]
                except:
                    is_neighbor_alive = 0
                neighbors += is_neighbor_alive

        return neighbors

    def calculate_next_gen(self):
        nex_gen = []
        for i in range(len(self.seed)):
            nex_gen_y = []
            for j in range(len(self.seed[0])):
                cell = Cell(self.seed[i][j])
                neighbors = self.calculate_neighbors([j, i])
                cell.update_state(neighbors)
                nex_gen_y.append(cell.state)
            nex_gen.append(nex_gen_y)
        self.seed = nex_gen
