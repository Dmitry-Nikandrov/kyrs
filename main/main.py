from func import load_function, filter_and_mask_account, sorted_list, data_transform


operation_all = load_function("operations.json")
operation_filted = filter_and_mask_account(operation_all)
operation_sorted = sorted_list(operation_filted)
operation_data_transform = data_transform(operation_sorted)

for operation in operation_data_transform:
  print (f'''{operation['date']} {operation['description']}
{operation['from']} -> {operation['to']}
{operation['amount']} {operation['name']}\n''')