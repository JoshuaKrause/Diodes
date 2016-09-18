/// Outputs the current state of the grid to a text file.
var file;
file = file_text_open_write(working_directory + "/gridOutput.txt");

j = 0;
i = 0;

repeat(ds_grid_width(gameGrid))
{
    repeat(ds_grid_height(gameGrid))
    {        
        file_text_write_string(file, "| "+ string(ds_grid_get(gameGrid, i, j))+" |");
        j += 1;
    }
    file_text_writeln(file);
    j = 0;
    i += 1;
}

file_text_close(file);
