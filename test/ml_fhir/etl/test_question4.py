from pandas.testing import assert_frame_equal
import pytest
import pandas as pd
import os
import sys
from src.ml_fhir.etl.patients import Patients
from src.ml_fhir.etl.observations import Observations
from src.ml_fhir.etl.label import Label


import pytest

def test_storke_ind():
    """ Test that the stroke ind is labeled properly"""
    actual_df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/q4-test.csv'))
    label = Label(os.path.join(os.path.dirname(__file__), '../data/test-observations.ndjson') , os.path.join(os.path.dirname(__file__), '../data/test-patients.ndjson') )
    label_df = label.pipeline()
    assert_frame_equal(actual_df, label_df)
