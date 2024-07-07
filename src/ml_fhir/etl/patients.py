from tokenize import String
import pandas as pd
from datetime import datetime
from ._base import DataFrameFromJSONMixin


class Patients(DataFrameFromJSONMixin):
    def __init__(self, path):
        super().__init__(path)

    def get_age(self, dob, input_date):
        '''
        Question 1-1
        Calculate the age of the patient.

        Create a function that calculates the age based on the birthday and a given date. This will be used to apply to each row of the
        patient dataframe. 

        For example if the dob is 2000-01-01 and the input_date is 2024-01-03 then the age is 24

        inputs: 
        dob: string birthdate of patient
        input_date: string date used to calculate the age. yyyy-mm-dd

        Output:
        age_years: integer the age of the patient in years 
        '''
        # raise NotImplementedError
    
    def get_marital_status(self, df: pd.DataFrame):
        '''
        Question 1-2
        One hot encode the marital status. Take the existing dataframe and add the marital status columns.
         You can use built in pandas function for this.

        The columns added should be the following. It should be an integer 0 or 1.
        married_Divorced

        married_Married

        married_Never Married

        married_Widowed


        Input: pandas dataframe
        Output: pandas dataframe 
        '''
        # raise NotImplementedError


    def pipeline(self):
        patient_df = self.data

        patient_df["age"] = patient_df['birthDate'].apply(lambda x: self.get_age(x, '2023-11-05'))

        patient_df = self.get_marital_status(patient_df)
        return patient_df[['id','age','married_Divorced','married_Married','married_Widowed','married_Never Married' ]]
