# Project Proposal: The AI-Powered Solar Advisor

**Hook:** For millions of Nigerians, investing in solar energy is a high-stakes gamble filled with uncertainty. Our platform replaces that gamble with data-driven confidence, acting as a trusted AI advisor to guide every user to their perfect solar solution.

---

### 1. Executive Summary

This document outlines the architecture and implementation plan for an AI-Powered Solar Recommendation Platform, a sophisticated multi-agent system designed to de-risk and simplify the process of adopting solar energy in Nigeria. The platform will function as an unbiased advisor, guiding users from initial curiosity to a final, optimized system recommendation and a safe connection with vetted installers. It leverages a modern tech stack (FastAPI, MongoDB, React) and an advanced AI core, including a multi-LLM strategy for user interaction and a two-stage machine learning pipeline for providing objective, data-driven hardware recommendations. The system's key competitive advantage is its "Data Flywheel," a mechanism to capture proprietary data on component performance and market trends, allowing the platform to become progressively smarter and more accurate over time. We have already completed the full architectural design and a functional "walking skeleton" prototype, proving the viability of the core technology.

---

### 2. Target Audience

The platform serves two primary audiences:

*   **Primary Audience (End-Users):** Nigerian households and small-to-medium-sized enterprises (SMEs) who are considering investing in solar energy but lack the technical expertise to make an informed decision. They are budget-conscious and risk-averse.
*   **Secondary Audience (Installers):** Qualified, professional solar installers across Nigeria. The platform will serve as a valuable source of highly-qualified, educated customer leads, saving them marketing costs and connecting them with clients who understand the value of professional installation.

---

### 3. Data Acquisition Strategy

The platform's intelligence is dependent on a robust data pipeline. We will employ a two-phase strategy to build our core dataset:

*   **Phase 1: Initial Data Enrichment (Cold Start Solution):** We will deploy a targeted web scraping agent to gather data from major Nigerian e-commerce and supplier websites. The goal is not to get perfect specs, but to generate proxy metrics for **component popularity** and **supply chain availability** by counting listings and sellers. This provides an initial, data-driven foundation for our "Practicality Score".
*   **Phase 2: The "Data Flywheel" (Long-Term Competitive Advantage):** The platform itself is designed to become our primary source of proprietary data. We will build features to:
    *   **Capture Installer Feedback:** Collect structured feedback from our vetted installers on component reliability and ease of installation after a job is complete.
    *   **Log Transaction Data:** Record which specific components are quoted and chosen in real-world projects, giving us the most accurate market data possible.

---

### 4. Methodology

The platform is built on a modular, multi-agent architecture orchestrated by a **Super-Agent**.

1.  **User Interaction:** A user interacts with the system via a **Conversational Chatbot (powered by Groq for speed)** or a manual UI. The **Interaction Agent** gathers their needs (appliances, location, budget, etc.).
2.  **Geo-Spatial Analysis:** The **Geo-Agent** receives the user's location, parses it, and calculates the precise solar irradiance (Peak Sun Hours) for that location, accounting for seasonal variations (Dry vs. Rainy).
3.  **System Sizing:** The **Sizing Agent** takes the user's energy requirements and the geo-data to calculate the necessary technical specifications (e.g., total panel wattage, battery capacity, inverter size).
4.  **Recommendation Engine:** The **Recommendation Agent** uses a two-stage ML pipeline:
    *   **Model 1 (Scoring):** An automated pipeline (testing **RandomForest** first, then **XGBoost**) assigns objective scores (`Technical`, `Value`, `Practicality`) to all ~5,000 components in our database.
    *   **Model 2 (Recommending):** A **k-Nearest Neighbors (KNN)** model takes the user's required specs and finds the top 3 best-matching system combinations from the scored components.
5.  **Q&A and Installer Connection:** A **Q&A Agent** (using a RAG model) is available to answer user questions. The final recommendations are then passed to the **Marketplace Agent**, which manages the safe and transparent **Request for Quote (RFQ)** process with vetted installers.

---

### 5. Evaluation Metrics

To ensure a "perfect system," we will rigorously evaluate our models:

*   **Scoring Model (Regression Task):**
    *   **Mean Absolute Error (MAE):** To measure the average error of our score predictions.
    *   **R-squared (R²):** To measure how well the model explains the variance in scores.
*   **Recommendation Model (Ranking Task):**
    *   **Precision@k:** To measure how many of the top 'k' (e.g., 3) recommended systems are relevant.
    *   **nDCG (normalized Discounted Cumulative Gain):** To measure the quality of the ranking, ensuring the absolute best results are at the very top.

---

### 6. Expected Outcome and Deliverables

*   **Outcome:** A trusted, intelligent, and unbiased web platform that empowers Nigerians to confidently invest in solar energy, while providing high-quality leads to professional installers.
*   **Key Deliverables:**
    1.  A production-ready **FastAPI Backend** hosting the multi-agent system.
    2.  A polished **React Frontend** providing the chatbot and manual UI.
    3.  A **Streamlit Prototype** for internal testing and rapid iteration.
    4.  A **MongoDB Database** containing our enriched and ever-growing dataset of solar components.
    5.  A suite of trained and evaluated **ML models** for scoring and recommendation.
    6.  A curated **Knowledge Base** for the RAG-powered Q&A Agent.

---

### 7. Project Timeline (High-Level Estimate)

This timeline is an estimate and can be adjusted.

*   **Phase 1: Foundational Implementation (4 Weeks)**
    *   **Week 1:** Implement and test the Data Preparation Agent and the initial data scraping/cleaning pipeline.
    *   **Week 2:** Implement the full logic for the Geo-Agent and System Sizing Agent.
    *   **Week 3-4:** Build and train the first versions of the Scoring (RandomForest) and Recommendation (KNN) models.
*   **Phase 2: Prototyping & Integration (3 Weeks)**
    *   **Week 5-6:** Develop the Streamlit prototype, integrating all backend agents to create the first fully interactive version of the application.
    *   **Week 7:** Internal testing, debugging, and refinement based on prototype usage.
*   **Phase 3: Production Frontend & Launch (5 Weeks)**
    *   **Week 8-10:** Develop the production-grade React frontend.
    *   **Week 11:** Final integration of the React frontend with the FastAPI backend.
    *   **Week 12:** Final testing, deployment, and preparation for a beta launch.

**Total Estimated Timeline:** 12 Weeks.
