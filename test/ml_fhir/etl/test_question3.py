from pandas.testing import assert_frame_equal
import pytest
import pandas as pd

import sys
sys.path.append('./src')

from ml_fhir.etl.observations import Observations

def test_mean_norm_glucose():
    """ Test mean normilization works"""
    test_df = pd.read_csv('/app/test/ml_fhir/data/q2-glucose-test.csv')
    actual_df = pd.read_csv('/app/test/ml_fhir/data/q3-test.csv')
    observations = Observations('/app/data/test-observations.ndjson', '/app/data/test-patients.ndjson')
    test_df['glucose'] = observations.mean_normalize(test_df, 'glucose')

    assert_frame_equal(actual_df, test_df)
