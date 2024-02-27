from ._base import DataFrameFromJSONMixin
import pandas as pd 

def get_patientid(subject):
    '''
    Helper function to get a paitent id from a fhir reference string. 
    '''
    split_string = subject['reference'].split('/')
    return split_string[-1]

class Label(DataFrameFromJSONMixin):

    def __init__(self, path, patient_path):
        super().__init__(path)
        self.patient_df = pd.read_json(patient_path, lines = True)

    def get_stroke_ind(self,obs_df: pd.DataFrame, patient_df: pd.DataFrame):
        '''
        Question 4 
        Create a binarized column called stroke_ind. This column will have a 1.0 if the patient had 
        a stroke and a 0.0 if they did not have a stroke. Keep in mind that you need to account for all 
        patients in the patient dataframe not just the observations.

        input: observations dataframe, patient datafame
        output: data frame with the id and stroke_ind column (float 1 decimal)
        '''
        # raise NotImplementedError

    def pipeline(self):
        observation_df = self.data
        patient_df = self.patient_df 
        stroke_df = self.get_stroke_ind(observation_df,patient_df)
        return stroke_df
