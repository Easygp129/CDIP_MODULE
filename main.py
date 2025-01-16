import streamlit as st

def main():
    st.title("EFNS/PNS 2021 CIDP Diagnostic and Management Module")

    # ---------------------------------------------------------------------
    # SECTION A: CLINICAL CRITERIA AND HISTORY
    # ---------------------------------------------------------------------
    st.header("A. Clinical and Historical Information")

    duration_months = st.number_input(
        "Duration of symptoms in months (≥2 months suggests CIDP):",
        min_value=0.0,
        max_value=120.0,
        value=3.0,
        step=0.5
    )

    symmetry = st.selectbox(
        "Overall Pattern of Limb Involvement:",
        ["Symmetrical", "Asymmetrical", "Focal"]
    )

    distribution_weakness = st.multiselect(
        "Distribution of Weakness (select all that apply):",
        ["Proximal Upper Limbs", "Distal Upper Limbs", "Proximal Lower Limbs", "Distal Lower Limbs"]
    )

    sensory_involvement = st.selectbox(
        "Sensory Involvement Pattern:",
        ["Prominent Sensory", "Mild to Moderate Sensory", "Pure Motor (No Sensory)"]
    )

    reflex_status = st.selectbox(
        "Deep Tendon Reflexes in Affected Limbs:",
        ["Normal", "Reduced", "Absent"]
    )

    progression_pattern = st.selectbox(
        "Progression Pattern of Weakness/Sensory Change:",
        [
            "Slowly Progressive",
            "Stepwise Progressive",
            "Recurrent/Relapsing",
            "No Significant Progression"
        ]
    )

    other_causes = st.selectbox(
        "Any Other Cause(s) That Fully Explain the Neuropathy?",
        ["No", "Yes"]
    )

    sensory_ataxia = st.selectbox(
        "Is there Sensory Ataxia (e.g., positive Romberg)?",
        ["No", "Yes"]
    )

    # ---------------------------------------------------------------------
    # SECTION B: NERVE CONDUCTION STUDIES
    # We include data for the following nerves on BOTH sides (Left & Right):
    #   1) Median Motor
    #   2) Median Sensory
    #   3) Ulnar Motor
    #   4) Ulnar Sensory
    #   5) Radial Motor
    #   6) Superficial Radial Sensory
    #   7) Tibial Motor
    #   8) Peroneal (Fibular) Motor
    #   9) Sural Sensory
    #   10) Superficial Peroneal (Fibular) Sensory
    #
    # For each motor nerve:
    #   - Distal Motor Latency (DML) in ms
    #   - Conduction Velocity (CV) in m/s
    #   - CMAP Amplitude in mV
    #   - Duration of Motor Waveform in ms
    #   - F-wave Latency in ms
    #   - Conduction Block (Yes/No)
    #
    # For each sensory nerve:
    #   - Distal Latency in ms
    #   - Conduction Velocity in m/s
    #   - SNAP Amplitude in µV
    #   - Duration of Sensory Waveform in ms
    #
    # ---------------------------------------------------------------------
    st.header("B. Nerve Conduction Studies (Left & Right)")

    # -------------- Helper UI function to input motor nerve data --------------
    def motor_nerve_input(nerve_name, side):
        st.subheader(f"{nerve_name} Motor - {side} Side")

        dml = st.number_input(f"{nerve_name} Motor ({side}) - Distal Motor Latency (ms):", 0.0, 50.0, 4.0, 0.1)
        cv = st.number_input(f"{nerve_name} Motor ({side}) - Conduction Velocity (m/s):", 0.0, 100.0, 50.0, 1.0)
        cmap = st.number_input(f"{nerve_name} Motor ({side}) - CMAP Amplitude (mV):", 0.0, 50.0, 5.0, 0.1)
        duration = st.number_input(f"{nerve_name} Motor ({side}) - Duration (ms):", 0.0, 50.0, 8.0, 0.1)
        fwave = st.number_input(f"{nerve_name} Motor ({side}) - F-wave Latency (ms):", 0.0, 80.0, 30.0, 0.5)
        conduction_block = st.selectbox(
            f"{nerve_name} Motor ({side}) - Conduction Block?",
            ["No", "Yes"]
        )
        return (dml, cv, cmap, duration, fwave, conduction_block)

    # -------------- Helper UI function to input sensory nerve data --------------
    def sensory_nerve_input(nerve_name, side):
        st.subheader(f"{nerve_name} Sensory - {side} Side")

        dist_lat = st.number_input(f"{nerve_name} Sensory ({side}) - Distal Latency (ms):", 0.0, 30.0, 3.0, 0.1)
        cv = st.number_input(f"{nerve_name} Sensory ({side}) - Conduction Velocity (m/s):", 0.0, 100.0, 48.0, 1.0)
        snap = st.number_input(f"{nerve_name} Sensory ({side}) - SNAP Amplitude (µV):", 0.0, 200.0, 12.0, 0.1)
        duration = st.number_input(f"{nerve_name} Sensory ({side}) - Duration (ms):", 0.0, 50.0, 6.0, 0.1)
        return (dist_lat, cv, snap, duration)

    # ----------------- Collect motor data for each nerve (Left & Right) -----------------
    median_motor_left = motor_nerve_input("Median", "Left")
    median_motor_right = motor_nerve_input("Median", "Right")

    ulnar_motor_left = motor_nerve_input("Ulnar", "Left")
    ulnar_motor_right = motor_nerve_input("Ulnar", "Right")

    radial_motor_left = motor_nerve_input("Radial", "Left")
    radial_motor_right = motor_nerve_input("Radial", "Right")

    tibial_motor_left = motor_nerve_input("Tibial", "Left")
    tibial_motor_right = motor_nerve_input("Tibial", "Right")

    peroneal_motor_left = motor_nerve_input("Peroneal", "Left")
    peroneal_motor_right = motor_nerve_input("Peroneal", "Right")

    # ----------------- Collect sensory data for each nerve (Left & Right) -----------------
    median_sens_left = sensory_nerve_input("Median", "Left")
    median_sens_right = sensory_nerve_input("Median", "Right")

    ulnar_sens_left = sensory_nerve_input("Ulnar", "Left")
    ulnar_sens_right = sensory_nerve_input("Ulnar", "Right")

    radial_sens_left = sensory_nerve_input("Superficial Radial", "Left")
    radial_sens_right = sensory_nerve_input("Superficial Radial", "Right")

    sural_sens_left = sensory_nerve_input("Sural", "Left")
    sural_sens_right = sensory_nerve_input("Sural", "Right")

    superficial_peroneal_sens_left = sensory_nerve_input("Superficial Peroneal", "Left")
    superficial_peroneal_sens_right = sensory_nerve_input("Superficial Peroneal", "Right")

    # ---------------------------------------------------------------------
    # SECTION C: OPTIONAL ANCILLARY DATA
    # ---------------------------------------------------------------------
    st.header("C. Ancillary Investigations (Optional)")

    csf_protein = st.number_input("CSF Protein (mg/dL):", 0.0, 300.0, 80.0, 1.0)
    csf_elevated = True if csf_protein > 45.0 else False

    imaging_findings = st.selectbox(
        "Ultrasound/MRI Evidence of Nerve Enlargement?",
        ["Not Done", "No", "Yes"]
    )
    biopsy_findings = st.selectbox(
        "Nerve Biopsy Consistent with CIDP?",
        ["Not Done", "No", "Yes"]
    )

    # ---------------------------------------------------------------------
    # SECTION D: EVALUATE BUTTON
    # ---------------------------------------------------------------------
    if st.button("Evaluate for CIDP Diagnosis and Management"):
        diagnosis_result, cidp_subtype, differentials_text, management_plan = evaluate_cidp(
            duration_months,
            symmetry,
            distribution_weakness,
            sensory_involvement,
            reflex_status,
            progression_pattern,
            other_causes,
            sensory_ataxia,
            csf_elevated,
            
            # Motor data (each is a tuple)
            median_motor_left,
            median_motor_right,
            ulnar_motor_left,
            ulnar_motor_right,
            radial_motor_left,
            radial_motor_right,
            tibial_motor_left,
            tibial_motor_right,
            peroneal_motor_left,
            peroneal_motor_right,

            # Sensory data (each is a tuple)
            median_sens_left,
            median_sens_right,
            ulnar_sens_left,
            ulnar_sens_right,
            radial_sens_left,
            radial_sens_right,
            sural_sens_left,
            sural_sens_right,
            superficial_peroneal_sens_left,
            superficial_peroneal_sens_right
        )

        st.subheader("D. Results")
        st.markdown(f"**Diagnosis Conclusion:** {diagnosis_result}")
        if "CIDP" in diagnosis_result:
            st.markdown(f"**Likely CIDP Subtype:** {cidp_subtype}")
        st.markdown(f"**Potential Differentials:**\n{differentials_text}")
        st.markdown(f"**Management Recommendations:**\n{management_plan}")


