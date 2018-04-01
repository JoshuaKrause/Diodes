/// Draw the grid.

gridWidth = room_width - 100;
gridHeight = room_height - 100;

gridWidthMin = (room_width / 2) - (gridWidth / 2);
gridWidthMax = (room_width / 2) + (gridWidth / 2);

gridHeightMin = (room_height / 2) - (gridHeight / 2)
gridHeighMax = (room_height / 2) + (gridHeight / 2);

cellWidth = gridWidth / gridSize;
cellHeight = gridHeight / gridSize;

increment = 0;

for (i = 0; i < gridSize + 1; i++)
{
    draw_line(gridWidthMin, increment, gridWidthMax, increment);
    draw_line(increment, gridHightMin, increment, gridHeightMax);
    increment += cellWidth;
}
