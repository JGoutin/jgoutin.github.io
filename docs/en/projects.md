---
title: Projects
description: Selected projects from 10+ years of consulting in software, cloud and DevOps
keywords: portfolio, case studies, projects, AI agents, agentic delivery, Claude Code, TDD, code review, mutation testing, LLM cost, AI security, local inference, cloud architecture, AWS, DevOps, Terraform, LLM, Python
---

# Projects

A selection of significant projects completed over 10+ years of experience.
The most recent ones were delivered with AI agents, using the
[agentic delivery](#agentic-delivery-skills-and-long-running-milestone-workflows) method.

## :material-email-fast: AI email assistant with RAG and guarded actions

!!! abstract "June 2026 – September 2026 &middot; JGoutin-dev &middot; In production"

    **Stack:** Amazon Bedrock (Nova, Knowledge Bases, S3 Vectors), AWS Lambda,
    SES, DynamoDB, EventBridge, Python, OpenTofu

An assistant that answers customer emails and acts on their requests: here, private
commercial offers for a software product.

It works out what each customer asks and in which language, creates the offer
through the marketplace API, follows it up to acceptance or expiry, and
answers technical questions from the product documentation (**RAG** on a
Bedrock Knowledge Base, with source links).

**The model classifies, translates and drafts; plain code decides every
action**, with prices and terms taken only from configuration. Unclear emails
go to a human, and a human is copied on every reply. Prompt-injection cases and tests
against the real model run on every change. Built for GDPR: EU region,
limited retention, no email bodies in logs.

## :material-robot-industrial: Agentic delivery — skills and long-running milestone workflows

!!! abstract "April 2026 – Present &middot; JGoutin-dev"

    **Stack:** Claude Code (skills, subagents, workflows), Git, GitHub,
    Python, Rust, CI quality gates

A delivery system in which AI agents build complete releases end to end,
used on an open-source product and on a private Rust application.

One command runs a whole milestone: a plan reviewed before any code, tests
written first, implementation, review, and a release candidate tested on real
AWS. A human approves the result, the release and any risky action. The
**gates cannot be skipped** (100% coverage on critical code, mutation
testing, supply-chain checks): CI and permissions enforce them, not prompts.
Independent agents hunt bugs and security issues, another tries to disprove
each finding, and a fix counts only if its new test fails without it.

Work resumes cleanly after hours or weeks, the strongest model and every
gate go only where data or security is at risk, token spend is measured,
and 14 skills hold one product's knowledge.

Measured on the private Rust application: about 200,000 lines of code and
370,000 lines of tests in 27 days, 1,200+ agents, and 3,151 review findings
of which 40% were confirmed and fixed.

[Bring this method to your team](contact.md){ .md-button .md-button--primary }

## :material-chip: Local AI inference optimisation and the inference box

!!! abstract "July 2026 – Present &middot; Open project"

    **Stack:** llama.cpp, Lemonade, stable-diffusion.cpp, ROCm, Vulkan,
    AMD GPUs and Ryzen AI Max, Fedora CoreOS, Python

Running large models fast on local hardware, and turning that know-how into
a self-hosted inference appliance.

A tuning method for llama.cpp servers and image models: sizing a model
against the memory budget, placing mixture-of-experts layers between GPU and
CPU, KV cache placement and speculative decoding, each benchmarked with
repeated runs. Measured on a workstation GPU: **+76% prompt processing and
+21% generation** over automatic placement, **+27% to +58%** from
speculative decoding, and **1.8× faster** image generation.

The **inference box** applies this to AMD Ryzen AI Max machines: a turnkey,
private AI server on a hardened immutable OS, with its own management UI. It
is in design, with a first machine used for benchmarks.

## :material-image-auto-adjust: Image generation pipeline with controlled originality and automatic quality check

!!! abstract "August 2026 &middot; JGoutin-dev R&D &middot; Prototype"

    **Stack:** Python, local LLM and vision models, Lemonade,
    stable-diffusion.cpp, Claude Code skill

A local pipeline that produces original images one after the other, designed
to avoid repeats and defects.

Language models are poor at randomness, so **code provides it**: it draws
keywords and composition rules, and a language model guided by a skill turns
them into a coherent prompt. After local generation, a **control model
inspects each image** for visual defects. A defective image is regenerated,
and the prompt is corrected when a defect comes back.

## :material-shield-lock: Securing AI agents — isolation and access broker

!!! abstract "September 2026 – Present &middot; JGoutin-dev R&D"

    **Stack:** Rust, Linux (ACLs, nftables, Landlock, seccomp, cgroups,
    FUSE), KeePassXC, Kani, microVMs (smolvm), Wolfi, bubblewrap

Letting AI agents work autonomously without giving them the keys to the
machine: the security boundary is the operating system, not the agent's own
permission prompts. Agents run as a separate, unprivileged user that cannot
reach the owner's home, credentials or git push, and changes to its own
setup need the owner's approval.

An **access broker** in Rust lends access for a limited time with one
command: KeePassXC secrets (optionally single use or approved on the desktop,
with token rotation), SSH logins signed only for the granted hosts, NAS
folders mounted through a jailed helper (Landlock, seccomp, cgroups),
read-only by default or writable within a budget, and local services opened
in the firewall. Values go straight from KeePassXC to the command that uses
them, never through the model, and every use is audited. The broker is a
reproducible static binary that depends only on the `libc` crate, with Kani
proofs among its release checks.

An earlier prototype ran each agent in a minimal Wolfi-based microVM, and
supply-chain controls cover what agents install.

## :material-server-network: Self-hosted Kubernetes platform operated with an AI agent

!!! abstract "September 2026 – Present &middot; Personal infrastructure"

    **Stack:** Talos Linux, Kubernetes, Flux, Forgejo, Cilium,
    cert-manager, CloudNativePG, Grafana, Renovate, SOPS, gVisor, TrueNAS

A self-hosted platform designed, built and run with an AI agent: Kubernetes
on Talos Linux, GitOps with Flux from a self-hosted forge, automated updates
that stop at the first failure, encrypted backups with tested restores,
monitoring and sandboxed workloads.

The agent prepares every change (scripts, dry runs) and has **read-only
production access, with no standing write credentials**. Read-only steps run
freely, reversible ones are reported, and risky ones need a plan, a rollback
and the owner's approval; write credentials are lent for one run only. More
than 120 architecture decisions are logged.

## :material-school: Claude Code skills for client teams

!!! abstract "July 2026 – Present &middot; Freelance"

    **Stack:** Claude Code (skills, agents, hooks), Git, CI/CD

Design and upkeep of AI agent skills for client development teams, so that
agents work the way the team does: knowledge-base skills on the company's
architecture and conventions, development workflow skills (test-driven
development, quality gates, code review, releases) and git skills. The
skills are updated as tools, models and team practices change.

## :material-rocket-launch: stdapi.ai — open-source AI gateway compatible with OpenAI, Anthropic, Cohere & Ollama

!!! abstract "August 2025 – November 2026 &middot; Open source"

    **Stack:** AWS (Bedrock, Lambda, ECS, CloudWatch), Python, FastAPI,
    multi-modal AI, MCP · **Link:**
    [:fontawesome-brands-github: GitHub](https://github.com/stdapi-ai/stdapi.ai)

Open-source API that made the OpenAI, Anthropic, Cohere and Ollama SDKs work
with 100+ Amazon Bedrock models and AWS AI services. AWS approved it as **AWS
Qualified Software**, after verifying it against its technical and security
requirements. The project is discontinued, and its source code stays
available.

End-to-end project: architecture, development, AWS deployment, documentation
and go-to-market. It covered chat, image and video generation, speech
(**Amazon Polly**, **Amazon Transcribe**), translation, embeddings, batches,
vector stores, realtime voice and an **MCP server** listed in the official
MCP registry. Multi-tenant controls covered scoped API keys, rate and token
limits, and per-user cost tracking.

Deployed on AWS in several regions with hardened container images, and
released under AGPL-3.0. **6,000+ automated tests run against real AWS**,
20 third-party tools (Claude Code, Open WebUI, n8n, LangChain, …) are tested
end to end, and 43 releases shipped in under a year.

## :material-brain: Enterprise AI / LLM platform

!!! abstract "July 2025 – August 2025 &middot; Freelance"

    **Stack:** Amazon Bedrock, Python, RAG, LLM, AI

A centralised solution to leverage LLM models while ensuring strict data
governance.

The platform was deployed on AWS infrastructure, with a chatbot designed as
the single, controlled access point to AI capabilities. This governance
ensures the protection of sensitive company data.

The platform integrates advanced features such as **RAG**, allowing models to
provide enriched responses based on internal documents. Development teams can
also integrate AI directly into their IDEs to generate and improve code.

The architecture relies on **Amazon Bedrock** for access to a diverse portfolio
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

!!! abstract "October 2019 – Present &middot; Open source"

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
ensures validation and deployment. A 2026 update added audit logging and
stronger kernel, database and web-server settings.

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
