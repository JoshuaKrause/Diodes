/// Resize tile.

if sprite_width != objGameBoard.cellWidth
{
    image_xscale = objGameBoard.cellWidth/sprite_width;
}

if sprite_height != objGameBoard.cellHeight
{
    image_yscale = objGameBoard.cellHeight/sprite_height;
}
