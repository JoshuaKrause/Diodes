/// Destroys the GameInit objects and buttons when a new game begins.

with (objGameInit)
{
    instance_destroy();
}

with (objNumberButton)
{
    instance_destroy();
}

show_debug_message("Init destroyed.");
