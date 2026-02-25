# 🍔 Food Delivery Microservices - EKS Deployment Guide

This project demonstrates the deployment of a containerized Food Delivery Application on **Amazon EKS (Elastic Kubernetes Service)** using a microservices architecture and **AWS Application Load Balancer (ALB)**.

## 🚀 Project Overview

The project consists of multiple microservices (Menu and Order) that are orchestrated by Kubernetes. We utilize the **AWS Load Balancer Controller** to automatically provision an ALB, providing a single public entry point for users to access different services via path-based routing.

---

## 🛠️ Tasks Completed Today

Today, we successfully transitioned the application from a "Pending/Error" state to a "Live" state by performing the following steps:

1. **IAM Policy & Permission Update**:
* Updated the IAM Policy to version `v4` to ensure the AWS Load Balancer Controller has the latest permissions required to manage ALB listeners and target groups.


2. **Controller Optimization**:
* Re-associated the IAM Service Account and restarted the controller deployment to apply new permissions.
* Scaled the controller to 1 replica to optimize resource usage on smaller nodes.


3. **VPC Subnet Tagging**:
* Verified that public subnets are correctly tagged with `kubernetes.io/role/elb: 1`, allowing the controller to auto-discover them for public-facing load balancers.


4. **Resource & Node Scaling**:
* Identified a "Too many pods" error where nodes reached their maximum capacity.
* Increased the NodeGroup capacity by updating the **Max Size** from 3 to 5 and the **Desired Capacity** to 4 using `eksctl` and the AWS Console.


5. **Ingress & Connectivity**:
* Successfully generated the Application Load Balancer DNS.
* Resolved `503 Service Temporarily Unavailable` errors by ensuring pods moved from `Pending` to `Running` status.



---

## 📦 Services Added

The architecture currently supports the following services:

| Service Name | Container Port | Path Pattern | Responsibility |
| --- | --- | --- | --- |
| **Menu Service** | 5001 | `/menu` | Handles restaurant menu data and item listings. |
| **Order Service** | 5002 | `/order` | Manages user orders and checkout processes. |
| **ALB Controller** | N/A | N/A | Provisions and manages the AWS Application Load Balancer. |

---

## 🔍 Quick Reference Commands

* **Check Ingress Status**:
`kubectl get ingress`
* **Check Pod Status**:
`kubectl get pods`
* **Scale Node Group**:
`eksctl scale nodegroup --cluster=food-delivery-cluster --name=ng-975e022d --nodes=4`
* **Restart Controller**:
`kubectl rollout restart deployment aws-load-balancer-controller -n kube-system`

---

