/// Create a red tile.

x_coord = floor(mouse_x / cellWidth);
y_coord = floor(mouse_y / cellHeight);

x = x_coord * cellWidth + (cellWidth * .5);
y = y_coord * cellHeight + (cellHeight * .5);

instance_create(x, y, objRedTile);
show_debug_message(string(x_coord) + ", " + string(y_coord))
