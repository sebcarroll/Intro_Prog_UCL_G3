import pickle
from general_functions import get_selected_listbox_value
from general_functions import check_input_valid


all_camp_data = {}

def create_resource_allocation_dict(camp_id, no_weeks_aid, total_food_supplied, total_medicine_supplied,no_refugees, week_food_per_refugee, week_medicine_per_refugee,delivery_time_weeks):
    resource_allocation_variables = {
        'camp_id': camp_id,
        'no_weeks_aid': no_weeks_aid,
        'total_food_supplied': total_food_supplied,
        'total_medicine_supplied': total_medicine_supplied,
        'no_refugees': no_refugees,
        'week_food_per_refugee': week_food_per_refugee,
        'week_medicine_per_refugee': week_medicine_per_refugee,
        'delivery_time_weeks': delivery_time_weeks
    }
    return resource_allocation_variables
def save_to_all_camp_data(camp_id, resource_allocation_variables):
    unique_name = f"camp_{camp_id}_data"
    all_camp_data[unique_name] = resource_allocation_variables


def resource_allocation(camp_id, no_weeks_aid, total_food_supplied, total_medicine_supplied, no_refugees, week_food_per_refugee, week_medicine_per_refugee):
    '''
    This function enables the administrator to allocate resources to a camp and will notify the administrator
    if the resources provided to the camp are not adequate to cover the total period in which aid is provided.

    :param camp_id: The identification number of the camp to which these resources are being allocated.
    :param no_weeks_aid: Defines the estimated number of weeks the camp shall be supplying aid for.
    This is important in determining when the administrator should be notified when supplies need delivery.
    :param total_food_supplied: Defines the amount of food supplied by the administrator to the camp in total.
    Will have to be updated prior to the camp running out of food.
    :param total_medicine_supplied: Defines the amount of medicine supplied by the administrator to the camp in total.
    Will have to be updated prior to the camp running out of medicine.
    :param no_refugees: The number of refugees that are at the camp - will change as the volunteers add to it.
    :param week_food_per_refugee: The expected weekly consumption of food per refugee.
    :param week_medicine_per_refugee: The expected weekly consumption of medicine per refugee
    :return:
    '''

    weeks_of_food_supply = total_food_supplied / week_food_per_refugee * no_refugees
    weeks_of_medicine_supply = total_medicine_supplied / week_medicine_per_refugee * no_refugees


    if weeks_of_food_supply < no_weeks_aid:

        additional_food_needed = (no_weeks_aid - weeks_of_food_supply) * week_food_per_refugee * no_refugees

        print(f" {additional_food_needed} additional units of food needed at camp {camp_id} to cover the aid duration period.")

    if weeks_of_medicine_supply < no_weeks_aid:

        additional_medicine_needed = (no_weeks_aid - weeks_of_medicine_supply) * week_medicine_per_refugee * no_refugees

        print(f" {additional_medicine_needed} units of medicine needed at camp {camp_id} to cover the aid duration period.")



'''

with open('camp_resources.pkl', 'wb') as file:
        pickle.dump(data, file)

    print("Values Submitted and Saved")

'''