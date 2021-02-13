# fastCubicBezier
Calculate Bezier points using the forward difference method.
This method is way faster than the standard formular (0.3s for 10^6 points vs. 2s with standard formular).

Read a detail explaination here: https://www.drdobbs.com/forward-difference-calculation-of-bezier/184403417?pgno=1

Use

*x, y = fastCubicBezier.universal(Startpoint_X, Startpoint_Y, Endpoint_X, Endpoinnt_Y, Handle1_X, Handle1_Y, Handle2_X, Handle2_Y, Resolution)*

for any kind of Bezier.

Use

*x,y = fastCubicBezier.transition(Handle1_X, Handle1_Y, Handle2_X, Handle2_Y, Resolution)*

if Startpoint is 0 and Endpoint is 1, usually when Bezier is used for animated transistions.
