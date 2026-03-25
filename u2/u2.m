clc
clear

%Face 1


%Draw graticule, gnomonic projection, normal aspect
umin = 30 * pi / 180;
umax = 90 * pi / 180;
vmin = -180 * pi / 180;
vmax = 180 * pi / 180;
Du = 10 * pi/180;
Dv = Du;
du = pi/180;
dv = du;
R = 1;
uk = 90*pi/180;
vk = 0;
u0 = pi/4;
proj = @gnom 
ub = 35.2644 *pi/180;
vb1 = 0;
vb2 = pi/2;
vb3 = pi;
vb4 = 3/2*pi;
conts = {'v:\Bayer\mk_2025_26\u2\continents_points\amer.txt', ...
         'v:\Bayer\mk_2025_26\u2\continents_points\anta.txt', ...
         'v:\Bayer\mk_2025_26\u2\continents_points\austr.txt', ...
         'v:\Bayer\mk_2025_26\u2\continents_points\eur.txt'};

uv = [umin, umax, vmin, vmax];

createGlobeFace(uv, steps, R, uk, vk, s0, proj, conts, ub, vb)

hold on
axis equal
plot(XM, YM);
plot(XP, YP);

%Draw graticule, gnomonic projection, transverse aspect
umin = -45 * pi / 180;
umax = 45 * pi / 180;
vmin = -180 * pi / 180;
vmax = 180 * pi / 180;
Du = 10 * pi/180;
Dv = Du;
du = pi/180;
dv = du;
R = 1;
uk = 0;
vk = pi/2;
u0 = pi/4;
proj = @gnom 

[XM, YM, XP, YP] = graticule(umin, umax, vmin, vmax, Du, Dv, du, dv, R, uk, vk, u0, proj);

hold on
axis equal
plot(XM, YM);
plot(XP, YP);





