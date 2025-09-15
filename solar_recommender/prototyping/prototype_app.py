import streamlit as st

st.title("AI-Powered Solar Recommendation Platform (Prototype)")

st.header("User Input")

# --- User Input Section ---
user_location = st.text_input("Enter your location (e.g., 'Lagos, Nigeria'):")
user_budget = st.number_input("What is your budget (in NGN)?", min_value=0)
# TODO: Add more input fields for appliances, usage, autonomy days, etc.

if st.button("Get Recommendation"):
    if user_location and user_budget > 0:
        st.info("Sending request to the Super-Agent...")

        # --- Agent Workflow ---
        # In a real scenario, this would call our backend/Super-Agent
        # from app.agents.super_agent import super_agent
        # response = super_agent.process(...)

        # --- Dummy Response ---
        st.success("Recommendation received!")
        st.subheader("Top Recommended System")
        st.json({
            "system_score": 0.95,
            "components": {
                "panels": "Brand A - 450W Mono Panel (x12)",
                "battery": "Brand B - 10kWh Lithium-ion",
                "inverter": "Brand C - 5kVA Hybrid Inverter"
            },
            "estimated_cost": "₦1,450,000"
        })

        st.subheader("Why this system?")
        st.write("This system was selected for its high efficiency and excellent 10-year warranty, offering the best long-term value within your budget.")

    else:
        st.error("Please provide your location and budget.")
