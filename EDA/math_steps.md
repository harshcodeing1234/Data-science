# स्टेप 1: डेटा का आकार और प्रकार देखें (Shape & Scale Check)

कोई भी कैलकुलेशन करने से पहले डेटा के स्ट्रक्चर को समझें।

### क्या चेक करें:

`df.shape` और `df.describe()`

### गणितीय लॉजिक (What to Observe):

* डेटा में कितने रो (Rows) और कॉलम (Columns) हैं?
* क्या किसी कॉलम की वैल्यू बहुत छोटी है (जैसे उम्र: 1-100) और किसी की बहुत बड़ी (जैसे सैलरी: 10,000-10,00,000)?

### ऑब्जर्वेशन:

अगर स्केल में बहुत बड़ा अंतर है, तो आपको Distance-based algorithms (जैसे KNN, SVM) या Gradient Descent का उपयोग करने से पहले डेटा को Normalize/Standardize करना होगा, नहीं तो बड़ा नंबर छोटे नंबर के प्रभाव को खत्म कर देगा।

---

# स्टेप 2: सेंट्रल टेंडेंसी का मुकाबला (Mean vs Median Check)

यह स्टेप आपको डेटा के असली स्वभाव (Behavior) से परिचित कराएगा।

### क्या चेक करें:

हर न्यूमेरिकल कॉलम का Mean और Median निकालें और दोनों की तुलना करें।

### गणितीय लॉजिक (What to Observe):

**Mean ≈ Median:**
डेटा संतुलित है (Symmetric)। यानी ज़्यादातर वैल्यू बीच में हैं।

**Mean > Median:**
डेटा राइट-स्क्यूड (Right-Skewed) है। इसका मतलब है कि डेटा में कुछ बहुत बड़ी वैल्यूज़ (Outliers) मौजूद हैं जो औसत (Mean) को ऊपर खींच रही हैं (जैसे भारत में लोगों की इनकम का डेटा)।

**Mean < Median:**
डेटा लेफ्ट-स्क्यूड (Left-Skewed) है। डेटा में कुछ बहुत छोटी वैल्यूज़ हैं (जैसे किसी आसान एग्जाम के स्कोर्स)।

### ऑब्जर्वेशन:

अगर अंतर बड़ा है, तो मिसिंग वैल्यूज़ को भरने के लिए Mean की जगह Median का इस्तेमाल करें, क्योंकि Median पर आउटलायर्स का असर नहीं पड़ता।

---

# स्टेप 3: डेटा का बिखराव देखें (Spread & Variance Check)

सिर्फ बीच की वैल्यू (Mean) जानना काफी नहीं है, डेटा कितना फैला हुआ है यह जानना भी जरूरी है।

### क्या चेक करें:

**Standard Deviation (SD)** और **Range (Max - Min)**।

### गणितीय लॉजिक (What to Observe):

**छोटा Standard Deviation:**
डेटा की ज़्यादातर वैल्यूज़ Mean के बहुत पास हैं (डेटा कंसिस्टेंट और प्रेडिक्टेबल है)।

**बड़ा Standard Deviation:**
डेटा बहुत फैला हुआ है और इसमें बहुत विविधता (High Variance) है।

### ऑब्जर्वेशन:

अगर SD बहुत बड़ा है, तो आपका मॉडल आसानी से ओवरफिट (Overfit) हो सकता है या उसे सीखने में कठिनाई होगी। आपको डेटा को री-ग्रुप (Binning) करने या आउटलायर्स हटाने की जरूरत पड़ सकती है।

---

# स्टेप 4: डेटा का Distribution देखें (Distribution Check)

यह समझना जरूरी है कि डेटा किस प्रकार फैला हुआ है।

### क्या चेक करें:

* Histogram
* Skewness
* Distribution

### गणितीय लॉजिक (What to Observe):

**Symmetric / Normal Distribution:**
डेटा लगभग दोनों तरफ समान रूप से फैला हुआ है।

**Right-Skewed Distribution:**
कुछ बड़ी values मौजूद हैं।

**Left-Skewed Distribution:**
कुछ छोटी values मौजूद हैं।

### ऑब्जर्वेशन:

अगर data बहुत ज्यादा skewed है, तो जरूरत के अनुसार:

* Log Transformation
* Square Root Transformation
* Box-Cox Transformation

का उपयोग किया जा सकता है।

---

# स्टेप 5: आउटलायर्स चेक करें (Outlier Check)

डेटा में बहुत ज्यादा छोटी या बड़ी unusual values को identify करें।

### क्या चेक करें:

