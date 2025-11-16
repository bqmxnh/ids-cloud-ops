# IDS Cloud Ops

A complete cloud-native IDS system built with:

- FastAPI (Inference + Feedback + Metrics)
- Adaptive Random Forest (River)
- MLflow (Experiment Tracking)
- Helm Charts for deployment
- ArgoCD GitOps automation
- AWS EKS + ALB Ingress + S3 artifact store

## Components

### 📌 API
Located at:
api/
Features:
- /predict → real-time inference
- /feedback → incremental learning
- /metrics → Prometheus metrics
- Load model artifacts from S3

### 📌 Helm Charts
API → `charts/ids-api/`  
MLflow → `mlflow/charts/mlflow-server/`

### 📌 GitHub CI/CD
.github/workflows/
- Build API image → DockerHub  
- Auto update Helm chart

### 📌 ArgoCD Apps
apps/
- Automatically deploy API + MLflow to EKS

## Deployment Flow
Git Push → GitHub Actions → DockerHub → Helm chart update → ArgoCD auto sync → EKS