def evaluate_cidp(
    duration_months,
    symmetry,
    distribution_weakness,
    sensory_involvement,
    reflex_status,
    progression_pattern,
    other_causes,
    sensory_ataxia,
    csf_elevated,

    # Motor nerve data: (dml, cv, amplitude, duration, fwave, conduction_block)
    median_motor_left,
    median_motor_right,
    ulnar_motor_left,
    ulnar_motor_right,
    radial_motor_left,
    radial_motor_right,
    tibial_motor_left,
    tibial_motor_right,
    peroneal_motor_left,
    peroneal_motor_right,

    # Sensory nerve data: (dist_lat, cv, snap, duration)
    median_sens_left,
    median_sens_right,
    ulnar_sens_left,
    ulnar_sens_right,
    radial_sens_left,
    radial_sens_right,
    sural_sens_left,
    sural_sens_right,
    superficial_peroneal_sens_left,
    superficial_peroneal_sens_right
):
    # ----------------------------------------------------------
    # 1) CLINICAL SUSPICION (Simplified Scoring)
    # ----------------------------------------------------------
    clinical_points = 0

    # Duration ≥ 2 months
    if duration_months >= 2:
        clinical_points += 1

    # Reflexes
    if reflex_status in ["Reduced", "Absent"]:
        clinical_points += 1

    # Progression
    if progression_pattern in ["Slowly Progressive", "Stepwise Progressive", "Recurrent/Relapsing"]:
        clinical_points += 1

    # No alternative full explanation
    if other_causes == "No":
        clinical_points += 1

    # We'll consider ≥ 3 as strong clinical suspicion
    clinical_suspicion = (clinical_points >= 3)

    # ----------------------------------------------------------
    # 2) ELECTROPHYSIOLOGY (Demyelination Criteria)
    #    We check all 10 nerves on both sides. 
    #    For each motor nerve: check for demyelinating features.
    #    For each sensory nerve: check for demyelinating features.
    # ----------------------------------------------------------
    # Normal reference thresholds (approx). 
    # These can vary by nerve, but here we define general cutoffs for demonstration.
    # You can fine-tune them per nerve in a dictionary if desired.

    # Motor thresholds (generic):
    normal_motor_dml = 4.2
    normal_motor_cv = 50.0
    normal_motor_duration = 9.0
    normal_motor_fwave = 32.0

    # Sensory thresholds (generic):
    normal_sens_distal_latency = 3.5
    normal_sens_cv = 45.0
    normal_sens_duration = 10.0

    # We'll define a function that checks motor demyelination:
    def motor_demyelinated(dml, cv, duration, fwave, conduction_block):
        abnormal_dml = (dml > normal_motor_dml)
        abnormal_cv = (cv < 0.9 * normal_motor_cv)
        abnormal_duration = (duration > 1.3 * normal_motor_duration)
        abnormal_fwave = (fwave > normal_motor_fwave or fwave == 0.0)  # 0 indicates absent
        abnormal_block = (conduction_block == "Yes")

        # If any feature suggests demyelination, we count that nerve
        return any([abnormal_dml, abnormal_cv, abnormal_duration, abnormal_fwave, abnormal_block])

    # We'll define a function that checks sensory demyelination:
    def sensory_demyelinated(dist_lat, cv, duration):
        abnormal_dist_lat = (dist_lat > normal_sens_distal_latency)
        abnormal_cv = (cv < 0.9 * normal_sens_cv)
        abnormal_duration = (duration > 1.3 * normal_sens_duration)
        return any([abnormal_dist_lat, abnormal_cv, abnormal_duration])

    # Unpack motor data:
    # median_motor_left/right = (dml, cv, amplitude, duration, fwave, conduction_block), etc.
    motor_nerves_data = [
        median_motor_left, median_motor_right,
        ulnar_motor_left, ulnar_motor_right,
        radial_motor_left, radial_motor_right,
        tibial_motor_left, tibial_motor_right,
        peroneal_motor_left, peroneal_motor_right
    ]

    motor_demyelinated_count = 0
    for m in motor_nerves_data:
        dml, cv_m, amp, dur, fw, cb = m
        if motor_demyelinated(dml, cv_m, dur, fw, cb):
            motor_demyelinated_count += 1

    # Unpack sensory data:
    # median_sens_left/right = (dist_lat, cv, snap, duration), etc.
    sensory_nerves_data = [
        median_sens_left, median_sens_right,
        ulnar_sens_left, ulnar_sens_right,
        radial_sens_left, radial_sens_right,
        sural_sens_left, sural_sens_right,
        superficial_peroneal_sens_left, superficial_peroneal_sens_right
    ]

    sensory_demyelinated_count = 0
    for s in sensory_nerves_data:
        dist_lat, cv_s, snap, dur = s
        if sensory_demyelinated(dist_lat, cv_s, dur):
            sensory_demyelinated_count += 1

    total_demyelinated_nerves = motor_demyelinated_count + sensory_demyelinated_count

    # EFNS/PNS typically requires demyelinating features in ≥ 2 nerves for typical CIDP
    # (motor ± sensory). This is a simplified approach.
    ncs_criteria_met = (total_demyelinated_nerves >= 2)

    # ----------------------------------------------------------
    # 3) CSF PROTEIN SUPPORT
    # ----------------------------------------------------------
    # Elevated CSF protein > 45 mg/dL is supportive but not mandatory.
    # We'll just track it as an additional supportive factor.
    if csf_elevated:
        csf_support = True
    else:
        csf_support = False

    # ----------------------------------------------------------
    # 4) DIAGNOSTIC DECISION
    # ----------------------------------------------------------
    # For a simplified approach:
    #   - "CIDP (Definite)" if clinical suspicion AND NCS demyelination are met, plus CSF support
    #   - "CIDP (Probable)" if clinical suspicion AND NCS demyelination are met, but no CSF support
    #   - "Possible CIDP" if clinical suspicion but insufficient NCS
    #   - "Unlikely CIDP" if not meeting these criteria

    if clinical_suspicion and ncs_criteria_met:
        if csf_support:
            diagnosis_result = "CIDP (Definite by EFNS/PNS 2021 criteria)."
        else:
            diagnosis_result = "CIDP (Probable by EFNS/PNS 2021 criteria)."
    elif clinical_suspicion and not ncs_criteria_met:
        diagnosis_result = "Possible CIDP (Clinical suspicion but insufficient NCS evidence)."
    else:
        diagnosis_result = "CIDP unlikely based on EFNS/PNS criteria."

    # ----------------------------------------------------------
    # 5) CIDP SUBTYPE (If Applicable)
    # ----------------------------------------------------------
    cidp_subtype = "Not Applicable"
    if "CIDP" in diagnosis_result:
        proximal_involved = any("Proximal" in dist for dist in distribution_weakness)
        distal_involved = any("Distal" in dist for dist in distribution_weakness)

        if symmetry == "Symmetrical":
            if (distal_involved and not proximal_involved) and (sensory_involvement != "Pure Motor (No Sensory)"):
                cidp_subtype = "DADS (Distal Acquired Demyelinating Symmetric Neuropathy)"
            elif (proximal_involved or distal_involved) and (sensory_involvement != "Pure Motor (No Sensory)"):
                cidp_subtype = "Typical CIDP (Symmetrical Proximal and Distal)"
            elif sensory_involvement == "Pure Motor (No Sensory)":
                cidp_subtype = "Pure Motor CIDP"
            else:
                cidp_subtype = "Typical CIDP"
        elif symmetry == "Asymmetrical":
            cidp_subtype = "MADSAM (Lewis-Sumner Syndrome, Multifocal Asymmetric)"
        elif symmetry == "Focal":
            cidp_subtype = "Focal CIDP Variant"
        else:
            cidp_subtype = "Atypical CIDP Variant"

    # ----------------------------------------------------------
    # 6) DIFFERENTIAL DIAGNOSES
    # ----------------------------------------------------------
    # Key differentials typically include:
    #   - Multifocal Motor Neuropathy (especially if purely motor, conduction block in arms)
    #   - Diabetic Neuropathy
    #   - Hereditary demyelinating neuropathies (e.g., CMT)
    #   - Paraproteinemic neuropathy, POEMS, IgM anti-MAG neuropathy
    #   - Vasculitic neuropathy, other inflammatory neuropathies, etc.

    differentials_text = (
        "• Multifocal Motor Neuropathy\n"
        "• Diabetic or Metabolic Polyneuropathy\n"
        "• Hereditary Neuropathies (e.g. CMT)\n"
        "• Paraproteinemic Neuropathy / POEMS Syndrome / IgM anti-MAG\n"
        "• Vasculitic Neuropathy\n"
        "• Other Inflammatory or Toxic Neuropathies"
    )

    # ----------------------------------------------------------
    # 7) MANAGEMENT RECOMMENDATIONS
    # ----------------------------------------------------------
    if "CIDP" in diagnosis_result:
        management_plan = (
            "1) First-Line Options:\n"
            "   • IVIG (2 g/kg over 2–5 days, then maintenance doses)\n"
            "   • High-Dose Corticosteroids (oral or IV)\n"
            "   • Plasma Exchange (alternative in certain cases)\n\n"
            "2) If Inadequate Response:\n"
            "   • Repeat or increase frequency of IVIG\n"
            "   • Combine IVIG with steroids\n"
            "   • Alternate immunotherapies\n\n"
            "3) Refractory CIDP:\n"
            "   • Immunosuppressants (Azathioprine, Mycophenolate, Cyclophosphamide)\n"
            "   • Rituximab or other biologics in selected cases\n\n"
            "4) Supportive Care:\n"
            "   • Physical/Occupational Therapy\n"
            "   • Monitor for treatment side effects\n"
            "   • Regular neurological follow-up"
        )
    else:
        management_plan = (
            "Not consistent with CIDP based on current data. Further diagnostic workup or\n"
            "treatment should follow the most likely alternative diagnosis."
        )

    return diagnosis_result, cidp_subtype, differentials_text, management_plan


if __name__ == "__main__":
    main()

