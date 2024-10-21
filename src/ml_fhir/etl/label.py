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

        def get_snomed_code(valueCodeableConcept):
            try:
                for coding in valueCodeableConcept.get('coding', []):
                    if coding.get('system') == 'http://snomed.info/sct':
                        return coding.get('code')
                return None
            except (TypeError, AttributeError):
                return None

        obs_df['snomed_code'] = obs_df['valueCodeableConcept'].apply(get_snomed_code)

        stroke_obs = obs_df[obs_df['snomed_code'] == "230690007"]
        stroke_patient_ids = stroke_obs['subject'].apply(
            lambda x: x.get('reference', '').split('/')[1] if isinstance(x, dict) else None
        ).dropna().unique()

        result_df = patient_df[['id']].copy()
        result_df['stroke_ind'] = 0.0
        result_df.loc[result_df['id'].isin(stroke_patient_ids), 'stroke_ind'] = 1.0
        result_df['stroke_ind'] = result_df['stroke_ind'].astype(float).round(1)

        return result_df[['id', 'stroke_ind']]

    def pipeline(self):
        observation_df = self.data
        patient_df = self.patient_df 
        stroke_df = self.get_stroke_ind(observation_df,patient_df)
        return stroke_df
