import pandas as pd 

#loading dataset
data = pd.read_csv("SampleSuperstore.csv")

#checking dataset
print(data.head())
print(data.info())

#checking null values
print(data.isnull().sum())

#checking duplicate values
print(data.duplicated().sum())
data = data.drop_duplicates()
print(data.duplicated().sum())

#cleaning str data
text_col = [
    "Ship Mode",
    "Segment",
    "City",
    "State",
    "Region",
    "Category",
    "Sub-Category",
                    ]
for col in text_col:
    data[col] = data[col].astype(str).str.strip()

data["City"] = data["City"].str.title()
data["State"] = data["State"].str.title()

#cleaning numeric data
data = data[data["Sales"]>0]
data = data[data["Quantity"]>0]
data = data[data["Discount"]>=0]

#saving cleaned data
data.to_csv("Cleaned_SampleSuperstore.csv",index=False)


#understandind data
print("TOTAL SALES",data["Sales"].sum())
print("TOTAL PROFIT",data["Profit"].sum())
print("TOTAL QUANTITY SOLD",data["Quantity"].sum())

#summary
print(data[["Sales","Profit","Quantity","Discount"]].describe())

#sales by category
category_sales = data.groupby("Category")[["Sales","Profit"]].sum().reset_index()
print(category_sales)

#profit by region
region_profit = data.groupby("Region")[["Sales","Profit"]].sum().reset_index()
print(region_profit)

#segment analysis
segment_profit = data.groupby("Segment")[["Sales","Profit"]].sum().reset_index()
print(segment_profit)

#sub category analysis
sub_category_analysis = data.groupby("Sub-Category")[["Sales","Profit"]].sum().reset_index()
print(sub_category_analysis)
