from tkinter import *
import numpy as np
import pandas as pd
import pickle as pk

# It should be noted that all of these
no_weeks_aid = 30
total_food_supplied = 500
total_medicine_supplied = 100
no_refugees = 50
week_food_per_refugee = 21
week_medicine_per_refugee = 2
delivery_time_weeks = 2
def resource_allocation(camp_id, no_weeks_aid, total_food_supplied, total_medicine_supplied, no_refugees, week_food_per_refugee, week_medicine_per_refugee):
    '''
    This function enables the administrator to allocate resources to a camp and will notify the administrator
    what camp resources are running low and when they should allocate more resources to ensure that they do not run out.

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

    weeks_of_food_supply = total_food_supplied / week_food_per_refugee / no_refugees
    weeks_of_medicine_supply = total_medicine_supplied / week_medicine_per_refugee / no_refugees


    if no_weeks_aid < (total_food_supplied / week_food_per_refugee / no_refugees):
        #some code that makes it suggest it allocate more resources - are you sure you want to allocate this amount of food given?
        #some code that then reminds admin in x number of weeks to allocate more resources to this camp - probably a separate function.

    elif no_weeks_aid < (total_medicine_supplied / week_medicine_per_refugee / no_refugees):
        # some code that makes it suggest it allocate more resources - are you sure you want to allocate this amount of medicine given?
        # some code that then reminds admin in x number of weeks to allocate more resources to this camp - probably a separate function

def notify_admin_resources(camp_id, current_food, current_medicine, delivery_time_weeks):