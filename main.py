import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

sns.set(style="whitegrid")

# 1) Veri yükle
df = pd.read_csv("fish.csv")
print("Veri seti ilk 5 satır:")
print(df.head())

# 2) Eksik değer kontrol ve imputation
print("\nHer sütunda boş (NaN) sayısı:")
print(df.isnull().sum())

imputer = SimpleImputer(strategy="median")
df[["weight", "length1", "length2", "length3", "height", "width"]] = imputer.fit_transform(
    df[["weight", "length1", "length2", "length3", "height", "width"]]
)

print("\nImputation sonrası eksik değer sayısı:")
print(df.isnull().sum())

# 3) Label encode (etiketleme)
le = LabelEncoder()
df["species"] = le.fit_transform(df["species"])

# 4) X, y
X = df[["weight", "length1", "length2", "length3", "height", "width"]].copy()
y = df["species"].copy()

# 5) Train/test split (stratify tavsiye edilir)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 6) Modeller (LogReg,SVM ve KNN için ölçekleme kullandık (Ölçekleme, verideki sayısal sütunların ölçeğini eşitlemek için yapılır.))
models = {
    "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000, solver="lbfgs", random_state=42)),
    "Random Forest": RandomForestClassifier(n_estimators=200, random_state=42),
    "KNN": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)),
    "SVM": make_pipeline(StandardScaler(), SVC(kernel="rbf", C=1, gamma="scale"))
}

results = []

for name, model in models.items():
    print(f"\n----- {name} -----")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    rec = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

    print(f"Accuracy: {acc:.4f}")
    print(f"Precision (weighted): {prec:.4f}")
    print(f"Recall (weighted): {rec:.4f}")
    print(f"F1 Score (weighted): {f1:.4f}")

    results.append([name, acc, prec, rec, f1])

    # Confusion Matrix çizimi (doğru fonksiyon kullanıldı)
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(f"{name} - Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.show()

# Özet tablo
result_df = pd.DataFrame(results, columns=["Model", "Accuracy", "Precision", "Recall", "F1 Score"])
print("\n\n===== MODEL KARŞILAŞTIRMA TABLOSU =====")
print(result_df)


# =====================================================
#               *** PCA BÖLÜMÜ (Ekledim) ***
# =====================================================

from sklearn.decomposition import PCA

# Ölçekleme (PCA için gerekli)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA (2 bileşene düşür)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# PCA DataFrame
pca_df = pd.DataFrame({
    "PCA1": X_pca[:, 0],
    "PCA2": X_pca[:, 1],
    "species": y
})

# PCA GRAFİĞİ
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=pca_df,
    x="PCA1",
    y="PCA2",
    hue="species",
    palette="tab10",
    s=80
)
plt.title("PCA: Balık Türlerinin 2 Boyutta Gösterimi")
plt.show()