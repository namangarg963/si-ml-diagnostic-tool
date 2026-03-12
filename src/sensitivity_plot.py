
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib

FEATURES = ['trace_spacing_mils', 'return_via_dist_um', 'sim_crosstalk_mv', 'temp_c']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True)
    parser.add_argument('--out', default='assets/via_sensitivity.png')
    parser.add_argument('--spacing', type=float, default=10.0)
    parser.add_argument('--xtalk', type=float, default=10.0)
    parser.add_argument('--temp', type=float, default=25.0)
    parser.add_argument('--vmin', type=float, default=100.0)
    parser.add_argument('--vmax', type=float, default=1000.0)
    parser.add_argument('--points', type=int, default=100)
    args = parser.parse_args()

    model = joblib.load(args.model)
    via_sweep = np.linspace(args.vmin, args.vmax, args.points)
    sweep_df = pd.DataFrame({
        'trace_spacing_mils': args.spacing,
        'return_via_dist_um': via_sweep,
        'sim_crosstalk_mv': args.xtalk,
        'temp_c': args.temp
    })
    preds = model.predict(sweep_df)

    plt.figure(figsize=(8,5))
    plt.plot(via_sweep, preds, label='Predicted Eye Width', color='blue')
    plt.axhline(y=35, color='red', linestyle='--', label='Min Spec (35 ps)')
    plt.title('Impact of Return-Via Distance on Predicted Eye Width')
    plt.xlabel('Return-Via Distance (µm)')
    plt.ylabel('Eye Width (ps)')
    plt.legend(); plt.grid(True); plt.tight_layout()
    plt.savefig(args.out, dpi=160)
    print(f'Saved sensitivity plot to {args.out}')

if __name__ == '__main__':
    main()
