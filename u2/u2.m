clc
clear

%Conversion
u = [49, 50, 51] * pi / 180;
v = [14, 15, 16] * pi / 180;
uk = 60 * pi /180;
vk = 20 * pi / 180;

[s,d] = uvTosd(u, v, uk, vk);

%Draw graticule, gnomonic projection
umin = 20 * pi / 180;
umax = 90 * pi / 180;
vmin = -180 * pi / 180;
vmax = 180 * pi / 180;
Du = 10 * pi/180;
Dv = Du;
du = pi/180;
dv = du;
R = 1;
uk = pi/2;
vk = 0;
u0 = pi/4;
proj = @gnom 

[XM, YM, XP, YP] = graticule(umin, umax, vmin, vmax, Du, Dv, du, dv, R, uk, vk, u0, proj);

hold on
plot(XM, YM);
%plot(XP, YP);





