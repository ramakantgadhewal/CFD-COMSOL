clear all
%Design of wind tunnel contraction shape based on the following two papers:
% [1] "Design and calibration of a wind tunnel with a two dimensional
% contraction", J.E. Sargison, G.J. Walker and R. Rossi, 2004
% [2] "Flow characteristics in low-speed wind tunnel contractions: Simulation and
% testing", Alexandria Engineering Journal (2018) 57
% Following [1] a sixth orde polynom is chosen as shape model for a
% 2D-contraction with inlet crossection Di*W, outlet crossection Do*W:
% y=a*x^6+b*x^5+c*x^4+d*x^3+e*x^2+f*x+g
% From [2] the recommendation of contraction number CR is between 6-12
% and the contraction length L is between 0.75*Di and 1.25*Di
% CR is chosen to 5, i.e. CR=(Di*W)/(Do*W)=5
% and the contraction length is chosen to L=Di
% Model 3 in [1] is chosen, i.e xi/L=0.6 and alpha=0, where xi is the
% inflexion point along contraction axis and alpha is the inlet curvature.
CR=7;
Do=0.050; %50mm
Di=sqrt(Do^2*CR);
L=1.0*Di;
xi=0.6*L;
h=1*(Di/2-Do/2);
% The constratints on the shape model is the following:
% x=0: y(0)=h, y'(0)=0, y''(0)=0
% x=L: y(L)=0, y'(L)=0, y''(L)=0
% x=xi: y''(xi)=0
% When the constraints are applied we obtain a system of equations
% for the coefficients a,b,c,d in terms of L and xi, and that g=h, f=e=0.
% The system looks like Asys*Coeff=B:
Asys=[30*xi^4 20*xi^3 12*xi^2 6*xi;
L^6 L^5 L^4 L^3;
6*L^5 5*L^4 4*L^3 3*L^2;
30*L^4 20*L^3 12*L^2 6*L];
B=[0 -h 0 0]';
Coeff=linsolve(Asys,B);
a=Coeff(1); b=Coeff(2); c=Coeff(3); d=Coeff(4); e=0; f=0;g=h;
%Contraction shape model from [1]
x=[0:0.001:L];
y=a*x.^6+b*x.^5+c*x.^4+d*x.^3+e*x.^2+f*x+g;
%Plot shape
figure(1)
hold on
plot(x,y+Do/2,'b')
plot(x,-y-Do/2,'b')
xlabel('x'); ylabel('y'); axis equal
title(['CR=', num2str(CR), ', L/Di=',num2str(L/Di)])