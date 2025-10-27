---
title: Projects - Jérémy Goutin
---

[← Back to main page](../../index)

# Projects

This page presents a selection of significant projects completed throughout my career.

---

## Enterprise AI/LLM Platform
**July 2025 - August 2025**

Creation of a centralized solution to leverage LLM models while ensuring data governance.

Deployment of an LLM platform on AWS infrastructure. The core of this solution is a chatbot designed as the single, controlled access point to artificial intelligence capabilities. This chatbot ensures strict governance of model usage to protect company data.

The platform integrates advanced features such as RAG allowing models to provide enriched responses based on internal documents. The platform also provides development teams with the ability to integrate AI into their IDEs to generate and improve code.

The architecture relies on the AWS Bedrock service for access and management of a diverse portfolio of language models.

---

## GitLab Runners Migration to AWS Serverless Architecture
**March 2025 - June 2025**

Implementation of a dynamic and secure CI/CD infrastructure through GitLab runners integration with AWS ECS/Fargate and CodeBuild.

For generic tasks such as running Terraform, curl, or various linters, GitLab runners based on ECS Fargate ARM were deployed.

For compilation and build tasks specific to programming languages, GitLab runners leveraging AWS CodeBuild were implemented, taking advantage of native development environment support.

Security was enhanced by abandoning static AWS IAM access keys in favor of temporary, least-privilege IAM roles. Secret management, particularly for access to Docker registries and Maven and NPM repositories, was centralized and secured.

The benefits achieved include notable performance improvements, reduced wait times and job congestion through on-demand scalability, and significant operational cost optimization. Simplified pipeline configuration within gitlab-ci.yml files, and the ability to build Docker images for ARM64 architecture.

---

## AWS Infrastructure Standardization with Terraform
**October 2023 - October 2024**

Development of reference architectures via reusable Terraform modules to simplify, accelerate, and secure production deployments.

The main objective was to transition from an infrastructure historically centered on EC2 instances to a modern architecture fully leveraging AWS managed services (ECS, Aurora, Lambda, SQS, SES, ...).

This project focused on creating reusable and standardized Terraform modules.

These modules offer a streamlined interface designed to be accessible to non-experts, while encapsulating advanced and complex configuration.

Each module natively integrates security best practices, including fine-grained permission management with IAM (helping create least-privilege policies), network segmentation via security groups, systematic data encryption, and CloudWatch monitoring.

Benefits: Notable reduction in application deployment time, increased reliability through standardization, improved overall security posture, and simplified infrastructure maintenance. Adoption of DevOps processes by development teams.

---

## Multi-Account AWS Network Architecture with Shared VPC and Cost Optimization
**October 2023 - April 2024**

Complete overhaul of distributed network infrastructure to centralize management and significantly reduce operational costs.

This project involved restructuring a multi-account AWS architecture by replacing an expensive Transit Gateway with a solution based on AWS Resource Access Manager (RAM). The centralized approach uses a single VPC hosted in a dedicated account, with specialized subnet sharing to project accounts via AWS RAM.

The architecture segments environments into distinct isolation zones (public, private, etc.) while pooling critical resources: VPC endpoints, NAT Gateway, and other network components. This consolidation eliminates resource duplication and optimizes internal IPv4 range allocation.

Security relies on a least-privilege strategy with Network Access Control Lists (NACL) and least-privilege Security Groups. AWS Network Firewall and Route 53 Resolver Firewall provide global perimeter protection. The infrastructure supports dual-stack IPv4/IPv6.

Inter-project communications and communications with on-premise infrastructure are standardized via configurable centralized routing. Observability is performed centrally with CloudWatch.

The infrastructure is entirely managed as IaC with Terraform, with direct integration into existing enterprise modules. This approach standardizes deployment and simplifies adoption by technical teams.

Benefits include substantial infrastructure cost reduction, operational simplification, enhanced security, and significant reduction of network technical debt.

---

## FPGA Marketplace with Cloud-Native Architecture
**November 2021 - April 2023**

Cloud architecture & software for a specialized platform for distributing FPGA applications, integrating advanced license management, different billing models (subscription, pay-per-use), and hosting application resources such as Linux packages and documentation.

