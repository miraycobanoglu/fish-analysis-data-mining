# 🐟 Fish Species Classification

Bu projede, balıkların fiziksel ölçümlerine dayanarak türlerinin makine öğrenmesi algoritmaları ile tahmin edilmesi amaçlanmıştır.

---

## 📌 Proje Hakkında

Balık türlerinin doğru sınıflandırılması; ekosistem takibi, biyolojik çeşitlilik ve balıkçılık yönetimi açısından önemlidir.

Bu projede farklı makine öğrenmesi modelleri uygulanmış ve performansları karşılaştırılmıştır.

---

## 📊 Veri Seti

- Fish Market Dataset (Kaggle)
- 159 gözlem
- 6 farklı balık türü

### Özellikler

- Weight
- Length1
- Length2
- Length3
- Height
- Width

Hedef değişken:

- Species

---

## ⚙️ Veri Ön İşleme

- Eksik değer analizi yapıldı
- Median ile eksik değer doldurma
- Label Encoding uygulandı
- %80 eğitim / %20 test ayrımı yapıldı
- Ölçekleme (StandardScaler) uygulandı

---

## 🤖 Kullanılan Modeller

- Logistic Regression
- Random Forest
- KNN (K-Nearest Neighbors)
- SVM (Support Vector Machine)

---

## 📈 Değerlendirme Metrikleri

- Accuracy
- Precision (weighted)
- Recall (weighted)
- F1 Score (weighted)

---

## 🏆 Sonuçlar

- Tüm modeller yüksek doğruluk sağlamıştır
- Logistic Regression en dengeli performansı göstermiştir
- Bazı türler arasında karışmalar gözlemlenmiştir

---

## 📉 PCA Analizi

- Veri 2 boyuta indirgenmiştir
- Tür dağılımı görselleştirilmiştir
- Bazı sınıflar arasında örtüşme vardır

---

## 🧪 Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 🚀 Kurulum ve Çalıştırma

```bash
git clone https://github.com/kullaniciadi/fish-project.git
cd fish-project
pip install -r requirements.txt
python main.py
