import argparse
import pandas as pd
import joblib
from src.recommendation_engine import generate_si_recommendation

FEATURES = ['trace_spacing_mils', 'return_via_dist_um', 'sim_crosstalk_mv', 'temp_c']

def main():
    parser = argparse.ArgumentParser(description='Run a single prediction + recommendation.')
    parser.add_argument('--model', required=True, help='Path to trained model (.pkl)')
    parser.add_argument('--trace_spacing_mils', type=float, required=True)
    parser.add_argument('--return_via_dist_um', type=float, required=True)
    parser.add_argument('--sim_crosstalk_mv', type=float, required=True)
    parser.add_argument('--temp_c', type=float, required=True)
    args = parser.parse_args()

    model = joblib.load(args.model)

    df = pd.DataFrame([[args.trace_spacing_mils,
                        args.return_via_dist_um,
                        args.sim_crosstalk_mv,
                        args.temp_c]],
                      columns=FEATURES)

    report = generate_si_recommendation(model, df)
    print(report)

if __name__ == '__main__':
    main()