Cloud infrastructure fully automated via Terraform: backend on AWS with EC2, Aurora Serverless, Application Load Balancer, autoscaling, and Global Accelerator. Frontend distributed with Amazon S3 and CloudFront. Set of Python microservices operating on AWS Lambda, interfacing with DynamoDB, SQS, SNS, and notification management via SES. Centralized authentication via Amazon Cognito and real-time monitoring provided by CloudWatch. EC2 image construction with Ansible and Packer.

SQL (PostgreSQL via SQLAlchemy core) and NoSQL (DynamoDB) data models. Main backend built with Python/FastAPI.

Integration of automated tests covering all business flows. Complete CI/CD pipeline automation with Azure Pipelines. Promotion of DevOps best practices.

Migration from a previous version with backward compatibility management.

Benefits include high availability, enhanced security, optimized cost management, and significantly accelerated deployment and maintenance.

---

## Highly Available Linux Repository Manager with CI/CD Integration and API
**October 2021 - March 2022**

Highly available DEB and RPM package distribution solution, integrating addition flows from CI/CD and via a dedicated web API.

Architecture entirely based on AWS serverless components: artifact storage on S3, distribution via CloudFront, processing triggered by S3 Event Notifications, business script execution in AWS Lambda.

Development of a Python library optimized for Lambda, responsible for dynamic package metadata modification and automated cryptographic signature management.

Addition of Accelize packages via continuous integration, secure management of client and partner packages via REST API.

Main benefits: high availability, complete automation of package addition and validation flow, integrity and security ensured by systematic signing, ease of integration via API and CI/CD.

---

## Containerized FPGA Application Execution Service in Hybrid Cloud
**June 2021 - October 2021**

Implementation of a cloud service for on-demand execution of containerized applications on FPGA instances from product web pages.

The architecture relies on a 100% serverless backend and orchestrator, leveraging AWS Lambda, S3, SQS, CloudFront, and ECR services. This infrastructure drives application deployment on heterogeneous execution instances, supporting a multi-cloud environment including Amazon EC2 and OpenStack Nova.

The project addressed several major technical constraints. For cost control, an automatic provisioning and termination mechanism for FPGA instances was developed. Multi-cloud compatibility was ensured through a software abstraction layer. Using containerized applications with Docker required specific Linux host configurations to enable interaction between the container and FPGA hardware. The platform also guarantees execution security and confidentiality, even for public sessions launched without authentication.

The benefits achieved include high scalability and cost optimization through automation of instance lifecycle. The service offers a secure and flexible infrastructure capable of supporting public product demonstrations directly from web pages.

---

## ACID: Dynamic Cloud Agents for Azure Pipelines
**June 2021**

Execution of Azure Pipelines jobs on ephemeral agents provisioned on-demand on AWS EC2 and Azure VM.

Development of a utility enabling Azure Pipelines jobs to run on self-hosted agents created on temporary cloud instances. The tool leverages Terraform to automate resource provisioning and deletion on AWS EC2 and Azure Virtual Machines. Agent software configuration is handled by Ansible playbooks, offering complete execution environment customization.

The agent lifecycle is entirely managed within the pipeline. An instance is started just before the job that needs it and is automatically destroyed at the end. The system supports generic OS images and was initially designed to enable access to specific and expensive hardware configurations, such as AWS F1 FPGA instances. Spot instance usage is also integrated to minimize costs.

The main benefits are a drastic reduction in infrastructure costs through elimination of permanent agents, and increased flexibility allowing use of specialized hardware configurations only when necessary. Complete process automation simplifies agent management and optimizes cloud resource utilization.

---

## Microsoft Cloud Infrastructure Migration and Administration
**April 2021 - June 2021**

Complete IT infrastructure overhaul following company separation, including service migration, SSO implementation, and CI/CD toolchain modernization.

As part of the separation from PLDA Group, this project involved creating an entirely autonomous IT environment. The core operation was the strategic migration of the Google Workspace ecosystem to Microsoft 365, with identity transition to Azure Active Directory (Azure AD) as the central directory.

