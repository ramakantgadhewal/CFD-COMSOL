clear
BL20 = load("BL20.txt");
P2P1 = load("P2P1.txt");
Xcoarse = load("Xcoarse.txt");
coarser = load("coarser.txt");
yplus=load("yplus.txt");
% DNS = load("9_Lab2_Pkplus_DNS_Retau395_Kim_etal_211028_1.txt");
import_DNS
DNS = DNS_table(:,2);
% yplus = yplus(:,2);
%%
close all 

% plot(Xcoarse(:,1), Xcoarse(:,2))
plot(yplus(:,2),Xcoarse(:,2))
hold on
plot(yplus(:,2),coarser(:,2))
plot(yplus(:,2),BL20(:,2))
plot(yplus(:,2),P2P1(:,2))
% plot(linspace(yplus(1),yplus(end),length(DNS)),50*DNS)
plot(DNS_table(:,1),50*DNS_table(:,2),'k','LineWidth',2)
% plot(DNS_table)
% plot(yplus(:,2),Xcoarse(:,2))

% legend.FontSize=16
legend("Xcoarse","Coarser","BL20","P2P1","DNS")

% figure
% plot(DNS_table(:,1),DNS_table(:,2))