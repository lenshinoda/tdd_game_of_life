from game.cell import Cell
import pytest

def test_cell_state_can_be_dead_or_alive():
    state = 0
    dead_cell = Cell(state)
    state = 1
    alive_cell = Cell(state)

    assert dead_cell.state == 0
    assert alive_cell.state == 1

def test_cell_should_raise_an_exception_if_invalid_state():
    state = 3

    with pytest.raises(Exception) as e_info:
        Cell(state)
    
    assert e_info.value.args[0] == 'Invalid state'


# Any live cell with fewer than two live neighbors dies, as if by underpopulation.
def test_a_live_cell_should_die_if_less_than_two_cells_are_alive():
    live_cell_with_1_neighbor = Cell(1)
    live_cell_with_2_neighbor = Cell(1)

    live_cell_with_1_neighbor.update_state(0)
    live_cell_with_2_neighbor.update_state(1)

    assert live_cell_with_1_neighbor.state == 0
    assert live_cell_with_2_neighbor.state == 0

# Any live cell with two or three live neighbors lives on to the next generation.
def test_a_live_cell_should_keep_alive_if_2_or_3_live_neighbors():
    live_cell_with_2_neighbor = Cell(1)
    live_cell_with_3_neighbor = Cell(1)

    live_cell_with_2_neighbor.update_state(2)
    live_cell_with_3_neighbor.update_state(3)

    assert live_cell_with_2_neighbor.state == 1
    assert live_cell_with_3_neighbor.state == 1

# Any live cell with more than three live neighbors dies, as if by overpopulation.
def test_a_live_cell_should_die_if_more_than_3_live_neighbors():
    live_cell_with_4_neighbor = Cell(1)

    live_cell_with_4_neighbor.update_state(4)

    assert live_cell_with_4_neighbor.state == 0

# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
def test_a_dead_cell_should_live_if_exactly_3_live_neighbors():
    dead_cell_with_3_live_neighbor = Cell(0)

    dead_cell_with_3_live_neighbor.update_state(3)

    assert dead_cell_with_3_live_neighbor.state == 1