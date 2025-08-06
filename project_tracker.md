# ML Feature Store & Customer Attrition Model – Sprint Tracker

- **Project Duration:** Aug 4, 2025 – Oct 26, 2025  
- **Sprint Length:** 2 weeks  
- **Project Goal:** Build a production-ready ML feature store and a customer attrition prediction model.

---

## Overall Sprint Schedule

| Sprint | Dates            | Focus                                              |
|--------|------------------|----------------------------------------------------|
| 1      | Aug 4 – Aug 17   | Onboarding, initial meetings, access requests, env setup |
| 2      | Aug 18 – Aug 31  | Infra setup, data intake, data quality assessment |
| 3      | Sep 1 – Sep 14   | Feature engineering, snapshot and churn logic, data QC |
| 4      | Sep 15 – Sep 28  | Baseline churn model training + evaluation        |
| 5      | Sep 29 – Oct 12  | Model & feature tuning, SHAP explainability, customer segmentation |
| 6      | Oct 13 – Oct 26  | Final validation, pipeline automation, demo & handoff   |

---

## Project Progress Summary

| Sprint | Status         | % Complete | Notes                          |
|--------|----------------|------------|--------------------------------|
| 1      | 🔄 In Progress  | 50%       | Waiting on IT                  |
| 2      | ⏳ Not Started  | 0%        |                                |
| 3      | ⏳ Not Started  | 0%        |                                |
| 4      | ⏳ Not Started  | 0%        |                                |
| 5      | ⏳ Not Started  | 0%        |                                |
| 6      | ⏳ Not Started  | 0%        |                                |

✅🔄⏳

---

## Sprint 1 – Onboarding, Access, and Setup *(Aug 4–Aug 17)*

### Sprint Goals
- [x] Initial meeting clarifying expectations and intial plan 
- [~] Gather and request access to necessary systems and tools
    - [~] Confluence (Keystone & Data Services)
    - [~] Github
    - [~] Database (LADYSIF & Redshift)
    - [ ] AWS Glue & Sagemaker
    - [x] DBeaver
- [ ] Set up dev environment
    - [x] Terminal, Python + packages, VSCode, Jupyter
- [ ] Set up repo, version control, and initial folder structure 
- [ ] Explore different feature store options (Manually created Redshift or Sagemaker)

### Weekly Check-In *(Aug 7 & Aug 15)*
- **Progress Summary:**  
- **Blockers / Risks Identified:**  
- **Adjustments Made:**  

### End of Sprint Debrief
- **Completed Work:**  
- **Work Pushed to Next Sprint:**  
- **Key Learnings:**  
- **Next Sprint Priorities:**  

---

## Sprint 2 – Infra Setup, Data Intake, and Data Processing *(Aug 18–Aug 31)*

### Sprint Goals
- [ ] Define data sources and access method (AWS Glue + PySpark)
    - [ ] Develop master config and python class for Spark session and DB connections
- [ ] Draft feature store schema
- [ ] Define SQL query/joins for main data ingestion
    - [ ] Customer + Account Data
    - [ ] Transaction Data
    - [ ] Interaction Data
    - [ ] Send final query/schema to Vineeta and team for table creation (feature store)
- [ ] Develop a DataIngestionService() in PySpark  
    - [ ] Join/Ingest raw tables into feature store staging and perform quality checks
    - [ ] Implement point-in-time joins for first feature group  
- [ ] Plan for high-impact data to be used in churn definition.

### Weekly Check-In *(Aug 20 & Aug 28)*
- **Progress Summary:**  
- **Blockers / Risks Identified:**  
- **Adjustments Made:**  

### End of Sprint Debrief
- **Completed Work:**  
- **Work Pushed to Next Sprint:**  
- **Key Learnings:**  
- **Next Sprint Priorities:**  

---

## Sprint 3 – Feature Engineering *(Sep 1-Sep 14)*

### Sprint Goals
- [ ] Develop FeatureEngineeringService()
    - [ ] _get_eligible_customers() (minumum tenure, only data up until churn event, etc)
    - [ ] Generate customer snapshots
    - [ ] Add time-window aggregations (e.g. 30/60/90 day summaries) 
- [ ] Define & document input-output data contract (schema enforcement and partition strategy)
    - [ ] Start Feature Store data dictionary documentation (markdown >> Confluence)
- [ ] Choose feature store snapshot frequency
- [ ] Draft churn definition with input from stakeholders/domain experts
- [ ] Develop generate_churn_label() function using lookahead window
    - [ ] Create reference document on decision-making and functionality
- [ ] Validate data output with sample customers 
- [ ] Feature store creation (with historical backfill for initial setup)
- [ ] Exploratory Data Analysis with data distribution and correlation focus

### Weekly Check-In *(Sep 5 & Sep 12)*
- **Progress Summary:**  
- **Blockers / Risks Identified:**  
- **Adjustments Made:**  

### End of Sprint Debrief
- **Completed Work:**  
- **Work Pushed to Next Sprint:**  
- **Key Learnings:**  
- **Next Sprint Priorities:**  

---

## Sprint 4 – Model Development *(Sep 15–Sep 28)*

### Sprint Goals
- [ ] Set up model training and evaluation pipeline
    - [ ] Develop ModelTrainingService()
        - [ ] Automate hyperparameter selection
    - [ ] Develop ModelEvaluationService()
    - [ ] Develop ModelInferenceService()
- [ ] Compare model performance across parameter changes (feature windows, churn definitions, prediction horizon)
- [ ] Define model metadata storage needs (versioning, parameters)
- [ ] Store predictions in feature store or model registry table

### Weekly Check-In *(Sep 19 & Sep 26)*
- **Progress Summary:**  
- **Blockers / Risks Identified:**  
- **Adjustments Made:**  

### End of Sprint Debrief
- **Completed Work:**  
- **Work Pushed to Next Sprint:**  
- **Key Learnings:**  
- **Next Sprint Priorities:**  

---

## Sprint 5 – Pipeline Tuning, SHAP explainability, and Customer Segmenation *(Sep 29–Oct 12)*

### Sprint Goals
- [ ] Final model and feature tuning
- [ ] Develop feature importance and SHAPExplainabilityService()
- [ ] Perform customer segmentation (UMAP/PCA + HDBSCAN)
    - [ ] Automate or set parameter selection based on heuristics
    - [ ] Store cluster IDs in feature store or model registry
    - [ ] Store SHAP values in feature store or model registry
    - [ ] Output timestamped-versioned global feature importances
- [ ] Create model pipeline documentation, including parameter definitions and explanation
- [ ] Create SHAP Feature Importance documentation

### Weekly Check-In *(Oct 3 & Oct 9)*
- **Progress Summary:**  
- **Blockers / Risks Identified:**  
- **Adjustments Made:**  

### End of Sprint Debrief
- **Completed Work:**  
- **Work Pushed to Next Sprint:**  
- **Key Learnings:**  
- **Next Sprint Priorities:**  

---

## Sprint 6 – Final Validation, Pipeline Automation, Demo & Handoff  *(Oct 13–Oct 26)*

### Sprint Goals
- [ ] Final model validation
- [ ] Define pipeline component latencies and complete pipeline automation setup
- [ ] Revisit all documentation and final polish
- [ ] Pipeline walkthrough/demo and knowledge transfer

### Weekly Check-In *(Oct 17 & Oct 24)*
- **Progress Summary:**  
- **Blockers / Risks Identified:**  
- **Adjustments Made:**  

### End of Sprint Debrief
- **Completed Work:**  
- **Work Pushed to Next Sprint:**  
- **Key Learnings:**  
- **Next Sprint Priorities:**  