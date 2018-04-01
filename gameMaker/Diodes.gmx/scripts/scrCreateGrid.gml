/// Create our grid.

gridSize = argument0;

// Set up the player enum.
enum gridContents 
{
    empty,
    red,
    green
}

// The default first player is red.
currentPlayer = gridContents.red;

// Create a ds_grid and populate it with empty entries.
gameGrid = ds_grid_create(gridSize, gridSize);

i = 0;
j = 0;
repeat (ds_grid_width(gameGrid))
{
   repeat (ds_grid_height(gameGrid))
      {
      ds_grid_set(gameGrid, i, j, gridContents.empty); 
      j += 1;
      }
   j = 0;
   i += 1;
}




