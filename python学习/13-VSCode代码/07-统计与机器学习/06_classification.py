# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

y_true = np.array([0, 0, 0, 1, 1, 1])
probability = np.array([0.1, 0.4, 0.2, 0.45, 0.7, 0.9])
prediction = (probability >= 0.5).astype(int)
print(confusion_matrix(y_true, prediction))
print(classification_report(y_true, prediction, zero_division=0))
print("AUC：", roc_auc_score(y_true, probability))
