/// Move the tile to its final position.

if point_distance(x, y, x_coord, y_coord) > 0.001
   {
   move_towards_point(x_coord, y_coord, 50);
   }
else speed = 0;
