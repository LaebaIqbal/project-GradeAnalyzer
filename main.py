import matplotlib.pyplot as plt
import pandas as pd
csv_content= pd.read_csv("noten.csv", sep=";", encoding="latin1")

grade = csv_content["Note"]
ects = csv_content["ECTS"]

gpa = round((grade*ects).sum()/ects.sum(),2)

print("Your Current GPA: ", gpa)


plt.bar(csv_content["Modulcode"],csv_content["Note"])
plt.title("Notenübersicht")
plt.xlabel("Modul")
plt.ylabel("Note")
plt.text(0, -0.15,f'Your current GPA: {gpa}', fontsize=12, )

plt.show()



