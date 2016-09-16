switch(image_index)
{
    case 0:
        objGameInit.gridSize = 8;
        break;
    case 1:
        objGameInit.gridSize = 16;
        break;
    case 2:
        objGameInit.gridSize = 32;
        break;
}

instance_create(0,0,objGameBoard);
scrDestroyGameInit();
