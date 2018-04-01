/// Checks to see if the most recent move created a win condition.

var row = argument0;
var col = argument1;

var currentCell, previousCell, winCount;

var winCondition = 4;
var winner = false;

previousCell = gridContents.empty;
winCount = 0;

// Check horizontal.
// Iterate through the grid from left to right until enough consecutive tiles
// are found to trip the win condition.
for(i = 0; i < ds_grid_width(gameGrid); i++)
{
    currentCell = ds_grid_get(gameGrid, i, col);
    if (currentCell == gridContents.empty)
    {
        continue;
    }
    if (currentCell != previousCell)
    {
        winCount = 1;
        previousCell = currentCell;
    }
    else
    {
        winCount += 1;
    }
    if (winCount == winCondition)
    {
        winner = true;
        break;
    }
}

// Check vertical if no horizontal win detected.
if(!winner)
{
    previousCell = gridContents.empty;
    winCount = 0;
    
    // Iterate through the grid from top to bottom until enough consecutive tiles
    // are found to trip the win condition.
    for(i = 0; i < ds_grid_height(gameGrid); i++)
    {
        currentCell = ds_grid_get(gameGrid, row, i);
        if (currentCell == gridContents.empty)
        {
            continue;
        }
        if (currentCell != previousCell)
        {
            winCount = 1;
            previousCell = currentCell;
        }
        else
        {
            winCount += 1;
        }
        if (winCount == winCondition)
        {
            winner = true;
            break;
        }
    }
}

// Check diagonal (top-left to bottom-right) if no horizontal or vertical win detected.
if(!winner)
{
    var previousCell = gridContents.empty;
    var winCount = 0;
    
    // Find the top-left-most tile from the current move.
    var x_coord, y_coord;
    
    x_coord = col;
    y_coord = row;
    
    while (x_coord > 0 && y_coord > 0)
    {   
        x_coord--;
        y_coord--;
    }
    //show_debug_message(string(x_coord) +", "+ string(y_coord));
    //show_debug_message("Found top-left cell.");
    
    var previousCell = gridContents.empty;
    var winCount = 0;
    
    // Iterate through the grid from top-left to bottom-right until enough consecutive tiles
    // are found to trip the win condition.
    while(x_coord < ds_grid_width(gameGrid) && y_coord < ds_grid_height(gameGrid))
    {
        var currentCell = ds_grid_get(gameGrid, y_coord, x_coord);
        if (currentCell == gridContents.empty)
        {
            x_coord++;
            y_coord++;
            continue;
        }
        if (currentCell != previousCell)
        {
            winCount = 1;
            previousCell = currentCell;
        }
        else
        {
            winCount += 1;
        }
        //show_debug_message("Win count: "+ string(winCount));
        if (winCount == winCondition)
        {
            winner = true;
            break;
        }
        x_coord++;
        y_coord++;
    }
}

// Check diagonal (bottom-left to top-right) if no horizontal or vertical win detected.
if(!winner)
{
    var previousCell = gridContents.empty;
    var winCount = 0;
    
    // Find the bottom-left-most tile from the current move.
    var x_coord, y_coord;
    
    x_coord = col;
    y_coord = row;
    
    while (x_coord > 0 && y_coord < ds_grid_height(gameGrid) - 1)
    {   
        x_coord--;
        y_coord++;
    }
    
    var previousCell = gridContents.empty;
    var winCount = 0;
    
    // Iterate through the grid from top-left to bottom-right until enough consecutive tiles
    // are found to trip the win condition.
    while(x_coord < ds_grid_width(gameGrid) && y_coord > 0)
    {
        var currentCell = ds_grid_get(gameGrid, y_coord, x_coord);
        if (currentCell == gridContents.empty)
        {
            x_coord++;
            y_coord--;
            continue;
        }
        if (currentCell != previousCell)
        {
            winCount = 1;
            previousCell = currentCell;
        }
        else
        {
            winCount += 1;
        }
        if (winCount == winCondition)
        {
            winner = true;
            break;
        }
        x_coord++;
        y_coord--;
    }
}

return winner;


