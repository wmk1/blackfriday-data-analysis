from enum import Enum

class DataTranslators(Enum):
    trestbps = "Resting blood pressure"
    chol = "Serum cholesteral"
    thalach = "Maximum heart rate achieved"
    fbs = "Fasting blood sugar"
    cp = "chest pain"
    exang = "Excercise induced angina"
    oldpeak = "ST Depression"
    slope = "Slope of the peak"
    ca = "Number of major vessels"

class DataTableElements(Enum):
    age = "age"
    sex = "sex"
    cp = "cp"
    trestbps = "trestbps"
    chol = "chol"
    fbs = "fbs"
    restecg = "restecg"
    thalach = "thalach"
    exang = "exang"
    oldpeak = "oldpeak"
    slope = "slope"
    ca = "ca"
    thal = "thal"
    target = "target"

