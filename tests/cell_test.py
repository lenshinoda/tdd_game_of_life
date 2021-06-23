from game.cell import Cell

def test_cell_state_can_be_dead_or_alive():
    state = 0
    dead_cell = Cell(state)
    state = 1
    alive_cell = Cell(state)

    assert dead_cell.state == 0
    assert alive_cell.state == 1