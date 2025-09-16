# ML Feature Store & Customer Attrition Model – Sprint Tracker

- **Project Duration:** Aug 4, 2025 – Oct 26, 2025  
- **Sprint Length:** 2 weeks  
- **Project Goal:** Build a production-ready ML feature store and a customer attrition prediction model.

---

## Overall Sprint Schedule

| Sprint | Dates            | Focus                                              |
|--------|------------------|----------------------------------------------------|
| 1      | Aug 4 – Aug 17   | **Foundation Setup** - Onboarding, initial meetings, access requests, env setup |
| 2      | Aug 18 – Aug 31  | **Data Infrastructure** - Infra setup, data intake, data quality assessment |
| 3      | Sep 1 – Sep 14   | **Feature Engineering** - Feature engineering, snapshot and churn logic, data QC |
| 4      | Sep 15 – Sep 28  | **Model Development** - Baseline churn model training + evaluation        |
| 5      | Sep 29 – Oct 12  | **Model Enhancement** - Model & feature tuning, SHAP explainability, customer segmentation |
| 6      | Oct 13 – Oct 26  | **Production Deployment** - Final validation, pipeline automation, demo & handoff   |

---

## Project Progress Summary

| Sprint | Status         | % Complete | Notes                          |
|--------|----------------|------------|--------------------------------|
| 1      | ✅ Complete     | 95%       | AWS Setup pending with Jake Jones |
| 2      | ✅ Complete     | 95%       | Feature engineering and data processing complete, interaction data not included in feature set |
| 3      | 🔄 In Progress  | 65%       | ETL infrastructure, churn logic, and data validation in progress |
| 4      | ⏳ Not Started  | 0%        |                                |
| 5      | ⏳ Not Started  | 0%        |                                |
| 6      | ⏳ Not Started  | 0%        |                                |

✅🔄⏳

---

## Sprint Task Status  
<img src="https://github.com/chill0121/project_tracker/blob/main/assets/sprint_status_chart.png?raw=true" alt="Sprint Status" width="700">

---

## Key Deliverables & Milestones

| Sprint | Deliverable | Stakeholder Value | Demo Date |
|--------|-------------|-------------------|-----------|
| 2 | Feature Store Schema & Data Pipeline Architecture | Data architecture clarity | Aug 28 |
| 3 | Production Feature Store & Churn Definition | Reusable ML infrastructure, standardized customer churn logic | Sep 12 |
| 4 | Baseline Churn Prediction Model | First working churn predictions, performance benchmarks | Sep 26 |
| 5 | Model Explainability & Customer Segmentation | Business-interpretable insights, targeted customer strategies | Oct 9 |
| 6 | Production-Ready ML Pipeline | Automated churn detection system, knowledge transfer complete | Oct 24 |

---

## 🔄 Sprint 1: Foundation Setup – Onboarding, Access, and Setup *(Aug 4–Aug 17)*

### Sprint Goals
- [x] Initial meeting clarifying expectations and intial plan 
- [x] Gather info and request access to necessary systems and tools
    - [x] Confluence (Keystone & Data Services)
    - [x] Github
    - [x] Database (LADYSIF & Redshift)
    - [x] AWS Glue & Sagemaker
    - [x] DBeaver
- [x] Create, deploy, and share project tracker
- [x] Set up dev environment
    - [x] Terminal, Python + packages, VSCode, Jupyter
- [x] Set up repo, version control, and initial folder structure 
- [x] Explore different feature store options (Manually created S3 or Sagemaker)

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

## 🔄 Sprint 2: Data Infrastructure – Infra Setup, Data Intake, and Data Processing *(Aug 18–Aug 31)*

### Sprint Goals
- [x] Define data sources and access method (AWS Glue + PySpark)
- [x] Define SQL query/joins for main data ingestion
    - [x] Customer + Account Data
    - [x] Transaction Data
    - [ ] Interaction Data
    - [x] Join/Ingest raw tables into feature store staging and perform quality checks
    - [x] Implement point-in-time joins for first feature group
- [x] Plan for high-impact data to be used in churn definition
- [x] Complete demographic/account feature engineering (advanced from Sprint 3)
- [x] Meet with Jake Jones to align on system needs, pipeline endpoints, and timeline
- [x] Begin transaction feature engineering development 
    - [x] Add time-window aggregations (e.g. 30/60/90 day summaries)
- [x] Draft feature store schema (~200 features Customer+Acct+Transaction)
    - [x] Generate customer snapshots
- [x] Validate data output with sample customers (100)

### Weekly Check-In *(Aug 20 & Aug 28)*
- **Progress Summary:** Completed customer/demographic data ingestion and advanced feature engineering. 80% complete on transaction data ingestion. Sprint 2/3 hybrid approach proving effective.
- **Blockers / Risks Identified:** Minor balance discrepancies in transaction data, AWS Glue setup coordination
- **Adjustments Made:** Advanced feature engineering while data structure was fresh, reshuffled Sprint 2/3 tasks for better flow.

