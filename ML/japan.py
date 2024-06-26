import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Input
from keras.callbacks import EarlyStopping, ModelCheckpoint
import os

# 엔화 환율 데이터 수집
ticker = 'JPY=X'
start_date = '2010-01-01'
end_date = '2024-06-21'
df = yf.download(ticker, start=start_date, end=end_date)

# 데이터 전처리
data = df['Close'].values
data = data.reshape(-1, 1)

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# 학습 데이터 준비
train_size = int(len(scaled_data) * 0.8)
train_data = scaled_data[:train_size]
test_data = scaled_data[train_size:]

def create_dataset(data, time_step=60):
    X, y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 0])
    return np.array(X), np.array(y)

time_step = 60
X_train, y_train = create_dataset(train_data, time_step)
X_test, y_test = create_dataset(test_data, time_step)

# 입력 데이터의 형태 조정 [samples, time steps, features]
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# LSTM 모델 생성
model = Sequential([
    Input(shape=(time_step, 1)),
    LSTM(100, return_sequences=True),
    Dropout(0.3),
    LSTM(100, return_sequences=False),
    Dropout(0.3),
    Dense(50),
    Dense(1)
])

# 모델 컴파일
model.compile(optimizer='adam', loss='mean_squared_error')

# 모델 체크포인트 저장 경로 설정
checkpoint_path = 'best_model.keras'
checkpoint_dir = os.path.dirname(checkpoint_path)

# 조기 종료와 모델 체크포인트 설정
early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
model_checkpoint = ModelCheckpoint(filepath=checkpoint_path, monitor='val_loss', save_best_only=True)

# 모델 학습
model.fit(X_train, y_train, batch_size=32, epochs=100, validation_split=0.2, callbacks=[early_stop, model_checkpoint])

# 모델 로드 (최적의 성능을 낸 모델)
model.load_weights(checkpoint_path)

# 예측
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# 데이터 역변환
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)
y_train = scaler.inverse_transform(y_train.reshape(-1, 1))
y_test = scaler.inverse_transform(y_test.reshape(-1, 1))

# 성능 평가
train_mse = mean_squared_error(y_train, train_predict)
test_mse = mean_squared_error(y_test, test_predict)
train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)
train_mae = mean_absolute_error(y_train, train_predict)
test_mae = mean_absolute_error(y_test, test_predict)

print(f'Train MSE: {train_mse}, Train RMSE: {train_rmse}, Train MAE: {train_mae}')
print(f'Test MSE: {test_mse}, Test RMSE: {test_rmse}, Test MAE: {test_mae}')

# 미래 예측
def predict_future(model, data, steps):
    future_data = data[-time_step:]
    predictions = []
    for _ in range(steps):
        X = future_data.reshape(1, time_step, 1)
        pred = model.predict(X)
        predictions.append(pred[0, 0])
        future_data = np.append(future_data[1:], pred)
    return scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

# 미래 30일 예측
future_days = 30
future_predictions = predict_future(model, scaled_data, future_days)

# 예측 결과 시각화
plt.figure(figsize=(14, 7))
plt.plot(df.index, data, color='blue', label='Real JPY/USD Exchange Rate')
train_predict_plot = np.empty_like(data)
train_predict_plot[:, :] = np.nan
train_predict_plot[time_step:len(train_predict) + time_step, :] = train_predict

test_predict_plot = np.empty_like(data)
test_predict_plot[:, :] = np.nan
test_predict_plot[len(train_predict) + (time_step * 2) + 1:len(data) - 1, :] = test_predict

plt.plot(df.index, train_predict_plot, color='green', label='Train Predict')
plt.plot(df.index, test_predict_plot, color='red', label='Test Predict')

# 미래 예측 데이터 추가
last_date = df.index[-1]
future_dates = pd.date_range(last_date, periods=future_days + 1).tolist()
plt.plot(future_dates[1:], future_predictions, color='orange', label='Future Predictions')

plt.title('JPY/USD Exchange Rate Prediction using LSTM')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.show()
