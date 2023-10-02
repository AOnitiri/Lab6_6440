from ml_fhir.etl import Patients, Observations, Label

'''
Process the data pipline to run all of the transformations needed to create
the final dataset for machine learning training. 
'''

def process_pipeline(): 
    patients = Patients(path)
    patients.pipeline()
    raise NotImplementedError


if __name__ == "__main__":
    process_pipeline()
