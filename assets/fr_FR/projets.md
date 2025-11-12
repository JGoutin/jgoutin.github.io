---
title: Projets - Jérémy Goutin
---

[← Retour à la page principale](../../fr_FR)

# Projets

Cette page présente une sélection de projets significatifs réalisés au cours de ma carrière.

---

## stdapi.ai : API Compatible OpenAI pour les Services IA d'AWS
**Août 2025 - Aujourd'hui**

Création d'une API open source permettant la compatibilité des SDK OpenAI avec les services IA d'AWS et les modèles Amazon Bedrock.

Réalisation complète du projet couvrant la conception d'architecture, le développement full-stack, le déploiement d'infrastructure AWS, la rédaction de documentation technique et la stratégie de mise sur le marché. La solution fournit une couche de compatibilité établissant un pont entre les SDK OpenAI et plus de 40 modèles Amazon Bedrock ainsi que plusieurs services IA d'AWS.

Implémentation technique intégrant Amazon Bedrock pour l'orchestration des LLM, Amazon Polly pour la synthèse vocale, Amazon Transcribe pour la transcription audio et Amazon Translate. Capacités multi-modales couvrant les conversations textuelles, la génération d'images, le traitement audio et les embeddings vectoriels.

Infrastructure déployée sur AWS avec architecture multi-régions, observabilité CloudWatch et images de conteneurs durcies. Modèle de double licence (AGPL-3.0 et licence commerciale AWS Marketplace) établi pour équilibrer contribution à la communauté open source et viabilité en entreprise.

