from ._base import DataFrameFromJSONMixin
import pandas as pd


def get_patientid(subject):
    '''
    Helper function to get a paitent id from a fhir reference string. 
    '''
    split_string = subject['reference'].split('/')
    return split_string[-1]

class Observations(DataFrameFromJSONMixin):
    def __init__(self, path, patient_path):
        super().__init__(path)
        self.patient_df = pd.read_json(patient_path, lines = True)


    def impute_observation(self, obs_df: pd.DataFrame, patient_df: pd.DataFrame, loinc_code: str, col_name: str):
        '''
        Question 2

        Impute missing data for the glucose and triglycerides by using the mean of the column. 
        You will be using the observation resources that have these values. 
        You will be creating a column that that is a numerical value of the observation. 
        You will need to group the observation records by patient id. 
        When using the aggregation function aggregate by mean. The mean should be rounded to 2 decimal places

        The Loinc code for glucose is "2339-0"
        The Loinc code for triglycerides is "2571-8"

        Input: observations dataframe, loinc_code, col_name
        Output: a pandas dataframe grouped by patient id with mean imputed values for target column
        '''
        
        # raise NotImplementedError
        
    def mean_normalize(self, df: pd.DataFrame, col_name: str):
        '''
        Question 3 
        Create a function that will apply z score mean normalization to a column
        round the result to 3 decimal places. Hint this uses standard deviation. This function will take a dataframe 
        and the column name. It will apply normalization to the to the specified column.

        Inputs: 
        df: is a dataframe
        col_name:  the column name that z score mean normalized is applied to 

        Output: pandas series data float 3 decimal places
        '''
        # raise NotImplementedError

    def pipeline(self):
        observation_df = self.data
        patient_df = self.patient_df

        # get a dataframe that is grouped by patients and have imputed values of glucose 
        observation_glucose_df = self.impute_observation(observation_df,patient_df,'2339-0','glucose')

        # get a dataframe that is grouped by patients and have imputed values of triglycerides
        observation_tri_df = self.impute_observation(observation_df,patient_df,'2571-8', 'triglycerides')

        # merge the glucose and triglycerides dataframes
        combined_df = observation_tri_df.merge(observation_glucose_df, how='left', on='id')

        # apply mean normalization to the glucose and triglycerides columns
        combined_df['glucose'] = self.mean_normalize(combined_df,'glucose')
        combined_df['triglycerides'] = self.mean_normalize(combined_df,'triglycerides')

        return combined_df[['id','glucose','triglycerides']]