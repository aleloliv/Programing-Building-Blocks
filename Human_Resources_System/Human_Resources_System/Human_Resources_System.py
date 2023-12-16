with open("hr_system.txt") as hr_system:
    for line in hr_system:
        clean_line = line.strip()
        columns = clean_line.split(" ")
        names = columns[0]
        id_number = int(columns[1])
        job_title = columns[2]
        salary = float(columns[3])
        paycheck = salary/24
        bonus = 1000.00
        if (job_title == "Engineer"):
            paycheck += bonus

        print(f"{names} (ID: {id_number}), {job_title} - ${paycheck:.2f}")
