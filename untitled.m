T = readtable('toyz.csv'); % 推荐方式，适用于包含文本和数值的 CSV

%make can id 作为协议号
T(1,:)


regressionLearner(T, 'x__') % 'Price' 是目标变量