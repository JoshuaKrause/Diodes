/// Place a tile in the selected grid column.

// Determine the grid coordinates based on the current mouse location.
x_coord = floor(mouse_x / cellWidth);
y_coord = floor(mouse_y / cellHeight);

// Check to see if the column is empty.
if (!scrCheckColumn(x_coord, y_coord))
{   
    show_debug_message("Contents not empty.");
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
instance_create(x, y, tile);
//show_debug_message(string(x_coord) + ", " + string(y_coord))

// Switch the player.
scrSwitchPlayer();
scrOutputGrid();
