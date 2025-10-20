def total_salary(path) -> tuple[int, float]:
    try:
        # Open and read file
        with open(path, encoding="utf-8") as file:
            lines = file.readlines()
            # Retrieve records from the file
            payments = []
            for line in lines:
                name, salary = line.strip().split(",")
                payments.append(int(salary))
            # Calculate total and average
            total = sum(payments)
            average = total / len(payments)
            return total, average
    except FileNotFoundError:
        print("File not found")
        return 0,0
    except Exception as e:
        print(e)
        return 0,0

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
