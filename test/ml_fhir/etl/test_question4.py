from pandas.testing import assert_frame_equal
import pytest
import pandas as pd

import sys
sys.path.append('./src')

from ml_fhir.etl.patients import Patients
from ml_fhir.etl.observations import Observations
from ml_fhir.etl.label import Label


import pytest

def test_storke_ind():
    """ Test that the stroke ind is labeled properly"""
    actual_df = pd.read_csv('/app/test/ml_fhir/data/q4-test.csv')
    label = Label('/app/data/test-observations.ndjson', '/app/data/test-patients.ndjson')
    label_df = label.pipeline()
    assert_frame_equal(actual_df, label_df)
