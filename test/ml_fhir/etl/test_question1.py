from pandas.testing import assert_frame_equal
import pytest
import pandas as pd

import sys
sys.path.append('./src')

from ml_fhir.etl.patients import Patients

import pytest

@pytest.fixture
def setup_patient():
    patients = Patients('/app/data/test-patients.ndjson')
    return patients

def test_age(setup_patient):
    """ Test that the get_age"""
    actual_df = pd.read_csv('/app/test/ml_fhir/data/q1-1-test.csv')
    age_df = setup_patient.data
    age_df['age'] = age_df['birthDate'].apply(setup_patient.get_age)
    age_df = age_df[['id', 'age']]
    assert_frame_equal(actual_df, age_df)

def test_marital_status(setup_patient):
    """ Test that the get_marital_status """
    actual_df = pd.read_csv('/app/test/ml_fhir/data/q1-2-test.csv')
    marital_df = setup_patient.data
    marital_df = setup_patient.get_marital_status(marital_df)
    marital_df = marital_df[['id','married_Divorced','married_Married','married_Widowed','married_Never Married' ]]
    assert_frame_equal(actual_df, marital_df)