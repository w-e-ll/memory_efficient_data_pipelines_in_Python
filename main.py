from typing import Generator, List



def read_file(file_name: str) -> Generator:
    try:
        return (line for line in open(file_name))
    except Exception as err:
        print(f"Unexpected error reading {file_name}: ", repr(err))


def make_formatting(rows: Generator) -> Generator:
    return (row.rstrip().split(",") for row in rows)


def make_list_object(data_list: Generator) -> List:
    return list(row for row in data_list)


def generate_departments(cleaned_data_list: List) -> List:
    generated_states = (line[0] for line in cleaned_data_list)
    return list(set(generated_states))


def filter_by_department(data_list: List, departments: List) -> Generator:
    return (filter(lambda x: x[0] == dep, data_list) for dep in departments)


def total_number_of_sales(filtered_object: Generator) -> Generator:
    return (sum(map(lambda y: int(y[-1]), obj)) for obj in filtered_object)


def departments_with_sales(departments: List, total_sales: Generator) -> zip:
    return zip(departments, total_sales)


def write_output(file_name, output_data):
    try:
        with open(f'{file_name}', 'w') as output_file:
            [output_file.write(f"{obj[0]}, {obj[1]}\n") for obj in output_data]
    except Exception as err:
        print(f"Unexpected error writing {file_name}: ", repr(err))


if __name__ == '__main__':
    input_file_name = "./input.csv"
    output_file_name = "./output.csv"
    csv_lines = read_file(input_file_name)
    data = make_formatting(csv_lines)
    data_list_obj = make_list_object(data)
    unique_departments = generate_departments(data_list_obj)
    department_rows = filter_by_department(data_list_obj, unique_departments)
    sales_results = total_number_of_sales(department_rows)
    result = departments_with_sales(unique_departments, sales_results)
    write_output(output_file_name, result)
