import pandas as pd
list1 = [' loss_of_smell',
         ' red_spots_over_body',
         ' bloody_stool',
         ' slurred_speech',
         ' vomiting',
         ' pain_in_anal_region',
         ' chills',
         ' belly_pain',
         ' mild_fever',
         ' coma',
         ' fast_heart_rate',
         ' receiving_unsterile_injections',
         ' shivering',
         ' loss_of_appetite',
         ' sweating',
         ' prominent_veins_on_calf',
         ' irritability',
         ' abnormal_menstruation',
         ' internal_itching',
         ' watering_from_eyes',
         ' nausea',
         ' skin_peeling',
         ' excessive_hunger',
         ' scurring',
         ' continuous_feel_of_urine',
         ' restlessness',
         ' unsteadiness',
         ' pus_filled_pimples',
         ' red_sore_around_nose',
         ' irritation_in_anus',
         ' yellowing_of_eyes',
         ' continuous_sneezing',
         ' anxiety',
         ' visual_disturbances',
         ' polyuria',
         ' diarrhoea',
         ' irregular_sugar_level',
         ' inflammatory_nails',
         ' malaise',
         ' back_pain',
         ' increased_appetite',
         ' weight_gain',
         ' sunken_eyes',
         ' mucoid_sputum',
         ' loss_of_balance',
         ' palpitations',
         ' stomach_pain',
         ' patches_in_throat',
         ' fluid_overload',
         ' abdominal_pain',
         ' burning_micturition',
         ' yellow_urine',
         ' pain_behind_the_eyes',
         ' dizziness',
         ' movement_stiffness',
         ' swollen_legs',
         ' muscle_wasting',
         ' bruising',
         ' blurred_and_distorted_vision',
         ' phlegm',
         ' stomach_bleeding',
         ' dehydration',
         ' blood_in_sputum',
         ' obesity',
         ' silver_like_dusting',
         'itching',
         ' swelling_joints',
         ' breathlessness',
         ' weakness_in_limbs',
         ' blister',
         ' throat_irritation',
         ' spinning_movements',
         ' depression',
         ' foul_smell_of urine',
         ' knee_pain',
         ' receiving_blood_transfusion',
         ' constipation',
         ' swollen_extremeties',
         ' sinus_pressure',
         ' skin_rash',
         ' acidity',
         ' nodal_skin_eruptions',
         ' yellowish_skin',
         ' hip_joint_pain',
         ' swollen_blood_vessels',
         ' weakness_of_one_body_side',
         ' toxic_look_(typhos)',
         ' ulcers_on_tongue',
         ' neck_pain',
         ' cough',
         ' dischromic _patches',
         ' lack_of_concentration',
         ' brittle_nails',
         ' stiff_neck',
         ' painful_walking',
         ' swelling_of_stomach',
         ' high_fever',
         ' acute_liver_failure',
         ' spotting_ urination',
         ' pain_during_bowel_movements',
         ' runny_nose',
         ' weight_loss',
         ' mood_swings',
         ' puffy_face_and_eyes',
         ' redness_of_eyes',
         ' cramps',
         ' joint_pain',
         ' small_dents_in_nails',
         ' chest_pain',
         ' muscle_weakness',
         ' muscle_pain',
         ' lethargy',
         ' distention_of_abdomen',
         ' altered_sensorium',
         ' yellow_crust_ooze',
         ' blackheads',
         ' rusty_sputum',
         ' swelled_lymph_nodes',
         ' fatigue',
         ' family_history',
         ' indigestion',
         ' dark_urine',
         ' cold_hands_and_feets',
         ' headache',
         ' passage_of_gases',
         ' bladder_discomfort',
         ' enlarged_thyroid',
         ' extra_marital_contacts',
         ' drying_and_tingling_lips',
         ' congestion',
         ' history_of_alcohol_consumption']


def default_dataframe(list1):
    df = pd.Series(2, index=list1)

    df = pd.DataFrame(df).T
    return df


df = default_dataframe(list1)  # function call and unique dataframe is created


def symptoms_list(df, symptoms):
    df[symptoms] = 1
    return df


# this function will  fill the symptoms with 1 in the default df  hence df for prediction will be ready
symptoms = ['itching', 'skin_rash',
            'nodal_skin_eruptions', 'dischromic _patches']

df = symptoms_list(df, symptoms)

# now df is redy to be fed into the machine learning model and can predict disease
