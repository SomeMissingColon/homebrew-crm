import csv
csv_path = 'CSVs/jan26-2022.csv'
def load_call_list():
    with open(csv_path, 'r', newline='',encoding = 'utf-8') as read_object:
        reader = csv.DictReader(read_object)
        call_list = list(reader)
    return call_list

def get_client(client_number):
    #here client number refers to its position within the csv
        client_number = int(client_number)
        return load_call_list()[client_number]
def save_client_number(client_number):
    with open('last_client.txt', 'w') as f:
        f.write(str(client_number))
def get_last_client_number():
    with open('last_client.txt', 'r') as f:
        return f.read()
def delete_client(client_number):
    call_list = load_call_list()
    call_list.pop(int(client_number))
    with open(csv_path, 'w',encoding='utf8') as csvfile:
        fields = list(call_list[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for client in call_list:
            writer.writerow(client)
def update_client(client_number,key,new_value):
    call_list = load_call_list()
    call_list[int(client_number)][key] = new_value
    with open(csv_path, 'w',encoding='utf8') as csvfile:
        fields = list(call_list[0].keys())
        writer = csv.DictWriter(csvfile,fieldnames=fields)
        writer.writeheader()
        for client in call_list:
            writer.writerow(client)

def save_client_externally(client):
    fields = list(client.keys())

    with open('CSVs/prequalifieds/premades.csv', 'a', newline='', encoding='utf8') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writerow(client)
