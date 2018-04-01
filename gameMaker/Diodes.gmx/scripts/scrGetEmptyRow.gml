/// Find an empty row in the selected column.

col = argument0;
bottomRow = ds_grid_height(gameGrid) - 1;

// Iterate through the rows until an empty cell is found.
for (row = 0; row <= bottomRow; row++)
{
    if (ds_grid_get(gameGrid, col, row) != gridContents.empty)
    {
        return row - 1;
    }
}
return bottomRow;
