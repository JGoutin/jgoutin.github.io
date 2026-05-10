---
title: Projects
description: Selected projects from 10+ years of consulting in software, cloud and DevOps
keywords: portfolio, case studies, projects, AWS, cloud architecture, DevOps, Terraform, AI, LLM, Python, stdapi
---

# Projects

A selection of significant projects completed over 10+ years of experience.

## :material-rocket-launch: stdapi.ai — OpenAI- & Anthropic-compatible API for AWS AI services

!!! abstract "August 2025 – Present &middot; Freelance"

    **Stack:** AWS (Bedrock, Lambda, ECS, CloudWatch), Python, FastAPI,
    multi-modal AI · **Links:**
    [stdapi.ai](https://stdapi.ai) ·
    [:fontawesome-brands-github: GitHub](https://github.com/stdapi-ai/stdapi.ai)

Open-source API providing OpenAI and Anthropic SDK compatibility with AWS AI
services and Amazon Bedrock models.

End-to-end project covering architecture design, full-stack development, AWS
infrastructure deployment, technical documentation, and go-to-market strategy.
The solution provides a compatibility layer bridging the OpenAI and Anthropic
SDKs with 80+ Amazon Bedrock models and several AWS AI services.

The technical implementation integrates **Amazon Bedrock** for LLM
orchestration, **Amazon Polly** for speech synthesis, **Amazon Transcribe**
for speech-to-text, and **Amazon Translate**. Multi-modal capabilities span
text conversations, image generation, audio processing, and vector embeddings.

Infrastructure is deployed on AWS with a multi-region architecture, CloudWatch
observability, and hardened container images. A dual-licensing model (AGPL-3.0
and AWS Marketplace commercial license) balances open-source contribution and
enterprise viability.

## :material-brain: Enterprise AI / LLM platform

!!! abstract "July 2025 – August 2025 &middot; Freelance"

    **Stack:** AWS Bedrock, Python, RAG, LLM, AI

A centralised solution to leverage LLM models while ensuring strict data
governance.

The platform was deployed on AWS infrastructure, with a chatbot designed as
the single, controlled access point to AI capabilities. This governance
ensures the protection of sensitive company data.

The platform integrates advanced features such as **RAG**, allowing models to
provide enriched responses based on internal documents. Development teams can
also integrate AI directly into their IDEs to generate and improve code.

The architecture relies on **AWS Bedrock** for access to a diverse portfolio
of language models.

## :simple-gitlab: GitLab Runners migration to AWS serverless architecture

!!! abstract "March 2025 – June 2025 &middot; Freelance"

    **Stack:** GitLab CI/CD, AWS (ECS Fargate, CodeBuild, IAM), Docker, ARM64

Implementation of a dynamic and secure CI/CD infrastructure by integrating
GitLab Runners with AWS ECS/Fargate and CodeBuild.

For generic tasks (Terraform, `curl`, linters), GitLab Runners based on **ECS
Fargate ARM** were deployed. For language-specific compilation and build
tasks, GitLab Runners leveraging **AWS CodeBuild** were implemented, taking
advantage of native development-environment support.

Security was enhanced by abandoning static AWS IAM access keys in favour of
**temporary, least-privilege IAM roles**. Secret management — particularly
for Docker registries and Maven and NPM repositories — was centralised and
secured.

The benefits include notable performance improvements, reduced wait times and
job congestion through on-demand scalability, and significant operational
cost optimisation. Pipeline configuration in `gitlab-ci.yml` files was
simplified, and ARM64 Docker image building became possible.

## :simple-terraform: AWS infrastructure standardisation with Terraform

!!! abstract "October 2023 – October 2024 &middot; Freelance"

    **Stack:** Terraform, AWS (ECS, Aurora, Lambda, SQS, SES, IAM),
    Infrastructure as Code

Reference architectures developed as reusable Terraform modules to simplify,
accelerate, and secure production deployments.

The main objective was to transition from an infrastructure historically
centred on EC2 instances to a modern architecture fully leveraging AWS
managed services (ECS, Aurora, Lambda, SQS, SES, …).

Modules expose a streamlined interface designed to be accessible to
non-experts while encapsulating advanced and complex configuration. Each
module natively integrates security best practices: fine-grained IAM
permissions (least-privilege policies), network segmentation via security
groups, systematic data encryption, and CloudWatch monitoring.

Benefits: notable reduction in application deployment time, increased
reliability through standardisation, improved overall security posture, and
simplified infrastructure maintenance — together with the adoption of DevOps
processes by the development teams.

## :fontawesome-brands-aws: Multi-account AWS network architecture with shared VPC and cost optimisation

!!! abstract "October 2023 – April 2024 &middot; Freelance"

    **Stack:** AWS VPC, Terraform, Network Firewall, Route 53, VPN

Complete overhaul of distributed network infrastructure to centralise
management and significantly reduce operational costs.

This project restructured a multi-account AWS architecture by replacing an
expensive Transit Gateway with a solution based on AWS Resource Access
Manager (RAM). The centralised approach uses a single VPC hosted in a
dedicated account, with specialised subnet sharing to project accounts via
AWS RAM.

The architecture segments environments into isolation zones (public, private,
…) while pooling critical resources: VPC endpoints, NAT Gateway, and other
network components. This consolidation eliminates resource duplication and
optimises internal IPv4 range allocation.

Security relies on a least-privilege strategy with NACLs and Security Groups.
**AWS Network Firewall** and **Route 53 Resolver Firewall** provide global
perimeter protection. The infrastructure supports dual-stack IPv4/IPv6.

Inter-project and on-premises communications are standardised through
configurable centralised routing. Observability is centralised in CloudWatch.
The infrastructure is entirely managed as IaC with Terraform, with direct
integration into existing enterprise modules.

Benefits include substantial infrastructure cost reduction, operational
simplification, enhanced security, and significant reduction of network
technical debt.

## :material-chip: FPGA marketplace with cloud-native architecture

!!! abstract "November 2021 – April 2023 &middot; Accelize"

    **Stack:** AWS (EC2, Lambda, S3, CloudFront, Cognito, DynamoDB, RDS),
    Python, FastAPI, SQLAlchemy, PostgreSQL, Terraform

Cloud architecture and software for a specialised platform distributing FPGA
applications, with advanced licence management, multiple billing models
(subscription, pay-per-use), and hosting of resources such as Linux packages
and documentation.

Cloud infrastructure fully automated with Terraform: backend on AWS with EC2,
Aurora Serverless, Application Load Balancer, autoscaling, and Global
Accelerator. Frontend distributed via Amazon S3 and CloudFront. Python
microservices on AWS Lambda interfacing with DynamoDB, SQS, SNS, and SES for
notifications. Centralised authentication via Amazon Cognito and real-time
monitoring with CloudWatch. EC2 image construction with Ansible and Packer.

SQL (PostgreSQL via SQLAlchemy Core) and NoSQL (DynamoDB) data models. Main
backend built with Python / FastAPI.

Automated tests covering all business flows. Complete CI/CD pipeline
automation with Azure Pipelines and promotion of DevOps best practices.
Migration from a previous version with backward compatibility.

Benefits include high availability, enhanced security, optimised cost
management, and significantly accelerated deployment and maintenance.

## :simple-linux: Highly available Linux repository manager with CI/CD integration and API

!!! abstract "October 2021 – March 2022 &middot; Accelize"

    **Stack:** AWS (S3, Lambda, CloudFront), Python, CI/CD, GPG

Highly available DEB and RPM package distribution solution, integrating
addition flows from CI/CD and via a dedicated web API.

The architecture is entirely based on AWS serverless components: artifact
storage on S3, distribution via CloudFront, processing triggered by S3 Event
Notifications, and business script execution in AWS Lambda.

A Python library optimised for Lambda was developed, responsible for dynamic
package metadata modification and automated cryptographic signature
management.

Internal Accelize packages are added via continuous integration, while client
and partner packages are managed securely through a REST API.

Main benefits: high availability, complete automation of the package addition
and validation flow, integrity and security ensured by systematic signing,
and ease of integration via API and CI/CD.

## :material-docker: Containerised FPGA application execution service in hybrid cloud

!!! abstract "June 2021 – October 2021 &middot; Accelize"

    **Stack:** AWS (Lambda, CloudFront, S3, EC2), OpenStack, Docker, Python

Cloud service for on-demand execution of containerised applications on FPGA
instances directly from product web pages.

The architecture relies on a 100% serverless backend and orchestrator
leveraging AWS Lambda, S3, SQS, CloudFront, and ECR. This infrastructure
drives application deployment on heterogeneous execution instances, supporting
a multi-cloud environment including Amazon EC2 and OpenStack Nova.

Several major technical constraints were addressed: cost control with
automatic provisioning and termination of FPGA instances; multi-cloud
compatibility through a software abstraction layer; specific Linux host
configurations enabling container-to-FPGA hardware interaction; and execution
security and confidentiality, including for public sessions launched without
authentication.

Benefits: high scalability and cost optimisation through full lifecycle
automation. The service offers a secure and flexible infrastructure capable
of supporting public product demonstrations directly from web pages.

## :fontawesome-brands-microsoft: ACID — dynamic cloud agents for Azure Pipelines

!!! abstract "June 2021 &middot; Accelize"

    **Stack:** Azure Pipelines, AWS EC2, Azure VM, Terraform, Ansible

Execution of Azure Pipelines jobs on ephemeral agents provisioned on demand
on AWS EC2 and Azure VM.

A utility was developed to enable Azure Pipelines jobs to run on self-hosted
agents created on temporary cloud instances. The tool leverages **Terraform**
to automate resource provisioning and deletion on AWS EC2 and Azure Virtual
Machines. Agent software configuration is handled by **Ansible** playbooks,
offering complete environment customisation.

The agent lifecycle is entirely managed within the pipeline: an instance is
started just before the job that needs it and is automatically destroyed
afterwards. The system supports generic OS images and was initially designed
to enable access to specific and expensive hardware configurations such as
AWS F1 FPGA instances. Spot-instance usage is also integrated to minimise
costs.

Main benefits: drastic reduction in infrastructure costs through elimination
of permanent agents, and increased flexibility allowing specialised hardware
configurations to be used only when necessary.

## :fontawesome-brands-microsoft: Microsoft cloud infrastructure migration and administration

!!! abstract "April 2021 – June 2021 &middot; Accelize"

    **Stack:** Microsoft Azure, AAD, MS365, AWS, GitHub, PowerShell

Complete IT infrastructure overhaul following company separation, including
service migration, SSO implementation, and CI/CD toolchain modernisation.

As part of the separation from PLDA Group, this project created an entirely
autonomous IT environment. The core operation was the strategic migration of
the Google Workspace ecosystem to Microsoft 365, with identity transition to
Azure Active Directory as the central directory.

To secure and streamline access, **SSO identity federation** was configured
for critical services such as Jira, Lucca, and Google. On the development
operations side, the toolchain was rationalised by replacing Jenkins and AWS
CodeBuild systems with **Azure DevOps**, establishing a unified CI/CD platform.

IT asset management was modernised through **Microsoft Intune** for
provisioning and security policy management on Windows and Linux (Fedora)
workstations.

Benefits: complete IT autonomy, increased security posture through
centralised identity and access management, and improved CI/CD processes.

## :simple-ansible: Ansible Home — Ansible collection for self-hosted free software deployment

!!! abstract "October 2019 – October 2021 &middot; Open source"

    **Stack:** Ansible, Fedora Linux, GitHub Actions, PostgreSQL, Nginx

Ansible collection for self-hosting free software with enhanced security.

The collection includes specialised roles for the automated installation and
configuration of open-source services such as **Nextcloud** for cloud
storage, **Squid** as cache proxy, **Kodi** for media centre, and **MPD** for
audio playback.

Modular dependency roles cover **Nginx**, **PostgreSQL**, **PHP-FPM**, and
**Valkey** for a decentralised architecture. A *common* role centralises
system initialisation: firewall configuration, SELinux hardening, automatic
update management, and SSH hardening.

Fedora was adopted as the base operating system for its latest software
versions and advanced security features. A CI/CD workflow with GitHub Actions
ensures validation and deployment.

Benefits: drastic reduction in deployment time, configuration standardisation,
and simplified maintenance.

## :simple-terraform: AWS cloud infrastructure and security modernisation with Terraform

!!! abstract "January 2019 – January 2020 &middot; Accelize"

    **Stack:** AWS (VPC, EC2, RDS, S3, Lambda, Security Hub), Terraform

Complete AWS platform overhaul through Infrastructure as Code, in preparation
for an external security audit.

The project modernised the Accelize V1 platform infrastructure on AWS by
abandoning manual management in favour of an Infrastructure as Code and
GitOps approach. The entire environment was redefined using **Terraform** to
ensure reproducibility, traceability, and auditability.

Particular emphasis was placed on security: strict review of AWS IAM
policies, network segmentation via VPCs, and **Security Hub** integration for
centralised threat monitoring. Application services were structured around
Elastic Beanstalk, EC2, RDS, Application Load Balancer, S3, Lambda, and
Route 53.

Benefits: infrastructure entirely managed and versioned via Terraform,
eliminating configuration drift. The project enabled a successful external
security audit with excellent results.

## :material-chip: Accelpy — FPGA application deployment

!!! abstract "July 2019 – October 2019 &middot; Accelize"

    **Stack:** Python, AWS, OpenStack, FPGA, CLI

Automation tool for provisioning and deploying FPGA applications on cloud
and on-premises infrastructures.

This command-line tool, integrated with the Accelize platform, orchestrates
deployment of FPGA-accelerated hardware solutions. It interacts with platform
APIs to manage the FPGA design lifecycle, from bitstream selection to final
hardware target configuration.

Accelpy automates resource provisioning, whether on cloud FPGA instances or
on-premises servers. The process includes secure bitstream download, FPGA
chip programming, and host software environment setup. Deployment artefact
management relies on cloud object storage in the same region as instances to
reduce latency.

## :fontawesome-brands-aws: Internal AWS development environment

!!! abstract "June 2019 – July 2019 &middot; Accelize"

    **Stack:** AWS (IAM, EC2, CloudWatch, Lambda, EventBridge, DLM),
    Terraform, Python

Implementation of a secure, automated, and cost-controlled AWS development
environment.

The architecture relies on an isolated VPC. Security was enhanced through a
two-tier model: in addition to least-privilege IAM policies, a **resource
ownership** system was developed to ensure clear attribution and access
control.

Automation is at the heart of cost management and maintenance. **Lambda**
functions, orchestrated by **EventBridge**, automatically detect and
terminate orphaned resources such as unattached EBS volumes or unused EC2
instances. The **DLM** service was configured to automate EC2 instance
backups, and KMS encryption is enabled by default for EBS.

Benefits: enhanced security posture, significant cost reduction through
elimination of resource waste, and data sustainability.

## :material-chip: Apyfal — cloud FPGA application deployment

!!! abstract "April 2018 – April 2019 &middot; Accelize"

    **Stack:** Python, AWS, OpenStack, FPGA, REST API

Orchestration of hardware application execution on remote FPGA instances via
a Python API.

Apyfal facilitates computation acceleration on cloud-available FPGAs through
an easy-to-use Python client capable of remotely controlling the complete
application lifecycle, from deployment to execution.

The architecture relies on a RESTful API for communication between client
and orchestration server. The latter dynamically manages FPGA resources,
including bitstream programming and instance allocation.

The solution significantly reduces the complexity of accessing FPGA hardware
accelerators by abstracting cloud platform heterogeneity and automating
resource provisioning, making hardware acceleration as accessible as a
software library.

## :simple-python: Airfs (Pycosio) — unified Python library for cloud storage

!!! abstract "July 2018 – February 2021 &middot; Open source"

    **Stack:** Python, AWS S3, Azure Storage, OpenStack Swift

Unified access to cloud storage and local file systems through a standard
Python API, modelled after the Python standard library APIs for local file
manipulation.

The technical core relies on implementing the `io.RawIOBase` and
`io.BufferedIOBase` abstract classes, ensuring direct compatibility with
modules such as `io`, `os`, `os.path`, and `shutil`. This makes cloud object
manipulation transparent and interchangeable with local file system access.

Advanced features for buffered objects include asynchronous writing and
prefetching, memory-usage-based locking mechanisms, and parallel connections
for maximum bandwidth. Supported providers: **AWS S3**, **Azure Blob
Storage**, **Azure Files**, **OpenStack Swift**, and HTTP/HTTPS.

Initially created under the name *Pycosio*, the project was forked to be
extended and maintained.

Benefits: high-level abstraction simplifying application code and making it
agnostic to data sources, improving portability and maintainability while
ensuring high-performance data transfers.

## :material-waveform: Electronic card test-bench software evolution

!!! abstract "October 2017 – April 2018 &middot; SuperSonic Imagine"

    **Stack:** Python, Debian, NumPy, serial / TCP communication

Development of critical features for an industrial test bench in a Python
environment under Debian.

This project focused on improving test software used in an industrial
manufacturing context. Developments included software instrumentation for
control and communication with various measurement equipment. A major
evolution was the implementation of a **client/server** architecture to
improve supervision and test data collection.

Performance optimisation was a central focus, with use of NumPy to accelerate
calculations on large datasets. New test scenarios extended electronic card
validation coverage. A demonstrator was also developed to integrate the
**SPC** (Statistical Process Control) analysis method, providing tools to
facilitate measurement interpretation and early detection of manufacturing
process drift.

## :simple-python: Compilertools — high-performance Python binary package creation

!!! abstract "February 2017 – December 2017 &middot; Open source"

    **Stack:** Python, C / C++, SIMD, PyPI

A Python library for creating and distributing high-performance binary
packages leveraging modern CPU architectures.

The library detects and uses advanced processor instruction sets such as
**SIMD (AVX, SSE)** to generate binaries specifically optimised for the
target machine. The system manages the complexity of different compilation
toolchains and hardware architectures, offering a transparent build process.
It integrates with standard Python packaging tools to facilitate distribution
on repositories like PyPI.

This approach enables distribution of Python applications offering maximum
performance upon installation, without requiring manual compilation by the
end user.

## :material-chart-scatter-plot: Fazpy — optical measurement analysis and production control software

!!! abstract "October 2014 – September 2017 &middot; Thales SESO"

    **Stack:** Python, Qt, NumPy, SciPy, Cython, Windows

Complete software solution for optical metrology data processing and
production equipment adjustment generation.

This desktop application for Windows is built in Python with a Qt-based user
interface, dedicated to optical and mechanical engineers analysing complex
measurements (notably interferometry). The software core relies on advanced
optical calculation and image processing modules.

Particular attention was paid to performance, requiring algorithm
optimisation and specific solutions for large data volumes. The architecture
was designed to be modular and scalable, integrating more than **70 distinct
functional modules**, ranging from data acquisition to results visualisation.

Benefits: automation and reliability of measurement analysis, with a direct
link between quality control and manufacturing — yielding reduced development
cycles and improved precision of manufactured parts.
