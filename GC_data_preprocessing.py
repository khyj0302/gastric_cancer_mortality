
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df.columns

X = df[['SEX', 'TCODE', 'MCODE_GRP', 'GRADE', 'AGE', 'T_SIZE', 'AJCC7_STAGE',
        'G1E_HGHT', 'G1E_WGHT', 'G1E_BMI', 'G1E_WSTC', 'G1E_BP_SYS',
        'G1E_BP_DIA', 'G1E_URN_PROT', 'G1E_HGB', 'G1E_FBS', 'G1E_TOT_CHOL',
        'G1E_SGOT', 'G1E_SGPT', 'G1E_GGT', 'G1E_TG', 'G1E_HDL', 'G1E_LDL',
        'G1E_CRTN', 'G1E_GFR', 'Q_SMK_YN', 'Q_DRK_FRQ_V09N', 'Q_DRK_AMT_V09N',
        'Q_PA_VD', 'Q_PA_MD', 'Q_PA_WALK', 'AF', 'CKD', 'COPD', 'DM', 'DVT',
        'DYS', 'HF', 'hyper', 'LD', 'MI', 'obesity', 'Obesity', 'stroke']]

y = df[['5year_survival_time(day)', '5year_death', '3year_survival_time(day)',
        '3year_death', '1year_survival_time(day)', '1year_death']]

categorical_columns = ['SEX','TCODE','MCODE_GRP','Q_SMK_YN','G1E_HGHT', 'G1E_WGHT', 'G1E_WSTC']

categorical_order_columns = ['AJCC7_STAGE','GRADE', 'G1E_URN_PROT']

onehot_encoder = OneHotEncoder(sparse=False)

X_encoded = pd.DataFrame(onehot_encoder.fit_transform(X[categorical_columns]))
X_encoded.columns = onehot_encoder.get_feature_names_out(categorical_columns)

# Drop unnecessary columns or rows from the dataset
X_continuous = X.drop(columns=categorical_columns)
X=pd.concat([X_continuous, X_encoded], axis=1)

label_encoder = LabelEncoder()

for column in categorical_order_columns:
    X[column]=label_encoder.fit_transform(X[column])
