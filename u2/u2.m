clc
clear

u = [49, 50, 51] * pi / 180;
v = [14, 15, 16] * pi / 180;
uk = 60 * pi /180;
vk = 20 * pi / 180;

[s,d] = uvTosd(u, v, uk, vk);
