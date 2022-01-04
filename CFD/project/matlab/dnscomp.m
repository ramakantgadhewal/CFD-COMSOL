clear 
close all
run import_uplus_dns.m
run import_kplus_dns.m
run import_epplus_dns.m
run import_Pkplus_dns.m
%%
close all 
figure 
max_val = max(uplusDNS(:,2));
plot(uplusDNS(:,1), uplusDNS(:,2)/max_val)
hold on 
grid on 

%%
% close all 
% figure 
max_val = max(kplusDNS(:,2));
plot(kplusDNS(:,1), kplusDNS(:,2)/max_val)
hold on 
grid on
%%
% close all 
% figure 
max_val = max(PkplusDNS(:,2));
plot(PkplusDNS(:,1), PkplusDNS(:,2)/max_val)
hold on 
grid on
%%
% close all 
% figure 
max_val = max(epplusDNS(:,2));
plot(epplusDNS(:,1), epplusDNS(:,2)/max_val)
hold on 
grid on
%%
legend("U+","k+","Pk+","ep+","Location","best")