* Site du projet : [https://stdapi.ai](https://stdapi.ai)
* GitHub : [https://github.com/stdapi-ai/stdapi.ai](https://github.com/stdapi-ai/stdapi.ai)

---

## Plateforme IA/LLM d'Entreprise
**Juillet 2025 - Août 2025**

Création d'une solution centralisée pour exploiter des modèles LLM tout en assurant la gouvernance des données.

Déploiement d'une plateforme LLM sur l'infrastructure AWS. Le cœur de cette solution est un chatbot conçu comme le point d'accès unique et contrôlé aux capacités d'intelligence artificielle. Ce chatbot assure une gouvernance stricte de l'utilisation des modèles pour protéger les données de l'entreprise.

La plateforme intègre des fonctionnalités avancées telles que le RAG permettant aux modèles de fournir des réponses enrichies basées sur des documents internes. La plateforme fournie aussi la possibilité aux équipes de développement d'intégrer l'IA à leurs IDE afin de générer et d'améliorer le code.

L'architecture s'appuie sur le service AWS Bedrock pour l'accès et la gestion d'un portefeuille varié de modèles de langage.

---

## Migration de Runners GitLab vers une Architecture Serverless AWS
**Mars 2025 - Juin 2025**

Mise en place d'une infrastructure de CI/CD dynamique et sécurisée via l'intégration des runners GitLab avec AWS ECS/Fargate et CodeBuild.

Pour les tâches génériques telles que l'exécution de Terraform, curl ou divers linters, des runners Gitlab basés sur ECS Fargate ARM ont été déployés.

Pour les tâches de compilation et de construction spécifiques aux langages de programmation, des runners Gitlab exploitant AWS CodeBuild ont été mis en place, tirant parti du support natif des environnements de développement.

La sécurité a été renforcée par l'abandon des access keys AWS IAM statiques au profit de rôles IAM temporaires et à moindre privilège. La gestion des secrets, notamment pour l'accès aux registres Docker et aux dépôts Maven et NPM, a été centralisée et sécurisée.

Les gains obtenus sont une amélioration notable des performances, une réduction des temps d'attente et des congestions de jobs grâce à une scalabilité à la demande, et une optimisation significative des coûts opérationnels. Une simplification de la configuration des pipelines au sein des fichiers gitlab-ci.yml, et la possibilité de construction d'images Docker pour l'architecture ARM64.

---

## Standardisation d'Infrastructure AWS avec Terraform
**Octobre 2023 - Octobre 2024**

Développement d'architectures de référence via des modules Terraform pour simplifier, accélérer et sécuriser les mises en production.

Le but principal étant de passer d'une infrastructure historiquement centrée sur des instances EC2 à une architecture moderne exploitant pleinement la puissance des services managés AWS (ECS, Aurora, Lambda, SQS, SES, ...).

Ce projet s'est concentré sur la création de modules Terraform réutilisables et standardisés.

Ces modules proposent une interface d'utilisation épurée, conçue pour être accessible aux non-experts, tout en encapsulant une configuration avancée et complexe.

Chaque module intègre nativement les bonnes pratiques de sécurité, incluant une gestion fine des permissions avec IAM (aidant à la création de poliques moindres privilèges), une segmentation réseau via les security groups, le chiffrement systématique des données et le monitoring Cloudwatch.

Gains : Réduction notable du temps de mise en place de nouvelles applications, augmentation de la fiabilité par la standardisation, amélioration de la posture de sécurité globale et simplification de la maintenance des infrastructures. Adoption des processus DevOps par les équipes de développement.

---

## Architecture Réseau AWS Multi-Compte avec VPC Partagé et Optimisation des Coûts
**Octobre 2023 - Avril 2024**

Refonte complète de l'infrastructure réseau distribuée pour centraliser la gestion et réduire significativement les coûts opérationnels.

Ce projet consistait à restructurer une architecture AWS multi-compte en remplaçant une Transit Gateway coûteuse par une solution basée sur AWS Resource Access Manager (RAM). L'approche centralisée utilise un VPC unique hébergé dans un compte dédié, avec partage de sous-réseaux spécialisés vers les comptes projets via AWS RAM.

L'architecture segmente les environnements en zones d'isolation distinctes (publique, privée, etc.) tout en mutualisant les ressources critiques : VPC endpoints, NAT Gateway et autre composants réseau. Cette consolidation élimine la duplication de ressources et optimise l'allocation des plages IPv4 internes.

La sécurité s'appuie sur une stratégie de moindre privilège avec des Network Access Control Lists (NACL) et Security Groups moindres privilèges. AWS Network Firewall et Route 53 Resolver Firewall assurent une protection périmétrique globale. L'infrastructure supporte le dual-stack IPv4/IPv6.

Les communications inter-projets et avec l'infrastructure on-premise sont uniformisées via un routage centralisé configurable. L'observabilité est effectuée de manière centralisée avec CloudWatch.

L'Infrastructure est entièrement gérée en IaC avec Terraform, avec intégration directe dans les modules d'entreprise existants. Cette approche standardise le déploiement et simplifie l'adoption par les équipes techniques.

Les bénéfices incluent une réduction substantielle des coûts d'infrastructure, une simplification opérationnelle, une sécurité renforcée et une réduction significative de la dette technique réseau.

---

## Marketplace FPGA avec Architecture Cloud Native
**Novembre 2021 - Avril 2023**

Architecture Cloud & logiciel d'une plateforme spécialisée pour la distribution d'applications FPGA, intégrant une gestion avancée des licences, différents modèles de facturation (abonnement, paiement à l'usage) et l'hébergement de ressources applicatives telles que paquets Linux et documentation.

Infrastructure Cloud intégralement automatisée via Terraform : backend sur AWS avec EC2, Aurora Serverless, Application Load Balancer, autoscaling et Global Accelerator. Frontend distribué avec Amazon S3 et CloudFront. Ensemble de micro-services en Python opérant sur AWS Lambda, interfaçage avec DynamoDB, SQS, SNS, et gestion de notifications via SES. Authentification centralisée par Amazon Cognito et monitoring en temps réel assuré par CloudWatch. Construction d'images EC2 avec Ansible et Packer.

Modèles de données SQL (PostgreSQL via SQLAlchemy core) et NoSQL (DynamoDB). Backend principal réalisé en Python/FastAPI.

Intégration de tests automatisés couvrant l'ensemble des flux métiers. Automatisation complète des pipelines CI/CD avec Azure Pipelines. Promotion des bonnes pratiques DevOps.

Migration depuis une version antérieure avec gestion de la rétrocompatibilité.

Les bénéfices se traduisent par une haute disponibilité, une sécurité renforcée, une gestion optimisée des coûts, ainsi qu'une forte accélération du déploiement et de la maintenance.

---

## Gestionnaire de Dépôts Linux Hautement Disponible avec Intégration CI/CD et API
**Octobre 2021 - Mars 2022**

Solution de distribution de paquets DEB et RPM hautement disponible, intégrant des flux d'ajout depuis CI/CD et via une API web dédiée.

Architecture reposant entièrement sur des composants serverless AWS : stockage des artefacts sur S3, distribution par CloudFront, déclenchement des traitements par S3 Event Notifications, exécution des scripts métiers dans AWS Lambda.

Développement d'une bibliothèque Python optimisée pour Lambda, responsable de la modification dynamique des métadonnées des paquets et de la gestion automatisée de la signature cryptographique.

Ajout des paquets Accelize via l'intégration continue, gestion sécurisée des packages clients et partenaires par API REST.

Principaux gains : haute disponibilité, automatisation complète du flux d'ajout et de validation des paquets, intégrité et sécurité assurées par la signature systématique, facilité d'intégration via API et CI/CD.

---

## Service d'Exécution d'Applications FPGA Conteneurisées en Cloud Hybride
**Juin 2021 - Octobre 2021**

Mise en place d'un service cloud pour l'exécution à la demande d'applications conteneurisées sur des instances FPGA depuis les pages web des produits.

L'architecture repose sur un backend et un orchestrateur 100% serverless, s'appuyant sur les services AWS Lambda, S3, SQS, CloudFront et ECR. Cette infrastructure pilote le déploiement des applications sur des instances d'exécution hétérogènes, supportant un environnement multi-cloud incluant Amazon EC2 et OpenStack Nova.

Le projet a adressé plusieurs contraintes techniques majeures. Pour la maîtrise des coûts, un mécanisme de provisionnement et de résiliation automatique des instances FPGA a été développé. La compatibilité multi-cloud a été assurée par une couche d'abstraction logicielle. L'utilisation d'applications conteneurisées avec Docker a nécessité des configurations spécifiques de l'hôte Linux pour permettre l'interaction entre le conteneur et le matériel FPGA. La plateforme garantit également la sécurité et la confidentialité des exécutions, même pour des sessions publiques lancées sans authentification.

Les gains obtenus sont une scalabilité élevée et une optimisation des coûts grâce à l'automatisation du cycle de vie des instances. Le service offre une infrastructure sécurisée et flexible, capable de supporter des démonstrations publiques de produits directement depuis des pages web.

---

## ACID : Agents Cloud Dynamiques pour Azure Pipelines
**Juin 2021**

Exécution de jobs Azure Pipelines sur des agents éphémères provisionnés à la demande sur AWS EC2 et Azure VM.

Développement d'un utilitaire permettant de lancer des jobs Azure Pipelines sur des agents auto-hébergés, créés sur des instances cloud temporaires. L'outil s'appuie sur Terraform pour automatiser le provisionnement et la suppression des ressources sur AWS EC2 et Azure Virtual Machines. La configuration logicielle de ces agents est assurée par des playbooks Ansible, proposant une personnalisation complète de l'environnement d'exécution.

Le cycle de vie de l'agent est entièrement géré au sein du pipeline. Une instance est démarrée juste avant le job qui en a besoin et est automatiquement détruite à la fin de celui-ci. Le système supporte l'utilisation d'images d'OS génériques et a été initialement conçu pour permettre l'accès à des configurations matérielles spécifiques et coûteuses, comme les instances FPGA de type AWS F1. L'utilisation d'instances spot est également intégrée pour minimiser les coûts.

Les gains principaux sont une réduction drastique des coûts d'infrastructure grâce à l'élimination des agents permanents, et une flexibilité accrue permettant d'utiliser des configurations matérielles spécialisées uniquement lorsque c'est nécessaire. L'automatisation complète du processus simplifie la gestion des agents et optimise l'utilisation des ressources cloud.

---

## Migration et Administration d'une Infrastructure Cloud Microsoft
**Avril 2021 - Juin 2021**

Pilotage de la refonte complète de l'infrastructure IT suite à une scission d'entreprise, incluant la migration des services, l'implémentation du SSO et la modernisation de la chaîne CI/CD.

Dans le cadre de la séparation d'avec PLDA Group, ce projet a consisté à créer un environnement IT entièrement autonome. Le cœur de l'opération a été la migration stratégique de l'écosystème Google Workspace vers Microsoft 365, avec une transition des identités vers Azure Active Directory (Azure AD) comme annuaire central.

Pour sécuriser et fluidifier les accès, une fédération d'identités via Single Sign-On (SSO) a été configurée pour des services critiques tels que Jira, Lucca et Google. Sur le plan des opérations de développement, la chaîne d'outils a été rationalisée en remplaçant les systèmes Jenkins et AWS CodeBuild par Azure DevOps, établissant une plateforme CI/CD unifiée pour l'intégration et le déploiement continus.

La gestion du parc informatique a également été modernisée par la mise en place de Microsoft Intune pour le provisionnement et la gestion des politiques de sécurité sur les postes Windows & Linux (Fedora).

Gains : Le projet a permis d'établir une autonomie IT complète, d'accroître la posture de sécurité via une gestion centralisée des identités et des accès et d'améliorer les processus de CI/CD.

---

## Ansible Home : Collection Ansible pour le Déploiement de Services Libres Auto-Hébergés
**Octobre 2019 - Octobre 2021**

Développement d'une collection Ansible pour l'auto-hébergement de logiciels libres avec sécurité renforcée.

Création d'une collection Ansible structurée comprenant des rôles spécialisés pour l'installation et la configuration automatisée de services open source.

Implémentation des rôles principaux incluant Nextcloud pour le stockage cloud, Squid comme proxy cache, Kodi pour le media center, et MPD pour la lecture audio.

Développement de rôles de dépendances modulaires : Nginx, PostgreSQL, PHP-FPM, et Valkey pour une architecture décentralisée.

Intégration d'un rôle "common" centralisant les tâches d'initialisation système : configuration du pare-feu, durcissement SELinux, gestion des mises à jour automatiques, et sécurisation SSH.

Adoption de Fedora comme système d'exploitation de base pour bénéficier des dernières versions logicielles et des fonctionnalités de sécurité avancées.

Mise en place d'un workflow CI/CD avec GitHub Actions pour la validation et le déploiement.

Les gains incluent une réduction drastique du temps de déploiement, une standardisation des configurations et une maintenance simplifiée.

---

## Modernisation de l'Infrastructure et la Sécurité Cloud AWS avec Terraform
**Janvier 2019 - Janvier 2020**

Refonte complète d'une plateforme AWS via l'Infrastructure as Code pour renforcer la sécurité en vue d'un audit externe.

Le projet a consisté à moderniser l'infrastructure de la plateforme Accelize V1 sur AWS en abandonnant la gestion manuelle au profit d'une approche Infrastructure as Code et GitOps. L'intégralité de l'environnement a été redéfinie à l'aide de Terraform pour garantir la reproductibilité, la traçabilité et l'auditabilité des ressources déployées.

Un accent particulier a été mis sur le renforcement de la sécurité en préparation d'un audit externe. Cela a impliqué une révision stricte des politiques AWS IAM, la segmentation du réseau via des VPC, et l'intégration de Security Hub pour une surveillance centralisée des menaces.

Les services applicatifs existants étaient structurés autour d'Elastic Beanstalk, d'instances EC2, de bases de données RDS, d'Application Load Balancer, de S3, de fonctions Lambda et de Route 53.

Les gains obtenus sont une infrastructure entièrement gérée et versionnée via Terraform, éliminant les dérives de configuration. Le projet a permis le passage réussi de l'audit de sécurité avec d'excellents résultats.

---

## Accelpy : Déploiement d'Applications FPGA
**Juillet 2019 - Octobre 2019**

Outil d'automatisation pour le provisionnement et le déploiement d'applications FPGA sur des infrastructures cloud et on-premise.

Cet outil en ligne de commande, intégré à la plateforme Accelize, orchestre le déploiement de solutions matérielles accélérées par FPGA. Il interagit avec les API de la plateforme pour gérer le cycle de vie des designs FPGA, de la sélection du bitstream jusqu'à la configuration finale de la cible matérielle.

Accelpy automatise le provisionnement des ressources, que ce soit sur des instances FPGA dans le cloud ou sur des serveurs on-premise. Le processus inclut le téléchargement sécurisé des bitstreams, la programmation des puces FPGA, et la mise en place des environnements logiciels hôtes. La gestion des artefacts de déploiement s'appuie sur les solutions de stockage objets du cloud où sont provisionnées les instances afin de réduire la latence.

La mise en service d'une application FPGA est ainsi drastiquement simplifié et accéléré.

---

## Environnement de Développement Interne sur AWS
**Juin 2019 - Juillet 2019**

Mise en place d'un environnement de développement AWS sécurisé, automatisé et à coût maîtrisé.

Ce projet a consisté à déployer un environnement de développement interne sur AWS, en mettant l'accent sur la sécurité et l'optimisation.

L'architecture repose sur un réseau isolé via un VPC. La sécurité a été renforcée par l'implémentation d'un modèle à double niveau. En plus des politiques IAM basées sur le principe du moindre privilège, un système d'ownership des ressources a été développé pour assurer une attribution claire et un contrôle d'accès des ressources à leurs utilisateurs.

L'automatisation est au cœur de la gestion des coûts et de la maintenance. Des fonctions Lambda, orchestrées par EventBridge, ont été mises en place pour détecter et résilier automatiquement les ressources orphelines, comme les volumes EBS non attachés ou les instances EC2 inutilisées. De plus, le service DLM a été configuré pour automatiser la création et la gestion des sauvegardes des instances EC2. Enfin, le chiffrement KMS est activé par défaut pour EBS.

Les gains obtenus sont une posture de sécurité renforcée, une réduction significative des coûts grâce à l'élimination du gaspillage de ressources, et une garantie de la pérennité des données.

---

## Apyfal : Déploiement Cloud d'Applications FPGA
**Avril 2018 - Avril 2019**

Orchestration de l'exécution d'applications matérielles sur des instances FPGA distantes via une API Python.

Développement d'Apyfal, une solution logicielle facilitant l'accélération de calculs sur des FPGA disponibles dans le cloud. Le projet a permis de créer un client Python simple d'usage, capable de piloter à distance le cycle de vie complet d'une application, de son déploiement à son exécution sur des infrastructures matérielles spécialisées.

L'architecture repose sur une API RESTful pour la communication entre le client et le serveur d'orchestration. Ce dernier gère dynamiquement les ressources FPGA, incluant la programmation des bitstreams et l'allocation des instances.

Cette solution a permis de réduire significativement la complexité d'accès aux accélérateurs matériels FPGA pour les développeurs logiciels. Elle a ainsi offert un gain de productivité en abstrayant l'hétérogénéité des plateformes cloud et en automatisant entièrement le provisionnement des ressources, rendant l'accélération matérielle aussi accessible qu'une simple librairie logicielle.

---

## Airfs (Pycosio) : Bibliothèque Python Unifié pour le Stockage Cloud
**Juillet 2018 - Février 2021**

Unifie l'accès aux stockages cloud et systèmes de fichiers locaux via une API Python standard.

Développement d'une bibliothèque Python offrant une interface de programmation unifiée pour interagir avec divers systèmes de stockage distants et cloud. L'architecture est calquée sur les API de la bibliothèque standard Python pour la manipulation de fichiers locaux.

Le cœur technique du projet repose sur l'implémentation des classes abstraites "io.RawIOBase" et "io.BufferedIOBase". Cette conception garantit une compatibilité directe avec les modules natifs comme "io", "os", "os.path" et "shutil". Elle rend la manipulation d'objets sur le cloud transparente et interchangeable avec celle des fichiers sur un système de fichiers local.

La bibliothèque intègre des fonctionnalités avancées pour les objets bufferisés afin d'optimiser les performances. Celles-ci incluent l'écriture et le pré-chargement (prefetching) asynchrones, des mécanismes de verrouillage basés sur l'utilisation de la mémoire, et l'usage de connexions parallèles pour maximiser la bande passante. Le projet supporte de multiples fournisseurs comme AWS S3, Azure Blob Storage, Azure Files, OpenStack Swift et l'accès via HTTP/HTTPS.

Initialement créé sous le nom "pycosio", le projet a été repris sous forme de "fork" pour être étendu et maintenu.

Les gains principaux sont une abstraction de haut niveau qui simplifie le code applicatif et le rend agnostique à la source des données. Cela améliore la portabilité et la maintenabilité du code tout en garantissant des transferts de données à haute performance.

---

## Évolution d'un Logiciel de Banc de Test pour Cartes Électroniques
**Octobre 2017 - Avril 2018**

Développement de fonctionnalités critiques pour un banc de test industriel en environnement Python sous Debian.

Ce projet portait sur l'amélioration d'un logiciel de test utilisé dans un contexte de fabrication industrielle. Les développements ont inclus l'instrumentation logicielle pour le pilotage et la communication avec divers équipements de mesure. Une des évolutions majeures a été la mise en place d'une architecture client/serveur pour améliorer la supervision et la collecte des données de test.

L'optimisation des performances a été un axe central, avec l'utilisation de la bibliothèque Numpy pour accélérer les calculs sur les jeux de données importants. De nouveaux scénarios de test ont été implémentés pour étendre la couverture de validation des cartes électroniques.

Un démonstrateur a également été développé pour intégrer la méthode d'analyse SPC (Statistical Process Control). Cet outil visait à fournir des outils d'analyse statistique pour faciliter l'interprétation des mesures et la détection précoce de dérives dans le processus de fabrication.

---

## Compilertools : Création de Paquets Binaires Python Hautes Performances
**Février 2017 - Décembre 2017**

Une bibliothèque Python pour la création et la distribution de paquets binaires hautes performances tirant parti des architectures CPU modernes.

Ce projet fournit une solution complète pour la compilation de code, notamment les extensions C et C++, en paquets Python binaires.

La librairie détecte et utilise les jeux d'instructions avancés des processeurs, tels que SIMD (AVX, SSE), pour générer des binaires spécifiquement optimisés pour la machine cible. Le système gère la complexité des différentes chaînes de compilation et des architectures matérielles, offrant un processus de construction transparent. Il s'intègre avec les outils de packaging Python standards pour faciliter la distribution sur des dépôts comme PyPI.

Cette approche permet de distribuer des applications Python offrant des performances maximales dès l'installation, sans nécessiter de compilation manuelle par l'utilisateur final. Les gains en vitesse d'exécution sont significatifs pour les applications de calcul intensif ou de traitement de données, tout en simplifiant le processus de déploiement.

---

## Fazpy : Logiciel d'Analyse de Mesures Optiques et de Pilotage de Production
**Octobre 2014 - Septembre 2017**

Conception d'une solution logicielle complète pour le traitement de données de métrologie optique et la génération de réglages pour les équipements de production.

Ce projet a consisté en la conception et la réalisation d'une application de bureau complète sous Windows avec le langage Python. L'interface utilisateur, développée avec le framework Qt, offre aux ingénieurs en optique et mécanique un outil dédié à l'analyse de mesures complexes, notamment issues de l'interférométrie. Le cœur du logiciel repose sur des modules de calculs optiques et de traitement d'image avancés.

Une attention particulière a été portée à la performance, nécessitant l'optimisation des algorithmes de calcul et la recherche de solutions spécifiques pour le traitement de grands volumes de données.

L'architecture logicielle a été conçue pour être modulaire et évolutive, intégrant plus de 70 briques fonctionnelles distinctes, allant de l'acquisition de données à la visualisation des résultats.

Gains: Le logiciel permet d'automatiser et de fiabiliser l'analyse des mesures, tout en créant un lien direct entre le contrôle qualité et la fabrication. Il en résulte une réduction des cycles de développement et une amélioration de la précision des pièces produites.

---

[← Retour à la page principale](../../fr_FR)

---

*Microentreprise enregistrée en France - Siren 978307999 - Siret 97830799900018*

*© Tout droit réservé.*
