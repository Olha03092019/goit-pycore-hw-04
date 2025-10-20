def get_cats_info(path):
    try:
        # Open file and create list
        with open(path, encoding="utf-8") as file:
            info = []
        # Retrieve the info and add as dictionaries to the list
            for line in file:
                identifier, name, age = line.strip().split(",")
                info.append({"id": identifier, "name": name, "age": age})
            return info
    except FileNotFoundError:
        print("File not found")
        return []
    except Exception as e:
        print(e)
        return []


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
