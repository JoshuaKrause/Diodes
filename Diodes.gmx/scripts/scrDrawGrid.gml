/// Draw the grid.

cellWidth = room_width / gridSize;
cellHeight = room_height / gridSize;

increment = 0;

for (i = 0; i < gridSize + 1; i++)
{
    draw_line(0, increment, room_width, increment);
    draw_line(increment, 0, increment, room_height);
    increment += cellWidth;
}
