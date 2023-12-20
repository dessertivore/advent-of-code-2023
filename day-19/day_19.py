import re


def parse_into_dicts(file_name: str) -> tuple:
    """
    Create dicts for workflows and ratings.
    For each workflow, add to dict entry, and create 2 lists: steps and final outcome.
    Within steps, create a list for each step.
    """
    input_as_list: list[str] = open(file_name, "r").readlines()
    output = [line.strip("\n") for line in input_as_list]
    all_workflows_parsed = False
    workflows: dict = {}
    ratings: dict = {}
    counter = 0
    for line in output:
        if all_workflows_parsed == False:
            if line == "":
                all_workflows_parsed = True
            else:
                parts: list = line.split("{")
                key = parts[0]
                steps = re.search(
                    r"((\w)[<>=](\d+):(\w+),)?((\w)[<>=](\d+):(\w+),)?((\w)[<>=](\d+):(\w+),)?",
                    parts[1],
                ).group()[
                    :-1
                ]  # up to penultimate char to cut out the final comma
                final_step = re.search(r"[\w]*}", parts[1]).group()[
                    :-1
                ]  # up to penultimate char to exclude ending curly bracket
                all_organised_steps: list = []
                for step_part in steps.split(","):
                    identifying_letter = re.search(r"[\w]", step_part).group()
                    operator = re.search(r"[<>=]", step_part).group()
                    number = int(re.search(r"\d+", step_part).group())
                    destination = (re.search(r":\w*", step_part).group())[1:]
                    all_organised_steps.append(
                        (identifying_letter, operator, number, destination)
                    )
                workflows[key] = all_organised_steps, final_step
        else:
            ratings[counter] = {}
            numbers = re.findall(r"\d+", line)
            ratings[counter]["x"] = int(numbers[0])
            ratings[counter]["m"] = int(numbers[1])
            ratings[counter]["a"] = int(numbers[2])
            ratings[counter]["s"] = int(numbers[3])
            counter += 1
    return workflows, ratings


test = parse_into_dicts("day-19/input.txt")


def go_through_ratings(workflows: dict, ratings: dict) -> int:
    """
    Sift through ratings to see which are accepted. Sum all numbers of accepted ratings.
    """
    all_nums = []
    for rating in ratings.values():
        finished = False
        step_number = 0
        workflow_key = "in"
        while not finished:
            while step_number < len(workflows[workflow_key][0]) and not finished:
                rating_category = workflows[workflow_key][0][step_number][0]
                operator = workflows[workflow_key][0][step_number][1]
                comparator_value = workflows[workflow_key][0][step_number][2]
                outcome = workflows[workflow_key][0][step_number][3]
                if operator == "<" and rating[rating_category] >= comparator_value:
                    step_number += 1

                elif operator == ">" and rating[rating_category] <= comparator_value:
                    step_number += 1

                elif operator == "=" and rating[rating_category] != comparator_value:
                    step_number += 1

                else:
                    if outcome == "R":
                        finished = True
                        break
                    elif outcome == "A":
                        all_nums.append(sum(rating.values()))
                        finished = True
                        break
                    else:
                        workflow_key = outcome
                        step_number = 0
            if step_number == len(workflows[workflow_key][0]):
                outcome = workflows[workflow_key][1]
                if outcome == "R":
                    break
                elif outcome == "A":
                    all_nums.append(sum(rating.values()))
                    break
                else:
                    workflow_key = outcome
                    step_number = 0
    print(all_nums)
    return sum(all_nums)


print(go_through_ratings(test[0], test[1]))
