# Responsible Data Card

## Dataset purpose
Supports the decision of predicting customer churn within 30 days. Must not be used for financial credit scoring, employment decisions, or any non-consensual profiling.

## Provenance and permission
Data collected from CRM system logs and subscription records. Consent obtained under service agreement. Usage restricted to educational purposes within RabTech Academy.

## Population and representation
Dataset includes 12 customers across Basic, Standard, and Pro plans. Basic plan users are overrepresented among churners. Small sample size limits generalization. Missing groups include enterprise customers and long-term premium users.

## Features and target
- tenure_months: subscription length
- support_tickets: number of support requests
- monthly_spend_inr: subscription cost
- last_login_days: days since last login
- plan_type: Basic, Standard, Pro
- churned: target label (1 = churn, 0 = retained)

No leakage identified. Sensitive proxies: plan_type may indirectly reflect income level. Customer_id anonymized to protect privacy.

## Quality checks
- Missingness: none
- Duplicates: none
- Outliers: high support tickets in Basic plan
- Class balance: churn rate ≈ 33%
- Train/test separation: temporal split recommended to avoid leakage

## Risks and safeguards
- Bias: Basic plan users churn more → fairness audit required
- Privacy: anonymize customer_id and restrict access
- Misuse: restrict dataset to academic use only
- False positives: wasted retention effort
- False negatives: lost revenue
- Safeguards: human review, fairness checks, rollback plan

## Intended evaluation
Baseline: majority class accuracy = 67%  
Performance: F1-score, AUC  
Calibration: reliability curves  
Fairness: churn prediction by plan type  
Error analysis: review misclassified cases
