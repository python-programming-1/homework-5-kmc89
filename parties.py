import csv
import pprint


def get_bar_party_data():
    """this function reads from a csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific location and the number of complaint calls
     it received in 2016"""

    bar_list = []
    with open('bar_locations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            bar_dict = {'location_type': row[0],
                        'zip_code': row[1],
                        'city': row[2],
                        'borough': row[3],
                        'latitude': row[4],
                        'longitude': row[5],
                        'num_calls': row[6]}
            bar_list.append(bar_dict)
    return bar_list


def print_data(data):
    for entry in data:
        print(entry)
        pprint.pprint(entry)


def get_most_noisy_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    noisiest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    # write code here to find the noisiest city and borough and their respective metrics
    noise_city_calls = {}
    noise_borugh_calls = {}

    for list in data:
        if list['city'] == 'City':
            continue
        if list['city'] in noise_city_calls.keys():
            noise_city_calls[list['city']] += int(list['num_calls'])
        else:
            noise_city_calls[list['city']] =  int(list['num_calls'])
        if list['borough'] in noise_borugh_calls.keys():
            noise_borugh_calls[list['borough']] += int(list['num_calls'])
        else:
            noise_borugh_calls[list['borough']] = int(list['num_calls'])

    city = ''
    borough = ''
    num = 0
    for k,v in noise_city_calls.items():
        if v > num:
            city = k
            num = v
    noisiest_city_and_borough['city'] = city
    noisiest_city_and_borough['num_city_calls'] = num

    num = 0
    for k,v in noise_borugh_calls.items():
        if v > num:
            borough = k
            num = v
    noisiest_city_and_borough['borough'] = borough
    noisiest_city_and_borough['num_borough_calls'] = num


    return noisiest_city_and_borough


def get_quietest_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    quietest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    # write code here to find the quietest city and borough and their respective metrics
    noise_city_calls = {}
    noise_borugh_calls = {}

    for list in data:
        if list['city'] == 'City':
            continue
        if list['city'] in noise_city_calls.keys():
            noise_city_calls[list['city']] += int(list['num_calls'])
        else:
            noise_city_calls[list['city']] =  int(list['num_calls'])
        if list['borough'] in noise_borugh_calls.keys():
            noise_borugh_calls[list['borough']] += int(list['num_calls'])
        else:
            noise_borugh_calls[list['borough']] = int(list['num_calls'])

    city = ''
    borough = ''
    num = float('inf')
    for k,v in noise_city_calls.items():
        if v < num:
            city = k
            num = v
    quietest_city_and_borough['city'] = city
    quietest_city_and_borough['num_city_calls'] = num

    num = float('inf')
    for k,v in noise_borugh_calls.items():
        if v < num:
            borough = k
            num = v
    quietest_city_and_borough['borough'] = borough
    quietest_city_and_borough['num_borough_calls'] = num

    return quietest_city_and_borough


if __name__ == '__main__':
    bar_data = get_bar_party_data()

    # uncomment the line below to see what the data looks like
    # print_data(bar_data)

    noisy_metrics = get_most_noisy_city_and_borough(bar_data)

    quiet_metrics = get_quietest_city_and_borough(bar_data)

    print('Noisy Metrics: {}'.format(noisy_metrics))
    print('Quiet Metrics: {}'.format(quiet_metrics))
