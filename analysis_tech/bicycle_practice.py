import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

train = pd.read_csv('./train.csv', encoding='utf-8')
train.head()

test = pd.read_csv('./test.csv', encoding='utf-8')
test.head()

## 결측치를 확인하고 결측치 채우기 (simple imputer 이용)
train.info()
train.isnull().sum()
train[train['hour_bef_pm2.5'].isnull()]

from sklearn.impute import SimpleImputer
si = SimpleImputer(strategy='mean')
imputed_df = si.fit_transform(train)
train = pd.DataFrame(imputed_df, columns = train.columns)
train.isnull().sum()

test.info()
test.isnull().sum()
test[test['hour_bef_pm2.5'].isnull()]

si = SimpleImputer(strategy='mean')
imputed_df2 = si.fit_transform(test)
test = pd.DataFrame(imputed_df2, columns = test.columns)
test.isnull().sum()

## 컬럼간 상관관계 확인하기
train.corr()
train.corr()[np.abs(train.corr())>=0.3]
sns.heatmap(train.corr()[np.abs(train.corr())>=0.3], annot=True)

test.corr()
test.corr()[np.abs(test.corr())>=0.3]
sns.heatmap(test.corr()[np.abs(test.corr())>=0.3], annot=True)

'''
train에서는 id는 상관관계가 없기 때문에 삭제하고 진행 
강수량은 상관관계가 낮으나 test에서는 상관관계가 존재하므로 삭제 안함
test는 id만 삭제하고 진행
'''

X_train = train.drop(columns=['id', 'count'], axis=1)
y_train = train['count']

print(X_train.shape, y_train.shape)

X_test = test.drop(columns=['id'], axis=1)
print(X_test.shape)

### 앙상블 모델링 진행하기
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
import lightgbm as lgb
from sklearn.metrics import *
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

abc = AdaBoostRegressor(random_state=100)
gbc = GradientBoostingRegressor(random_state=100)
rf = RandomForestRegressor(random_state=100, booster='gbtree')
xgb = xgb.XGBRegressor(random_state=100, booster='gbtree')
lgb = lgb.LGBMRegressor(random_state=100, booster='gbtree', boosting_type = 'gbdt')

######### 
param_grid_abc = {
    'n_estimators': [1, 10, 50, 100],
    'loss': ['linear', 'square', 'exponential'],
    'learning_rate': [0, 0.1, 0.2, 0.5, 0.8, 1.0],
}

grid_search_abc = GridSearchCV(abc, param_grid=param_grid_abc, cv=10, n_jobs=-1)
grid_search_abc.fit(X_train, y_train)
print(grid_search_abc.best_estimator_) #AdaBoostRegressor(learning_rate=0.1, n_estimators=100, random_state=100)
best_param_abc_gs = grid_search_abc.best_estimator_
pred_abc_gs = best_param_abc_gs.predict(X_test)

random_search_abc = RandomizedSearchCV(abc, param_grid_abc, n_iter=30, cv = 10, n_jobs=-1, scoring = 'neg_mean_squared_error')
random_search_abc.fit(X_train, y_train)
print(random_search_abc.best_estimator_) #AdaBoostRegressor(learning_rate=0.1, n_estimators=100, random_state=100)
best_param_abc_rs = random_search_abc.best_estimator_
pred_abc_rs = best_param_abc_rs.predict(X_test)

sns.kdeplot(pred_abc_gs, label = 'grid_pred')
sns.kdeplot(pred_abc_rs, label = 'rand_pred')
plt.legend()
plt.show()

print(best_param_abc_rs.score(X_train, y_train)) #0.7338069755742368

col_imp1 = pd.DataFrame(best_param_abc_gs.feature_importances_, index = X_train.columns, columns = ['value']).sort_values(by='value', ascending=False)
plt.figure(figsize=(10,10))
sns.barplot(col_imp1.index, col_imp1['value'])
plt.xticks(rotation=45)

######### 
param_grid_rf = {
    'max_depth': [None, 1, 10, 15, 20],
    'max_leaf_nodes': [2],
    'criterion':["mse"],
    'n_estimators': [1, 10, 50, 100, 150, 200],
    'min_samples_split':[2,3,4,8,10],
}
param_grid_rf = GridSearchCV(rf, param_grid=param_grid_rf, cv=10, n_jobs=-1)
param_grid_rf.fit(X_train, y_train)
print(param_grid_rf.best_estimator_) #RandomForestRegressor(max_leaf_nodes=2, n_estimators=150, random_state=100)
best_param_rf_gs = param_grid_rf.best_estimator_
pred_rf_gs = best_param_rf_gs.predict(X_test)

'''
random_search_rf = RandomizedSearchCV(rf, param_grid_rf, n_iter=30, cv = 10, n_jobs=-1, scoring = 'neg_mean_squared_error')
random_search_rf.fit(X_train, y_train)
print(random_search_rf.best_estimator_)
best_param_rf_rs = random_search_rf.best_estimator_
pred_rf_rs = best_param_rf_rs.predict(X_test)'''

sns.kdeplot(pred_rf_gs, label = 'grid_pred')
sns.kdeplot(pred_rf_rs, label = 'rand_pred')
plt.legend()
plt.show()

print(rf.fit(X_train, y_train).score(X_train, y_train))  #0.97125328407911

col_imp2 = pd.DataFrame(best_param_rf_gs.feature_importances_, index = X_train.columns, columns = ['value']).sort_values(by='value', ascending=False)
plt.figure(figsize=(10,10))
sns.barplot(col_imp2.index, col_imp2['value'])
plt.xticks(rotation=45)

