/// Draw the grid.

increment = cellWidth;
for (i = 0; i < gridSize; i++)
{
    draw_line(0, increment, room_width, increment);
    draw_line(increment, 0, increment, room_height);
    increment += cellWidth;
}