To secure and streamline access, Single Sign-On (SSO) identity federation was configured for critical services such as Jira, Lucca, and Google. On the development operations side, the toolchain was rationalized by replacing Jenkins and AWS CodeBuild systems with Azure DevOps, establishing a unified CI/CD platform for continuous integration and deployment.

IT asset management was also modernized through implementation of Microsoft Intune for provisioning and security policy management on Windows & Linux (Fedora) workstations.

Benefits: The project established complete IT autonomy, increased security posture through centralized identity and access management, and improved CI/CD processes.

---

## Ansible Home: Ansible Collection for Self-Hosted Free Software Deployment
**October 2019 - October 2021**

Development of an Ansible collection for self-hosting free software with enhanced security.

Creation of a structured Ansible collection including specialized roles for automated installation and configuration of open source services.

Implementation of main roles including Nextcloud for cloud storage, Squid as cache proxy, Kodi for media center, and MPD for audio playback.

Development of modular dependency roles: Nginx, PostgreSQL, PHP-FPM, and Valkey for a decentralized architecture.

Integration of a "common" role centralizing system initialization tasks: firewall configuration, SELinux hardening, automatic update management, and SSH hardening.

Adoption of Fedora as the base operating system to benefit from latest software versions and advanced security features.

Implementation of a CI/CD workflow with GitHub Actions for validation and deployment.

Benefits include drastic reduction in deployment time, configuration standardization, and simplified maintenance.

---

## AWS Cloud Infrastructure and Security Modernization with Terraform
**January 2019 - January 2020**

Complete AWS platform overhaul via Infrastructure as Code to enhance security in preparation for an external audit.

The project involved modernizing the Accelize V1 platform infrastructure on AWS by abandoning manual management in favor of an Infrastructure as Code and GitOps approach. The entire environment was redefined using Terraform to ensure reproducibility, traceability, and auditability of deployed resources.

Particular emphasis was placed on security enhancement in preparation for an external audit. This involved strict review of AWS IAM policies, network segmentation via VPCs, and Security Hub integration for centralized threat monitoring.

Existing application services were structured around Elastic Beanstalk, EC2 instances, RDS databases, Application Load Balancer, S3, Lambda functions, and Route 53.

Benefits achieved include infrastructure entirely managed and versioned via Terraform, eliminating configuration drift. The project enabled successful completion of the security audit with excellent results.

---

## Accelpy: FPGA Application Deployment
**July 2019 - October 2019**

Automation tool for provisioning and deploying FPGA applications on cloud and on-premise infrastructures.

This command-line tool, integrated with the Accelize platform, orchestrates deployment of FPGA-accelerated hardware solutions. It interacts with platform APIs to manage the FPGA design lifecycle, from bitstream selection to final hardware target configuration.

Accelpy automates resource provisioning, whether on FPGA instances in the cloud or on-premise servers. The process includes secure bitstream download, FPGA chip programming, and host software environment setup. Deployment artifact management relies on cloud object storage solutions where instances are provisioned to reduce latency.

FPGA application deployment is thus drastically simplified and accelerated.

---

## Internal AWS Development Environment
**June 2019 - July 2019**

Implementation of a secure, automated, and cost-controlled AWS development environment.

This project involved deploying an internal development environment on AWS, with emphasis on security and optimization.

The architecture relies on an isolated network via a VPC. Security was enhanced through implementation of a two-tier model. In addition to IAM policies based on the principle of least privilege, a resource ownership system was developed to ensure clear attribution and resource access control to their users.

Automation is at the heart of cost management and maintenance. Lambda functions, orchestrated by EventBridge, were implemented to automatically detect and terminate orphaned resources, such as unattached EBS volumes or unused EC2 instances. Additionally, the DLM service was configured to automate EC2 instance backup creation and management. Finally, KMS encryption is enabled by default for EBS.

Benefits achieved include enhanced security posture, significant cost reduction through elimination of resource waste, and data sustainability guarantee.

---

## Apyfal: Cloud FPGA Application Deployment
**April 2018 - April 2019**

Orchestration of hardware application execution on remote FPGA instances via a Python API.

