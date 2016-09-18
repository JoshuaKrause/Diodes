/// Place a tile in the selected grid column.

// Determine the grid coordinates based on the current mouse location.
x_coord = floor(mouse_x / cellWidth);

// Check to see if the column is empty.
y_coord = scrGetEmptyRow(x_coord);

if (y_coord < 0)
{   
    show_debug_message("Column full.");
    exit;
}

// Place the tile in the ds_grid.
ds_grid_set(gameGrid, x_coord, y_coord, currentPlayer);
show_debug_message("New tile:" + string(ds_grid_get(gameGrid, x_coord, y_coord)));

// Find the center of the selected cell and create an instance of the player's tile.
x = x_coord * cellWidth + (cellWidth * .5);
y = y_coord * cellHeight + (cellHeight * .5);

if (currentPlayer == gridContents.red)
{
    tile = objRedTile;
}
else
{
    tile = objGreenTile;
}

newTile = instance_create(x, 0 - cellWidth - (cellWidth * .5), tile);

newTile.x_coord = x;
newTile.y_coord = y;

//show_debug_message(string(x_coord) + ", " + string(y_coord))

// Switch the player.
scrSwitchPlayer();

// Output the grid for debugging.
scrOutputGrid();
