import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

df = pd.read_csv (r'C:\Users\rog-g\OneDrive\Desktop\Lab - Introduction to Data Mining\Project_python\healthcare-dataset-stroke-data.csv', header =0, index_col="id")

def menu():
	print("Press 1 to print data information")
	print("Press 2 to print heatmap")
	print("Press 3 to print stroke frequency by heart_disease and hypertension")
	print("Press 4 to print stroke frequency")
	print("Press 5 to print stroke frequency by Gender")
	print("Press 6 to print stroke frequency by Age and BMI")
	print("Press 0 to end")

menu()
val = input('\nEnter Number ')
val_int = int(val)

while True:
	if val_int == 1:
		df.info()
	if val_int == 2:
		corr_matrix = df.drop(columns=['gender','ever_married','work_type','Residence_type','smoking_status']).corr() 
		fig, ax = plt.subplots(figsize=(10,5))
		ax = sns.heatmap(corr_matrix,
						annot=True, 
						linewidths=0.5,
						fmt=".2f", 
						cmap="YlGnBu" 
						)
		plt.show()
	if val_int == 3:
		ct1 = pd.crosstab(df.heart_disease,df.stroke)
		ct2 = pd.crosstab(df.hypertension,df.stroke)
		ct3 = pd.crosstab(df.ever_married,df.stroke)
		ct4 = pd.crosstab(df.smoking_status,df.stroke)
		
		colors = ["#FF6D60","#41644A"]

		fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2,
												ncols=2, 
												figsize=(20,10))

		
		ct1.plot(kind='bar',ax=ax1,color=colors,rot=0)
		ct2.plot(kind='bar',ax=ax2,color=colors,rot=0)
		ct3.plot(kind='bar',ax=ax3,color=colors,rot=0)
		ct4.plot(kind='bar',ax=ax4,color=colors,rot=0)

		ax1.set_xticklabels(["No","Yes"])
		ax2.set_xticklabels(["No","Yes"])
		
		ax1.legend(labels=['No Stroke', 'Stroke'])
		ax2.legend(labels=['No Stroke', 'Stroke'])
		ax3.legend(labels=['No Stroke', 'Stroke'])
		ax4.legend(labels=['No Stroke', 'Stroke'])
		plt.show()
	if val_int == 4:
		st_plot = df["stroke"].value_counts().plot(kind="bar",color=["#FF6D60","#41644A"], rot=0)
		plt.title("Stroke Frequency")
		plt.xticks(ticks=[1,0], labels=["stroke", "no_stroke"])
		plt.show()
	if val_int == 5:
		pd.crosstab(df.stroke, df.gender).plot(kind='bar', figsize=(10,6), color=["#FF6D60","#41644A","#86007D"],rot=0)
		plt.title("Stroke Frequency by Gender")
		plt.xticks(ticks=[0,1],labels=["No Stroke", "Stroke"])
		plt.xlabel(None)
		plt.ylabel("Amount")
		plt.show()
	if val_int == 6:
		plt.figure(figsize=(10,6))
		plt.scatter(df.age[df.stroke==0], df.bmi[df.stroke==0],color="#41644A")
		plt.scatter(df.age[df.stroke==1], df.bmi[df.stroke==1],color="#FF6D60")
		plt.title("Stroke Frequency by Age and BMI")
		plt.xlabel("Age")
		plt.ylabel("BMI")
		plt.legend(["No Stroke", "Stroke"])
		plt.show()
	if val_int == 0:
		break
	print("-------------END-------------")
	print("\n")
	menu()
	val = input('\nEnter Number ')
	val_int = int(val)