Development of Apyfal, a software solution facilitating computation acceleration on cloud-available FPGAs. The project enabled creation of an easy-to-use Python client capable of remotely controlling the complete application lifecycle, from deployment to execution on specialized hardware infrastructures.

The architecture relies on a RESTful API for communication between client and orchestration server. The latter dynamically manages FPGA resources, including bitstream programming and instance allocation.

This solution significantly reduced the complexity of accessing FPGA hardware accelerators for software developers. It thus offered a productivity gain by abstracting cloud platform heterogeneity and fully automating resource provisioning, making hardware acceleration as accessible as a simple software library.

---

## Airfs (Pycosio): Unified Python Library for Cloud Storage
**July 2018 - February 2021**

Unifies access to cloud storage and local file systems via a standard Python API.

Development of a Python library offering a unified programming interface to interact with various remote and cloud storage systems. The architecture is modeled after the standard Python library APIs for local file manipulation.

The project's technical core relies on implementing "io.RawIOBase" and "io.BufferedIOBase" abstract classes. This design ensures direct compatibility with native modules like "io", "os", "os.path", and "shutil". It makes cloud object manipulation transparent and interchangeable with local file system file manipulation.

The library integrates advanced features for buffered objects to optimize performance. These include asynchronous writing and prefetching, memory-usage-based locking mechanisms, and parallel connection usage to maximize bandwidth. The project supports multiple providers such as AWS S3, Azure Blob Storage, Azure Files, OpenStack Swift, and access via HTTP/HTTPS.

Initially created under the name "pycosio", the project was taken over as a "fork" to be extended and maintained.

Main benefits are a high-level abstraction that simplifies application code and makes it agnostic to data source. This improves code portability and maintainability while ensuring high-performance data transfers.

---

## Electronic Card Test Bench Software Evolution
**October 2017 - April 2018**

Development of critical features for an industrial test bench in Python environment under Debian.

This project focused on improving test software used in an industrial manufacturing context. Developments included software instrumentation for control and communication with various measurement equipment. One major evolution was the implementation of a client/server architecture to improve supervision and test data collection.

Performance optimization was a central focus, with use of the Numpy library to accelerate calculations on large datasets. New test scenarios were implemented to extend electronic card validation coverage.

A demonstrator was also developed to integrate the SPC (Statistical Process Control) analysis method. This tool aimed to provide statistical analysis tools to facilitate measurement interpretation and early detection of manufacturing process drift.

---

## Compilertools: High-Performance Python Binary Package Creation
**February 2017 - December 2017**

A Python library for creating and distributing high-performance binary packages leveraging modern CPU architectures.

This project provides a complete solution for compiling code, particularly C and C++ extensions, into Python binary packages.

The library detects and uses advanced processor instruction sets, such as SIMD (AVX, SSE), to generate binaries specifically optimized for the target machine. The system manages the complexity of different compilation toolchains and hardware architectures, offering a transparent build process. It integrates with standard Python packaging tools to facilitate distribution on repositories like PyPI.

This approach enables distribution of Python applications offering maximum performance upon installation, without requiring manual compilation by the end user. Execution speed gains are significant for compute-intensive or data processing applications, while simplifying the deployment process.

---

## Fazpy: Optical Measurement Analysis and Production Control Software
**October 2014 - September 2017**

Design of a complete software solution for optical metrology data processing and production equipment adjustment generation.

This project involved designing and implementing a complete desktop application under Windows using Python. The user interface, developed with the Qt framework, offers optical and mechanical engineers a tool dedicated to analyzing complex measurements, particularly from interferometry. The software core relies on optical calculation and advanced image processing modules.

Particular attention was paid to performance, requiring calculation algorithm optimization and search for specific solutions for large data volume processing.

The software architecture was designed to be modular and scalable, integrating more than 70 distinct functional modules, ranging from data acquisition to results visualization.

Benefits: The software enables automation and reliability of measurement analysis, while creating a direct link between quality control and manufacturing. This results in reduced development cycles and improved precision of manufactured parts.

---

[← Back to main page](../../index)

---

*Sole proprietorship registered in France - Siren 978307999 - Siret 97830799900018*

*© All rights reserved.*
