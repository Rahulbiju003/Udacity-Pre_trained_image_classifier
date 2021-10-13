#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/print_functions_for_lab_checks.py
#                                                                             
# PROGRAMMER: Jennifer S.                                                    
# DATE CREATED: 05/14/2018                                  
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE:  This set of functions can be used to check your code after programming 
#           each function. The top section of each part of the lab contains
#           the section labeled 'Checking your code'. When directed within this
#           section of the lab one can use these functions to more easily check 
#           your code. See the docstrings below each function for details on how
#           to use the function within your code.
#
##

# Functions below defined to help with "Checking your code", specifically
# running these functions with the appropriate input arguments within the
# main() funtion will print out what's needed for "Checking your code"
#
def check_command_line_arguments(in_arg):

    if in_arg is None:
        print("* Doesn't Check the Command Line Arguments because 'get_input_args' hasn't been defined.")
    else:
        
        print("Command Line Arguments:\n     dir =", in_arg.dir, 
              "\n    arch =", in_arg.arch, "\n dogfile =", in_arg.dogfile)

def check_creating_pet_image_labels(results_dic):

    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'get_pet_labels' hasn't been defined.")
    else:

        stop_point = len(results_dic)
        if stop_point > 10:
            stop_point = 10
        print("\nPet Image Label Dictionary has", len(results_dic),
              "key-value pairs.\nBelow are", stop_point, "of them:")
   
        n = 0

        for key in results_dic:
 

            if n < stop_point:
                print("{:2d} key: {:>30}  label: {:>26}".format(n+1, key,
                      results_dic[key][0]) )

                n += 1
           
            else:
                break


def check_classifying_images(results_dic):

    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been defined.")
    elif len(results_dic[next(iter(results_dic))]) < 2:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been defined.")
    else:

        n_match = 0
        n_notmatch = 0

        print("\n     MATCH:")
        for key in results_dic:

            if results_dic[key][2] == 1:

                n_match += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}".format(key, 
                      results_dic[key][0], results_dic[key][1]))

        print("\n NOT A MATCH:")
        for key in results_dic:

            if results_dic[key][2] == 0:

                n_notmatch += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}".format(key,
                      results_dic[key][0], results_dic[key][1]))

        print("\n# Total Images",n_match + n_notmatch, "# Matches:",n_match ,
              "# NOT Matches:",n_notmatch)

 
def check_classifying_labels_as_dogs(results_dic):

    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been defined.")
    elif len(results_dic[next(iter(results_dic))]) < 4 :
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been defined.")

    else:

        n_match = 0
        n_notmatch = 0

        print("\n     MATCH:")
        for key in results_dic:

            if results_dic[key][2] == 1:

                n_match += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}  \nPetLabelDog: {:1d}  ClassLabelDog: {:1d}".format(key,
                      results_dic[key][0], results_dic[key][1], results_dic[key][3], 
                      results_dic[key][4]))

        print("\n NOT A MATCH:")
        for key in results_dic:

            if results_dic[key][2] == 0:

                n_notmatch += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}  \nPetLabelDog: {:1d}  ClassLabelDog: {:1d}".format(key,
                      results_dic[key][0], results_dic[key][1], results_dic[key][3], 
                      results_dic[key][4]))

        print("\n# Total Images",n_match + n_notmatch, "# Matches:",n_match ,
              "# NOT Matches:",n_notmatch)



def check_calculating_results(results_dic, results_stats_dic):

    if results_stats_dic is None:
        print("* Doesn't Check the Results Dictionary because 'calculates_results_stats' hasn't been defined.")
    else:

        n_images = len(results_dic)
        n_pet_dog = 0
        n_class_cdog = 0
        n_class_cnotd = 0
        n_match_breed = 0

        for key in results_dic:

            if results_dic[key][2] == 1:

                if results_dic[key][3] == 1:
                    n_pet_dog += 1

                    if results_dic[key][4] == 1:
                        n_class_cdog += 1
                        n_match_breed += 1

                else:

                    if results_dic[key][4] == 0:
                        n_class_cnotd += 1

            else:

                if results_dic[key][3] == 1:
                    n_pet_dog += 1

                    if results_dic[key][4] == 1:
                        n_class_cdog += 1

                else:

                    if results_dic[key][4] == 0:
                        n_class_cnotd += 1


        n_pet_notd = n_images - n_pet_dog
        pct_corr_dog = ( n_class_cdog / n_pet_dog )*100
        pct_corr_notdog = ( n_class_cnotd / n_pet_notd )*100
        pct_corr_breed = ( n_match_breed / n_pet_dog )*100
 
        print("\n ** Statistics from calculates_results_stats() function:")
        print("N Images: {:2d}  N Dog Images: {:2d}  N NotDog Images: {:2d} \nPct Corr dog: {:5.1f} Pct Corr NOTdog: {:5.1f}  Pct Corr Breed: {:5.1f}".format(
              results_stats_dic['n_images'], results_stats_dic['n_dogs_img'],
              results_stats_dic['n_notdogs_img'], results_stats_dic['pct_correct_dogs'],
              results_stats_dic['pct_correct_notdogs'],
              results_stats_dic['pct_correct_breed']))
        print("\n ** Check Statistics - calculated from this function as a check:")
        print("N Images: {:2d}  N Dog Images: {:2d}  N NotDog Images: {:2d} \nPct Corr dog: {:5.1f} Pct Corr NOTdog: {:5.1f}  Pct Corr Breed: {:5.1f}".format(
              n_images, n_pet_dog, n_pet_notd, pct_corr_dog, pct_corr_notdog,
              pct_corr_breed))
