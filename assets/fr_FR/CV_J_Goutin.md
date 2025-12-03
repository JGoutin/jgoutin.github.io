# Jérémy Goutin
**Architecte de solutions. Expert freelance en logiciel, cloud, & DevOps**

contact@jgoutin.dev  
https://jgoutin.dev  
https://www.linkedin.com/in/jgoutin  
https://github.com/jgoutin

---

## Compétences Clés

### Architecture Cloud

**Expert AWS** avec une expérience approfondie :

- Architecture de solutions cloud **serverless** et classiques
- Services maîtrisés : VPC, EC2, ELB, RDS/Aurora, Lambda, DynamoDB, CloudFront, CloudWatch, SQS, SNS, SES, Cognito, Route53, S3, ECS, IAM
- **Infrastructure as Code** avec **Terraform**
- Sécurité cloud : politiques IAM à moindres privilèges, pare-feu VPC, SecurityHub
- **FinOps** : optimisation des coûts et architecture multi-compte
- Audit de sécurité externe réussi

**Autres Cloud Providers** :

- **Microsoft Azure** : AAD, MS365, Azure DevOps
- **OpenStack**
- **Alibaba Cloud**

### Développement Logiciel

**Expert Python** avec une forte expérience en :

- Architecture logicielle et conception de modèles de données
- Développement de backends web et d'API REST avec **FastAPI**
- Gestion de bases de données avec **SQLAlchemy** (PostgreSQL) et **DynamoDB**
- Python scientifique : **Numpy**, **Scipy**, **Pandas**, **Matplotlib**, **Cython**
- Code de qualité, tests automatisés et maintenabilité

### DevOps & CI/CD

- Architecture et mise en place de pipelines CI/CD complets
- Automatisation totale du *push* au déploiement en production
- **DevSecOps** : intégration de la sécurité dans les pipelines
- **GitOps** : gestion de l'infrastructure et des déploiements via Git
- **GitHub Actions**, **GitLab CI/CD**, **Azure Pipeline**, **AWS CodeBuild**
- Déploiement de services web et de paquets logiciels
- **Ansible** pour la configuration de serveurs
- **Docker** pour la conteneurisation

### Intelligence Artificielle & LLM

- **LLMOps** : déploiement et gestion de modèles de langage en production
- Architecture de plateformes IA d'entreprise avec gouvernance des données
- Intégration de **RAG** (Retrieval-Augmented Generation) pour enrichir les réponses des LLM
- Utilisation d'**AWS Bedrock** pour l'accès à des modèles de langage variés
- Mise en place de chatbots IA et d'assistants de développement

### Administration Système

**Linux** : Expertise sur Fedora, CentOS, Debian, Ubuntu, Alpine Linux
- Configuration et automatisation avec **Ansible**
- Sécurité et renforcement (*hardening*) de Linux
- Gestion de pare-feu avec **PfSense**
- Stockage avec **TrueNAS**

### Compétences Fonctionnelles

- Architecture de solutions complètes
- Résolution de problèmes complexes
- Haute autonomie et esprit critique
- Force de proposition et rigueur
- Respect des bonnes pratiques
- Apprentissage rapide de nouvelles technologies

---

## Projets Significatifs

### Plateforme IA/LLM d'Entreprise (Juillet-Août 2025)

**Contexte** : Projet Freelance  
**Réalisations** :

- Création d'une solution centralisée pour exploiter des modèles LLM avec gouvernance des données
- Déploiement d'une plateforme LLM sur l'infrastructure AWS
- Développement d'un chatbot comme point d'accès unique et contrôlé aux capacités d'IA
- Intégration de **RAG** (Retrieval-Augmented Generation) pour enrichir les réponses avec des documents internes
- Intégration IDE pour permettre aux équipes de développement de générer et améliorer le code
- Utilisation d'**AWS Bedrock** pour l'accès à un portefeuille varié de modèles de langage
- Gouvernance stricte pour protéger les données de l'entreprise

**Technologies** : AWS Bedrock, Python, RAG, LLM, IA

### Migration de Runners GitLab vers Architecture Serverless AWS (Mars-Juin 2025)

**Contexte** : Projet Freelance  
**Réalisations** :

