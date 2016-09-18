// Create grid size selection buttons.

height = room_height * .5 + 50;

button0 = instance_create(room_width * .5 - 64, height, objNumberButton);
button0.image_speed = 0;
button0.image_index = 0;

button1 = instance_create(room_width * .5, height, objNumberButton);
button1.image_speed = 0;
button1.image_index = 1;

button2 = instance_create(room_width * .5 + 64, height, objNumberButton);
button2.image_speed = 0;
button2.image_index = 2;
