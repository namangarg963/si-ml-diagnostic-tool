def generate_si_recommendation(model, input_df, threshold_ps: float = 35.0) -> str:
    pred_width = float(model.predict(input_df)[0])

    spacing = float(input_df['trace_spacing_mils'].values[0])
    via_dist = float(input_df['return_via_dist_um'].values[0])

    report = f"Predicted Eye Width: {pred_width:.2f} ps\n"

    if pred_width < threshold_ps:
        report += "STATUS: FAIL. Suggestion: "
        if via_dist > 500:
            report += "Add return-via stitching. "
        if spacing < 8:
            report += "Increase trace spacing."
    else:
        report += "STATUS: PASS."

    return report