### End of Sprint Debrief
- **Completed Work:** Core feature engineering, SQL-based data processing, feature schema design
- **Work Pushed to Next Sprint:**
- **Key Learnings:** Early feature engineering while data structure was fresh was a better workflow.
- **Next Sprint Priorities:** Focus on PySpark conversion and production pipeline development

---

## 🔄 Sprint 3: ETL Infrastructure & Production Pipeline *(Sep 1-Sep 14)*

### Sprint Goals
- [x] Advanced feature engineering (completed early in Sprint 2)
    - [x] Derive demographic and account features (156 features)
    - [x] Add time-window aggregations
- [x] Define & document input-output data contract (schema enforcement and partition strategy)
    - [x] Start Feature Store data dictionary documentation (markdown >> Confluence)
- [x] Convert SQL work to PySpark + AWS Glue for automated ETL
    - [x] Develop master config and python class for Spark session and DB connections
    - [x] Choose feature store snapshot frequency
- [x] Implement initial historical backfill operation
- [x] Build automated data validation checks and logging with broader population (beyond 100-person samples)
- [~] Draft churn definition with input from stakeholders/domain experts
- [x] Develop generate_churn_label() function using lookahead window
    - [x] _get_eligible_customers() (minimum tenure, only data up until churn event, etc)
    - [x] Create reference documents on decision-making and functionality
- [~] Feature store creation in S3
    - [~] Execute historical backfill ETL for 3-month training dataset
    - [~] Configure automated ETL scheduling (EventBridge?)
- [~] Exploratory Data Analysis with data distribution and correlation focus
- [~] Validate churn criteria with business stakeholders (schedule meeting)
- [~] Test full population data processing (beyond sample validation)
- [~] Refine data quality scoring and drift detection 

### Weekly Check-In *(Sep 5 & Sep 12)*
- **Progress Summary:** AWS Glue ETL infrastructure bagan, feature store schema set, churn logic framework in progress
- **Blockers / Risks Identified:** Churn criteria need stakeholder validation, EDA pending, S3 still not deployed for testing
- **Adjustments Made:** Sprint 2/3 hybrid approach - feature engineering advanced early to maintain momentum

### End of Sprint Debrief
- **Completed Work:**  
- **Work Pushed to Next Sprint:**  
- **Key Learnings:** 
- **Next Sprint Priorities:** 

---

## ⏳ Sprint 4: Model Development *(Sep 15–Sep 28)*

### Sprint Goals
- [~] Feature selection and dimensionality analysis
    - [x] Create feature exclusion list
    - [ ] Correlation analysis and multicollinearity detection
    - [ ] Feature importance baseline using simple models
    - [ ] Identify optimal feature subset for model training
- [~] Baseline churn prediction model development
    - [ ] XGBoost model implementation with default parameters
    - [~] Logistic regression benchmark model
    - [~] Cross-validation framework (5-fold stratified?)
    - [~] Model evaluation metrics (precision, recall, F1, AUC-ROC)
- [~] Model training and evaluation pipeline
    - [x] Automated train/validation/test split with temporal and customer-level considerations
    - [~] Model performance comparison framework
    - [ ] Prediction storage in feature store with model versioning
- [ ] Initial hyperparameter optimization
    - [ ] Grid search for key XGBoost parameters
    - [ ] Learning curve analysis for optimal training data size
- [~] Model metadata and versioning system
    - [~] Track model parameters, performance metrics, and training data versions
    - [~] Integration with feature store versioning

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

## ⏳ Sprint 5: Model Enhancement – Pipeline Tuning, SHAP explainability, and Customer Segmenation *(Sep 29–Oct 12)*

### Sprint Goals
- [ ] Advanced model optimization and tuning
    - [ ] Bayesian hyperparameter optimization (Optuna or similar)
    - [ ] Feature engineering iteration based on model insights
    - [ ] Class imbalance handling (SMOTE, class weights, threshold tuning)
    - [ ] Model ensemble evaluation (XGBoost + XGBoost(Cluster_Features) + Logistic Regression)
- [ ] SHAP explainability framework implementation
    - [ ] Global feature importance analysis across all customers
    - [ ] Individual customer prediction explanations
    - [ ] Feature interaction discovery and visualization
    - [ ] SHAP value storage in feature store with model lineage
    - [ ] Business-friendly explanation templates
- [ ] Customer segmentation analysis
    - [ ] UMAP/PCA dimensionality reduction for behavioral features
    - [ ] HDBSCAN clustering with automatic parameter selection
    - [ ] Segment characterization and churn risk profiling
    - [ ] Cluster assignment storage and versioning
    - [ ] Business insights and segment-specific model performance
- [ ] Model validation and business impact assessment
    - [ ] Performance analysis across customer segments
    - [ ] Cost-benefit analysis of churn intervention
    - [ ] Model stability testing across different time periods
    - [ ] A/B testing framework design for model deployment
- [ ] Documentation and knowledge transfer preparation
    - [ ] Model methodology documentation
    - [ ] SHAP interpretation guide for business stakeholders
    - [ ] Customer segmentation insights summary

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

## ⏳ Sprint 6: Production Deployment – Final Validation, Pipeline Automation, Demo & Handoff  *(Oct 13–Oct 26)*

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