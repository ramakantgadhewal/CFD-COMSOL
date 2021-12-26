%% Import data from text file
% Script for importing data from the following text file:
%
%    filename: /home/henrik/Documents/umu/CFD/project/DNS_data/9_Lab2_uplus_DNS_Retau395_Kim_etal_211028_1.txt
%
% Auto-generated by MATLAB on 25-Dec-2021 14:50:56

%% Set up the Import Options and import the data
opts = delimitedTextImportOptions("NumVariables", 2);

% Specify range and delimiter
opts.DataLines = [2, Inf];
opts.Delimiter = "\t";

% Specify column names and types
opts.VariableNames = ["y", "U"];
opts.VariableTypes = ["double", "double"];

% Specify file level properties
opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";

% Import the data
kplusDNSRetau395Kimetal2110281 = readtable("/home/henrik/Documents/umu/CFD/project/DNS_data/9_Lab2_kplus_DNS_Retau395_Kim_etal_211028_1.txt", opts);

%% Convert to output type
kplusDNS = table2array(kplusDNSRetau395Kimetal2110281);

%% Clear temporary variables
clear opts
clear kplusDNSRetau395Kimetal2110281