* Box Plot
* IQR
* Z-Score

### गणितीय लॉजिक (What to Observe):

अगर कोई value बाकी data से बहुत दूर है, तो वह **Outlier** हो सकती है।

### ऑब्जर्वेशन:

Outlier मिलने पर पहले यह समझें कि वह:

* Data Entry Error है
* Genuine Value है
* या कोई Rare Event है

इसके बाद जरूरत के अनुसार:

* Remove
* Cap/Winsorize
* Transform
* Keep

कर सकते हैं।

---

# स्टेप 6: आपस का रिश्ता ढूंढें (Correlation Matrix)

यह स्टेप मशीन लर्निंग के लिए सबसे महत्वपूर्ण है क्योंकि इससे फीचर्स का चयन (Feature Selection) होता है।

### क्या चेक करें:

`df.corr()` (Pearson Correlation Coefficient)

### गणितीय लॉजिक (What to Observe):

इसकी वैल्यू **-1 से +1** के बीच होती है।

**+0.7 से +1.0:**
दो फीचर्स के बीच मजबूत सीधा संबंध है (जैसे: घर का एरिया बढ़ने पर कीमत बढ़ना)।

**-0.7 से -1.0:**
मजबूत उल्टा संबंध है (जैसे: गाड़ी की उम्र बढ़ने पर उसकी कीमत घटना)।

**0 के पास:**
कोई लीनियर संबंध नहीं है।

### ऑब्जर्वेशन (Multicollinearity):

अगर दो इनपुट फीचर्स के बीच का कोरिलेशन बहुत हाई (जैसे 0.90) है, तो उनमें से किसी एक ही फीचर को मॉडल में रखें। दोनों को रखने पर मॉडल भ्रमित (Confuse) हो जाता है और एरर बढ़ जाता है।

---

# स्टेप 7: Probability और Uncertainty देखें

डेटा में किसी घटना के होने की संभावना और uncertainty को समझें।

### क्या चेक करें:

* Probability
* Conditional Probability
* Probability Distribution

### गणितीय लॉजिक (What to Observe):

अगर किसी event की probability:

* `P(A)` है, तो event A के होने की संभावना समझी जाती है।
* `P(A|B)` है, तो B होने पर A की probability समझी जाती है।

### ऑब्जर्वेशन:

Classification, Risk Analysis और कई ML problems में probability model की prediction और uncertainty समझने में मदद करती है।

---

# स्टेप 8: Statistical Significance / Hypothesis Check

यह check करें कि data में दिखाई देने वाला difference या relationship वास्तव में meaningful है या सिर्फ random chance के कारण दिखाई दे रहा है।

### क्या चेक करें:

* Null Hypothesis (H₀)
* Alternative Hypothesis (H₁)
* P-value
* Confidence Interval
* t-test / Chi-square test आदि

### गणितीय लॉजिक (What to Observe):

अगर **P-value** चुने गए significance level से छोटी है, तो Null Hypothesis के खिलाफ statistical evidence माना जा सकता है।

---

# स्टेप 9: Model Error Analysis

जब आपका मॉडल तैयार हो जाए, तो एरर के गणित को समझें।

### क्या चेक करें:

**Actual Value - Predicted Value (Residuals)** का डिस्ट्रीब्यूशन (ग्राफ)।

### गणितीय लॉजिक (What to Observe):

क्या आपके एरर का ग्राफ Normal Distribution (Bell Curve) बना रहा है और उसका मीन 0 है? यदि हाँ, तो आपका मॉडल बेहतरीन काम कर रहा है।

अगर एरर का ग्राफ एक तरफ झुका हुआ है, तो इसका मतलब है कि डेटा में कोई ऐसा छुपा हुआ पैटर्न (Pattern/Bias) है जो आपका मॉडल पकड़ नहीं पा रहा है। आपको नए फीचर्स जोड़ने या अलग एल्गोरिदम का उपयोग करने की आवश्यकता है।

---

# स्टेप 10: Model Evaluation Metrics

अंत में यह देखें कि आपका मॉडल कितनी अच्छी तरह prediction कर रहा है।

### Regression में क्या चेक करें:

* MAE
* MSE
* RMSE
* R²

### Classification में क्या चेक करें:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

### गणितीय लॉजिक (What to Observe):

Metrics को problem के type और business requirement के अनुसार evaluate करें।

उदाहरण:

**Regression:**

```text
Actual → Predicted → Error → MAE / MSE / RMSE / R²
```

**Classification:**

```text
Actual Class → Predicted Class → Confusion Matrix → Metrics
```
