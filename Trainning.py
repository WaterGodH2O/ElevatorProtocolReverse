import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
def Train(output,input,verbose):
    X = input
    y = output

    # 训练模型
    model = LinearRegression()
    model.fit(X, y)

    # 预测
    y_pred = model.predict(X)

    # 输出回归系数
    print("截距:", model.intercept_)

    weights = model.coef_.ravel()  # 或者 model.coef_.flatten()

    print("========================准确度========================")
    r2 = model.score(X, y)
    print("Coefficient of Determination:", r2)

    # 如果需要更多评价指标，可以自行计算
    # 例如均方误差 MSE、均方根误差 RMSE 等
    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)
    print("MSE:", mse)
    print("RMSE:", rmse)
    print("=====================================================")
    if verbose:
        for i, weight in enumerate(weights):
            byte_index = i // 8  # 计算 ByteX
            bit_index = i % 8  # 计算 bitY
            print(f"Byte{byte_index}bit{bit_index}: {weight}")
    else:
        for i, weight in enumerate(weights):
            byte_index = i // 8  # 计算 ByteX
            bit_index = i % 8  # 计算 bitY
            if (abs(weight) > 0.001):
                print(f"Byte{byte_index}bit{bit_index}: {weight}")
    print("=====================================================")