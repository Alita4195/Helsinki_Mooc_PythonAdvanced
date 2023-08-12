# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):

    average_person1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    average_person2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    average_person3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3

    if average_person1 < average_person2 and average_person1 < average_person3:
        return person1
    elif average_person2 < average_person1 and average_person2 < average_person3:
        return person2
    else:
        return person3


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    averages = smallest_average(person1, person2, person3)
    print(averages)