#########
param_grid_gbc = {
    'n_estimators': [1, 10, 50, 100],
    'learning_rate': [0, 0.1, 0.2, 0.5, 0.8, 1.0],
    'criterion':["mse"],
    'max_depth':[None, 10, 20, 30, 50],
    'min_samples_split':[2,3,4,8,10],
}

param_grid_gbc = GridSearchCV(gbc, param_grid=param_grid_gbc, cv=10, n_jobs=-1)
param_grid_gbc.fit(X_train, y_train)
print(param_grid_gbc.best_estimator_) #GradientBoostingRegressor(criterion='mse', max_depth=10, min_samples_split=10, random_state=100)
best_param_gbc_gs = param_grid_gbc.best_estimator_ 
pred_gbc_gs = best_param_gbc_gs.predict(X_test)

'''
random_search_gbc = RandomizedSearchCV(gbc, param_grid_gbc, n_iter=30, cv = 10, n_jobs=-1, scoring = 'neg_mean_squared_error')
random_search_gbc.fit(X_train, y_train)
print(random_search_gbc.best_estimator_)
best_param_gbc_rs = random_search_gbc.best_estimator_
pred_gbc_rs = best_param_gbc_rs.predict(X_test)'''

sns.kdeplot(pred_gbc_gs, label = 'grid_pred')
sns.kdeplot(pred_gbc_rs, label = 'rand_pred')
plt.legend()
plt.show()

col_imp3 = pd.DataFrame(best_param_gbc_gs.feature_importances_, index = X_train.columns, columns = ['value']).sort_values(by='value', ascending=False)
plt.figure(figsize=(10,10))
sns.barplot(col_imp3.index, col_imp3['value'])
plt.xticks(rotation=45)

print(best_param_gbc_gs.score(X_train, y_train)) #0.9994846712235719

######### """
param_grid_xgb = {
    'max_depth': [None, 1, 10, 15, 20],
    'n_estimators': [1, 10, 50, 100],
#    'alpha': [0.001, 0.01, 0.1, 1],
#    'lambda': [0.001, 0.01, 0.1, 1],
    'learning_rate': [0, 0.1, 0.2, 0.5, 0.8, 1.0],
}
param_grid_xgb = GridSearchCV(xgb, param_grid=param_grid_xgb, cv=10, n_jobs=-1)
param_grid_xgb.fit(X_train, y_train)
print(param_grid_xgb.best_estimator_)
best_param_xgb_gs = param_grid_xgb.best_estimator_
pred_xgb_gs = best_param_xgb_gs.predict(X_test)
'''
random_search_xgb = RandomizedSearchCV(xgb, param_grid_xgb, n_iter=30, cv = 10, n_jobs=-1, scoring = 'neg_mean_squared_error')
random_search_xgb.fit(X_train, y_train)
print(random_search_xgb.best_estimator_)
best_param_xgb_rs = random_search_xgb.best_estimator_
pred_xgb_rs = best_param_xgb_rs.predict(X_test)'''

sns.kdeplot(pred_xgb_gs, label = 'grid_pred')
sns.kdeplot(pred_xgb_rs, label = 'rand_pred')
plt.legend()
plt.show()

col_imp4 = pd.DataFrame(best_param_xgb_gs.feature_importances_, index = X_train.columns, columns = ['value']).sort_values(by='value', ascending=False)
plt.figure(figsize=(10,10))
sns.barplot(col_imp4.index, col_imp4['value'])
plt.xticks(rotation=45)

#from xgboost import plot_importance
#plot_importance(param_grid_xgb.fit(X_train, y_train))

print(best_param_xgb_gs.score(X_train, y_train)) #0.9708202535661757

#########
param_grid_lgb = {
    'max_depth': [-1, 1, 5, 10, 15, 20],
    'n_estimators': [1, 9, 10, 50, 100],
#    'alpha': [0.001, 0.01, 0.1, 1],
#    'lambda': [0.001, 0.01, 0.1, 1],
    'learning_rate': [0.1, 0.2, 0.5, 0.8, 1.0],
    
}
param_grid_lgb = GridSearchCV(lgb, param_grid=param_grid_lgb, cv=10, n_jobs=-1)
param_grid_lgb.fit(X_train, y_train)
print(param_grid_lgb.best_estimator_)
best_param_lgb_gs = param_grid_lgb.best_estimator_
pred_lgb_gs = best_param_lgb_gs.predict(X_test)
'''
random_search_lgb = RandomizedSearchCV(lgb, param_grid_lgb, n_iter=30, cv = 10, n_jobs=-1, scoring = 'neg_mean_squared_error')
random_search_lgb.fit(X_train, y_train)
print(random_search_rf.best_estimator_)
best_param_rf_rs = random_search_rf.best_estimator_
pred_rf_rs = best_param_rf_rs.predict(X_test)'''

sns.kdeplot(pred_lgb_gs, label = 'grid_pred_lgb')
sns.kdeplot(pred_rf_rs, label = 'rand_pred')
plt.legend()
plt.show()

col_imp5 = pd.DataFrame(best_param_lgb_gs.feature_importances_, index = X_train.columns, columns = ['value']).sort_values(by='value', ascending=False)
plt.figure(figsize=(10,10))
sns.barplot(col_imp5.index, col_imp5['value'])
plt.xticks(rotation=45)

#from lightgbm import plot_importance
#plot_importance(param_grid_lgb.fit(X_train, y_train))

print(best_param_lgb_gs.score(X_train, y_train))  #0.9552976739243179
