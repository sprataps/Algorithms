from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_attr_pipeline=Pipeline([
                ('imputer', Imputer(strategy="median")),
                ('attribs_adder',CombinedAttributeAdder()),
                ('std_scaler',StandardScaler())
])