- Migration complète de l'infrastructure de CI/CD vers une architecture serverless AWS
- Déploiement de runners GitLab basés sur **ECS Fargate ARM** pour les tâches génériques (Terraform, curl, linters)
- Implémentation de runners GitLab exploitant **AWS CodeBuild** pour les tâches de compilation
- Abandon des access keys IAM statiques au profit de **rôles IAM temporaires** à moindres privilèges
- Centralisation et sécurisation de la gestion des secrets (registres Docker, dépôts Maven et NPM)
- Support natif de l'architecture **ARM64** pour la construction d'images Docker
- Amélioration notable des performances et réduction des temps d'attente
- Scalabilité à la demande éliminant les congestions de jobs
- Optimisation significative des coûts opérationnels

**Technologies** : GitLab CI/CD, AWS (ECS Fargate, CodeBuild, IAM), Docker, ARM64

### Standardisation d'Infrastructure AWS avec Terraform (Octobre 2023-Octobre 2024)

**Contexte** : Projet Freelance  
**Réalisations** :

- Développement d'architectures de référence via des modules Terraform réutilisables
- Migration d'architectures historiques EC2 vers des services managés AWS (ECS, Aurora, Lambda, SQS, SES)
- Création de modules avec interface épurée encapsulant une configuration avancée et complexe
- Intégration native des bonnes pratiques de sécurité (IAM moindres privilèges, security groups, chiffrement, monitoring)
- Réduction notable du temps de mise en place de nouvelles applications
- Amélioration de la fiabilité par la standardisation
- Simplification de la maintenance des infrastructures
- Adoption des processus DevOps par les équipes de développement

**Technologies** : Terraform, AWS (ECS, Aurora, Lambda, SQS, SES, IAM), Infrastructure as Code

### Architecture VPC Multi-Compte AWS (Octobre 2023-Avril 2024)

**Contexte** : Projet Freelance  
**Réalisations** :

- Conception et implémentation d'un VPC commun multi-compte **Dualstack (IPv4/IPv6)**
- Intégration de **AWS Network Firewall**, **Route53 Resolver Firewall**, **AWS Site-to-Site VPN**
- Optimisation **FinOps** avec gestion simplifiée et centralisée
- Configuration de **VPC Endpoints** pour sécuriser les communications
- Architecture permettant une scalabilité et une sécurité optimales

**Technologies** : AWS VPC, Terraform, Network Firewall, Route53, VPN

### Plateforme Web V2 Complète (2018-2023)

**Contexte** : Accelize - Architecture & Développement  
**Réalisations** :

**Architecture Cloud** :

- Service web haute disponibilité avec backend EC2 multi-AZ
- Frontend **Angular** avec **S3** et **CloudFront**
- Microservices **serverless** basés sur **Lambda**
- Authentification utilisateurs avec **Cognito**
- Déploiement totalement automatisé via CI/CD

**Architecture Logicielle** :

- Conception complète des modèles de données SQL (**PostgreSQL**) et NoSQL (**DynamoDB**)
- Développement du backend principal en Python avec **FastAPI** et **SQLAlchemy Core**
- Conception et développement de microservices Python
- Définition de toutes les API internes et externes (REST)
- Stratégies de tests et monitoring
- Configuration Linux optimisée pour les serveurs EC2

**Technologies** : AWS (EC2, Lambda, S3, CloudFront, Cognito, DynamoDB, RDS), Python, FastAPI, SQLAlchemy, PostgreSQL, Terraform

### Service d'Exécution d'Applications FPGA dans le Cloud (2018-2023)

**Contexte** : Accelize - Architecture Cloud  
**Réalisations** :

- Architecture **serverless** pour l'exécution de démos FPGA publiques
- Provisionnement et résiliation automatique des instances FPGA sur **AWS** et **OpenStack**
- Sécurisation de l'exécution Docker (isolation, sandboxing)
- Utilisation de **Lambda**, **CloudFront**, **S3** pour l'infrastructure
- Gestion automatique du cycle de vie des ressources en fonction de la demande

**Technologies** : AWS (Lambda, CloudFront, S3, EC2), OpenStack, Docker, Python

### Dépôts de Paquets Linux Serverless (2018-2023)

**Contexte** : Accelize - Architecture Cloud  
**Réalisations** :

