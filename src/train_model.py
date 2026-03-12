
import argparse
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib

FEATURES = ['trace_spacing_mils', 'return_via_dist_um', 'sim_crosstalk_mv', 'temp_c']
TARGET = 'meas_eye_width_ps'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True)
    parser.add_argument('--model', default='models/si_model_v1.pkl')
    parser.add_argument('--max_depth', type=int, default=3)
    args = parser.parse_args()

    df = pd.read_csv(args.data)
    X = df[FEATURES]
    y = df[TARGET]
    model = DecisionTreeRegressor(max_depth=args.max_depth)
    model.fit(X, y)
    joblib.dump(model, args.model)
    print(f'Model saved to {args.model}')

if __name__ == '__main__':
    main()
