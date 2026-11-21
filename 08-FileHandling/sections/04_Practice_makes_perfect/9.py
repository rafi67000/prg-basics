print("GRAPHIC DESIGNERS")
print("=================")

with open("it_company.csv", encoding="utf-8") as f:
    next(f)  # pominiecie zbednej linii

    for line in f:

        last_name, first_name, job, email = line.strip().split(",")  # rozdzielenie linii na dane

        if job == "Graphic Designer":
            print(f"{first_name} {last_name},{email}")