- Architecture serverless pour héberger des dépôts **Debian** et **Red Hat**
- Distribution via **S3** et **CloudFront** avec haute disponibilité
- Ajout de paquets automatisé via CI/CD (paquets internes)
- Service web pour les partenaires (upload de paquets externes)
- Mise à jour automatique des métadonnées et signatures GPG
- Utilisation de **Lambda** pour le traitement asynchrone

**Technologies** : AWS (S3, Lambda, CloudFront), Python, CI/CD, GPG

### Environnement de Développement AWS Sécurisé (2018-2023)

**Contexte** : Accelize - Architecture Cloud  
**Réalisations** :

- Conception d'un environnement de développement interne multi-utilisateurs
- Système d'**ownership des ressources** pour la traçabilité
- Politiques IAM à **moindres privilèges** pour chaque développeur
- Gestion automatique des coûts avec résiliation des ressources orphelines
- Sauvegardes automatiques des instances de développement
- Monitoring et alerting sur les dépenses

**Technologies** : AWS (IAM, EC2, CloudWatch, Lambda), Terraform, Python

### Infrastructure Informatique d'Entreprise (2018-2023)

**Contexte** : Accelize - Administration Système  
**Réalisations** :

- Architecture complète basée sur **Microsoft Azure**, **AAD**, **MS365**
- **Single Sign-On (SSO)** entre tous les services (AWS, GitHub, MS365)
- Migration de **Google Workspace** vers **MS365**
- Gestion automatisée des laptops Windows (provisionnement, configuration, sécurité)
- Administration **Azure DevOps** et gestion des repositories

**Technologies** : Microsoft Azure, AAD, MS365, AWS, GitHub, PowerShell

### Pipelines CI/CD DevSecOps (2018-2023)

**Contexte** : Accelize - DevOps  
**Réalisations** :

- Conception et implémentation de nombreux pipelines CI/CD
- Automatisation complète : tests, validation, sécurité, déploiement
- Intégration de scans de sécurité automatiques (**DevSecOps**)
- Création et mise à jour automatisée d'images Linux avec **Ansible**
- Construction et publication d'images **Docker** optimisées
- Déploiement automatique de services web et de paquets

**Technologies** : Azure Pipelines, GitHub Actions, Docker, Ansible, Python

### Logiciel d'Analyse Optique (2013-2017)

**Contexte** : Thales SESO - Développement Logiciel  
**Réalisations** :

- Développement complet d'un logiciel d'analyse optique sous Windows
- Plus de **70 modules** de fonctionnalités dans une architecture évolutive
- Calculs optiques avancés et traitement d'image
- Optimisation des performances avec Numpy et Cython
- Interface utilisateur complète avec **Qt**
- Recherche et implémentation d'algorithmes spécialisés
- Automatisation de bancs de tests optiques

**Technologies** : Python, Qt, Numpy, Scipy, Cython, Windows

### Logiciel de Test pour Banc d'Essai (2017-2018)

**Contexte** : SuperSonic Imagine - Développement Logiciel  
**Réalisations** :

- Développement d'un logiciel de test électronique sous **Debian**
- Architecture **client/serveur** pour contrôle distant
- Instrumentation et communication avec divers équipements
- Optimisation de calculs avec **Numpy**
- Implémentation de la méthode **SPC** (Statistical Process Control)
- Scénarios de test automatisés

**Technologies** : Python, Debian, Numpy, Communication série/TCP

---

## Contributions Open Source

Contributeur actif sur divers projets open source disponibles sur GitHub :

- Développement et maintenance de bibliothèques Python
- Contribution à des projets tiers
- Création d'outils pour la communauté

https://github.com/jgoutin

---

## Langues

- **Français** : Natif
- **Anglais** : Professionnel à l'écrit, intermédiaire à l'oral
- **Allemand** : Notions de base

---

## Disponibilité

Actuellement disponible pour des missions de conseil en tant que **freelance**.

Domaines d'intervention privilégiés :

- Architecture et développement cloud (AWS)
- Développement Python (backend, API, microservices)
- DevOps et CI/CD
- Architecture logicielle
- Sécurité cloud et système
- Migration et modernisation d'infrastructures

---

*JGoutin-dev SARL au capital de 1000€ - 994495422 R.C.S. Aix-en-Provence*

*© Tout droit réservé.*