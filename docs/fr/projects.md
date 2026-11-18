---
title: Projets
description: Sélection de projets représentatifs sur plus de 10 ans de conseil en logiciel, cloud et DevOps
keywords: portfolio, études de cas, projets, agents IA, livraison agentique, Claude Code, TDD, revue de code, tests de mutation, coût LLM, sécurité IA, inférence locale, architecture cloud, AWS, DevOps, Terraform, LLM, Python
---

# Projets

Une sélection de projets représentatifs réalisés sur plus de 10 ans
d'expérience. Les plus récents ont été réalisés avec des agents IA, selon la
méthode de [livraison agentique](#livraison-agentique-skills-et-workflows-de-jalons-longue-duree).

## :material-email-fast: Assistant e-mail IA avec RAG et actions encadrées

!!! abstract "Juin 2026 – septembre 2026 &middot; JGoutin-dev &middot; En production"

    **Stack :** Amazon Bedrock (Nova, Knowledge Bases, S3 Vectors), AWS Lambda,
    SES, DynamoDB, EventBridge, Python, OpenTofu

Un assistant qui répond aux e-mails des clients et agit en conséquence : ici,
des offres commerciales privées pour un produit logiciel.

Il détermine ce que demande chaque client et dans quelle langue, crée l'offre
via l'API de la place de marché, la suit jusqu'à son acceptation ou son
expiration, et répond aux questions techniques à partir de la documentation
du produit (**RAG** sur une Bedrock Knowledge Base, avec liens vers les
sources).

**Le modèle classe, traduit et rédige ; le code déterministe décide de chaque
action**, avec des prix et des conditions issus uniquement de la
configuration. Les e-mails ambigus vont à un humain, et un humain est en
copie de chaque réponse. Des cas d'injection de prompt et des tests sur le modèle réel
passent à chaque modification. Conçu pour le RGPD : région UE, rétention
limitée, aucun corps d'e-mail dans les journaux.

## :material-robot-industrial: Livraison agentique — skills et workflows de jalons longue durée

!!! abstract "Avril 2026 – présent &middot; JGoutin-dev"

    **Stack :** Claude Code (skills, subagents, workflows), Git, GitHub,
    Python, Rust, contrôles qualité en CI

Un système de livraison dans lequel des agents IA construisent des versions
complètes de bout en bout, utilisé sur un produit open source et sur une
application Rust privée.

Une seule commande exécute un jalon entier : un plan relu avant tout code,
les tests écrits d'abord, l'implémentation, la revue et une version candidate
testée sur le vrai AWS. Un humain valide le résultat, la publication et toute
action risquée. Les **contrôles ne peuvent pas être contournés** (100 % de
couverture sur le code critique, tests de mutation, chaîne
d'approvisionnement) : la CI et les permissions les imposent, pas les
prompts. Des agents indépendants traquent bugs et failles, un autre tente de
réfuter chaque constat, et une correction ne compte que si son nouveau test
échoue sans elle.

Le travail reprend proprement après des heures ou des semaines, le modèle le
plus capable et tous les contrôles ne servent que là où les données ou la
sécurité sont en jeu, la consommation de tokens est mesurée, et 14 skills
portent le savoir d'un produit.

Mesuré sur l'application Rust privée : environ 200 000 lignes de code et
370 000 lignes de tests en 27 jours, plus de 1 200 agents et 3 151 constats
de revue, dont 40 % confirmés et corrigés.

[Apportez cette méthode à votre équipe](contact.md){ .md-button .md-button--primary }

## :material-chip: Optimisation de l'inférence IA locale et inference box

!!! abstract "Juillet 2026 – présent &middot; Projet ouvert"

    **Stack :** llama.cpp, Lemonade, stable-diffusion.cpp, ROCm, Vulkan,
    GPU AMD et Ryzen AI Max, Fedora CoreOS, Python

Faire tourner de grands modèles rapidement sur du matériel local, et
transformer ce savoir-faire en appliance d'inférence auto-hébergée.

Une méthode de réglage pour les serveurs llama.cpp et les modèles d'image :
dimensionnement d'un modèle selon le budget mémoire, placement des couches
*mixture of experts* entre GPU et CPU, placement du KV cache et décodage
spéculatif, chacun mesuré par des exécutions répétées. Mesuré sur un GPU de
station de travail : **+76 % en traitement du prompt et +21 % en
génération** par rapport au placement automatique, **+27 % à +58 %** grâce
au décodage spéculatif, et une génération d'images **1,8× plus rapide**.

L'**inference box** applique cela aux machines AMD Ryzen AI Max : un serveur
IA privé clé en main, sur un OS immuable durci, avec sa propre interface
d'administration. Elle est en conception, avec une première machine utilisée
pour les mesures.

## :material-image-auto-adjust: Pipeline de génération d'images à originalité contrôlée et contrôle qualité automatique

!!! abstract "Août 2026 &middot; R&D JGoutin-dev &middot; Prototype"

    **Stack :** Python, LLM et modèles de vision locaux, Lemonade,
    stable-diffusion.cpp, skill Claude Code

Un pipeline local qui produit des images originales l'une après l'autre,
conçu pour éviter les répétitions et les défauts.

Les modèles de langage sont peu doués pour le hasard, donc **le code le fournit** :
il tire des mots-clés et des règles de composition, et un modèle de langage
guidé par un skill en fait un prompt cohérent. Après la génération locale,
un **modèle de contrôle inspecte chaque image** à la recherche de défauts
visuels. Une image défectueuse est régénérée, et le prompt est corrigé quand
un défaut revient.

## :material-shield-lock: Sécuriser les agents IA — isolation et broker d'accès

!!! abstract "Septembre 2026 – présent &middot; R&D JGoutin-dev"

    **Stack :** Rust, Linux (ACL, nftables, Landlock, seccomp, cgroups,
    FUSE), KeePassXC, Kani, microVM (smolvm), Wolfi, bubblewrap

Laisser des agents IA travailler en autonomie sans leur confier les clés de
la machine : la frontière de sécurité est le système d'exploitation, pas les
demandes d'autorisation de l'agent lui-même. Les agents s'exécutent sous un
utilisateur séparé et sans privilèges qui n'accède ni au répertoire
personnel du propriétaire, ni à ses identifiants, ni au `git push`, et les
modifications de sa propre configuration exigent l'accord du propriétaire.

Un **broker d'accès** en Rust prête un accès pour une durée limitée, en une
commande : secrets KeePassXC (à usage unique ou validés sur le bureau si
besoin, avec rotation des jetons), connexions SSH signées uniquement pour les
hôtes autorisés, dossiers du NAS montés via un programme auxiliaire isolé
(Landlock, seccomp, cgroups), en lecture seule par défaut ou modifiables dans
un budget d'écriture, et services locaux ouverts dans le pare-feu. Les
valeurs passent directement de KeePassXC à la commande qui les utilise,
jamais par le modèle, et chaque usage est audité. Le broker est un binaire
statique reproductible qui ne dépend que de la crate `libc`, avec des preuves
Kani parmi ses contrôles de publication.

Un prototype antérieur exécutait chaque agent dans une microVM minimale
basée sur Wolfi, et des contrôles de la chaîne d'approvisionnement couvrent
ce que les agents installent.

## :material-server-network: Plateforme Kubernetes auto-hébergée opérée avec un agent IA

!!! abstract "Septembre 2026 – présent &middot; Infrastructure personnelle"

    **Stack :** Talos Linux, Kubernetes, Flux, Forgejo, Cilium,
    cert-manager, CloudNativePG, Grafana, Renovate, SOPS, gVisor, TrueNAS

Une plateforme auto-hébergée conçue, construite et exploitée avec un agent
IA : Kubernetes sur Talos Linux, GitOps avec Flux depuis une forge
auto-hébergée, mises à jour automatiques qui s'arrêtent au premier échec,
sauvegardes chiffrées avec restaurations testées, supervision et charges de
travail isolées.

L'agent prépare chaque changement (scripts, essais à blanc) et dispose d'un
**accès en lecture seule à la production, sans aucun identifiant d'écriture
permanent**. Les étapes en lecture seule s'exécutent librement, les étapes
réversibles sont signalées, et les étapes risquées exigent un plan, un retour
arrière et l'accord du propriétaire ; les identifiants d'écriture ne sont
prêtés que pour une exécution. Plus de 120 décisions d'architecture sont
consignées.

## :material-school: Skills Claude Code pour les équipes clientes

!!! abstract "Juillet 2026 – présent &middot; Freelance"

    **Stack :** Claude Code (skills, agents, hooks), Git, CI/CD

Conception et maintenance de skills d'agents IA pour les équipes de
développement clientes, pour que les agents travaillent comme l'équipe :
skills de base de connaissances sur l'architecture et les conventions de
l'entreprise, skills de workflow de développement (TDD, contrôles qualité,
revue de code, publications) et skills git. Les skills évoluent avec les
outils, les modèles et les pratiques de l'équipe.

## :material-rocket-launch: stdapi.ai — passerelle IA open source compatible avec les API OpenAI, Anthropic, Cohere et Ollama

!!! abstract "Août 2025 – novembre 2026 &middot; Open source"

    **Stack :** AWS (Bedrock, Lambda, ECS, CloudWatch), Python, FastAPI,
    IA multimodale, MCP · **Lien :**
    [:fontawesome-brands-github: GitHub](https://github.com/stdapi-ai/stdapi.ai)

API *open source* qui faisait fonctionner les SDK OpenAI, Anthropic, Cohere
et Ollama avec plus de 100 modèles Amazon Bedrock et les services IA d'AWS.
AWS l'a approuvée comme **AWS Qualified Software**, après l'avoir vérifiée au
regard de ses exigences techniques et de sécurité. Le projet est arrêté, et
son code source reste disponible.

Projet de bout en bout : architecture, développement, déploiement AWS,
documentation et mise sur le marché. Il couvrait le chat, la génération
d'images et de vidéos, la synthèse et la transcription vocales (**Amazon
Polly**, **Amazon Transcribe**), la traduction, les *embeddings*, les batchs,
les *vector stores*, la voix en
temps réel et un **serveur MCP** référencé dans le registre MCP officiel. Les
contrôles multi-tenant couvraient des clés d'API à périmètre limité, des
limites de débit et de tokens, et le suivi des coûts par utilisateur.

Déployé sur AWS dans plusieurs régions avec des images de conteneur durcies,
et publié sous licence AGPL-3.0. **Plus de 6 000 tests automatisés exécutés
sur le vrai AWS**, 20 outils tiers (Claude Code, Open WebUI, n8n, LangChain,
…) testés de bout en bout, et 43 versions publiées en moins d'un an.

## :material-brain: Plateforme IA / LLM d'entreprise

!!! abstract "Juillet 2025 – août 2025 &middot; Freelance"

    **Stack :** Amazon Bedrock, Python, RAG, LLM, IA

Solution centralisée pour exploiter les modèles LLM tout en garantissant
une stricte gouvernance des données.

Plateforme déployée sur infrastructure AWS, dont le cœur est un *chatbot*
conçu comme point d'accès unique et contrôlé aux capacités d'IA. Cette
gouvernance assure la protection des données sensibles de l'entreprise.

La plateforme intègre des fonctionnalités avancées telles que **RAG**, qui
permettent aux modèles de fournir des réponses enrichies à partir de
documents internes. Les équipes de développement peuvent également intégrer
l'IA directement dans leur IDE pour générer et améliorer leur code.

L'architecture s'appuie sur **Amazon Bedrock** pour l'accès à un portefeuille
diversifié de modèles de langage.

## :simple-gitlab: Migration des GitLab Runners vers une architecture *serverless* AWS

!!! abstract "Mars 2025 – juin 2025 &middot; Freelance"

    **Stack :** GitLab CI/CD, AWS (ECS Fargate, CodeBuild, IAM), Docker,
    ARM64

Mise en place d'une infrastructure CI/CD dynamique et sécurisée par
intégration des GitLab Runners avec AWS ECS/Fargate et CodeBuild.

Pour les tâches génériques (Terraform, `curl`, *linters*), des GitLab
Runners basés sur **ECS Fargate ARM** ont été déployés. Pour les tâches de
compilation et de *build* spécifiques à un langage, des GitLab Runners
exploitant **AWS CodeBuild** ont été mis en œuvre, tirant parti du support
natif des environnements de développement.

La sécurité a été renforcée par l'abandon des clés d'accès IAM AWS statiques
au profit de **rôles IAM temporaires au moindre privilège**. La gestion des
secrets — notamment pour les *registries* Docker et les dépôts Maven et NPM —
a été centralisée et sécurisée.

Bénéfices : amélioration notable des performances, réduction des temps
d'attente et de la congestion grâce à la mise à l'échelle à la demande, et
optimisation significative des coûts opérationnels. Configuration des
*pipelines* simplifiée dans les fichiers `gitlab-ci.yml`, et capacité à
construire des images Docker pour l'architecture ARM64.

## :simple-terraform: Standardisation de l'infrastructure AWS avec Terraform

!!! abstract "Octobre 2023 – octobre 2024 &middot; Freelance"

    **Stack :** Terraform, AWS (ECS, Aurora, Lambda, SQS, SES, IAM),
    Infrastructure as Code

Architectures de référence développées sous forme de modules Terraform
réutilisables pour simplifier, accélérer et sécuriser les déploiements en
production.

L'objectif principal était de faire évoluer une infrastructure historiquement
centrée sur les instances EC2 vers une architecture moderne tirant pleinement
parti des services managés AWS (ECS, Aurora, Lambda, SQS, SES, …).

Les modules exposent une interface simplifiée, accessible aux non-experts,
tout en encapsulant des configurations avancées et complexes. Chaque module
intègre nativement les bonnes pratiques de sécurité : permissions IAM
granulaires (politiques au moindre privilège), segmentation réseau via
*security groups*, chiffrement systématique des données et supervision
CloudWatch.

Bénéfices : réduction notable du temps de mise en place des applications,
fiabilité accrue par la standardisation, posture de sécurité globale
renforcée et maintenance simplifiée — accompagnés de l'adoption des
processus DevOps par les équipes de développement.

## :fontawesome-brands-aws: Architecture réseau AWS multi-comptes avec VPC partagé et optimisation des coûts

!!! abstract "Octobre 2023 – avril 2024 &middot; Freelance"

    **Stack :** AWS VPC, Terraform, Network Firewall, Route 53, VPN

Refonte complète de l'infrastructure réseau distribuée pour centraliser la
gestion et réduire significativement les coûts opérationnels.

Ce projet a restructuré une architecture AWS multi-comptes en remplaçant un
Transit Gateway coûteux par une solution basée sur AWS Resource Access
Manager (RAM). L'approche centralisée repose sur un VPC unique hébergé dans
un compte dédié, avec partage spécifique de sous-réseaux vers les comptes
projet via AWS RAM.

L'architecture segmente les environnements en zones d'isolation distinctes
(public, privé, …) tout en mutualisant les ressources critiques : *VPC
endpoints*, NAT Gateway et autres composants réseau. Cette consolidation
élimine la duplication des ressources et optimise l'allocation interne des
plages IPv4.

La sécurité repose sur une stratégie au moindre privilège avec NACL et
*Security Groups* restreints. **AWS Network Firewall** et **Route 53
Resolver Firewall** assurent la protection périmétrique globale.
L'infrastructure prend en charge la double pile IPv4/IPv6.

Les communications inter-projets et avec l'infrastructure *on-premise* sont
standardisées par un routage centralisé configurable. L'observabilité est
centralisée dans CloudWatch. L'infrastructure est entièrement gérée comme
code via Terraform, avec intégration directe aux modules d'entreprise
existants.

Bénéfices : réduction substantielle des coûts d'infrastructure, simplification
opérationnelle, sécurité renforcée et réduction significative de la dette
technique réseau.

## :material-chip: Marketplace FPGA avec architecture *cloud-native*

!!! abstract "Novembre 2021 – avril 2023 &middot; Accelize"

    **Stack :** AWS (EC2, Lambda, S3, CloudFront, Cognito, DynamoDB, RDS),
    Python, FastAPI, SQLAlchemy, PostgreSQL, Terraform

Architecture cloud et logiciel pour une plateforme spécialisée de
distribution d'applications FPGA, intégrant une gestion avancée des licences,
plusieurs modèles de facturation (abonnement, *pay-per-use*) et l'hébergement
de ressources telles que des paquets Linux et de la documentation.

Infrastructure cloud entièrement automatisée par Terraform : *backend* sur
AWS avec EC2, Aurora Serverless, Application Load Balancer, *autoscaling* et
Global Accelerator. *Frontend* distribué via Amazon S3 et CloudFront.
Microservices Python sur AWS Lambda interfacés avec DynamoDB, SQS, SNS et
SES pour les notifications. Authentification centralisée via Amazon Cognito
et supervision en temps réel par CloudWatch. Construction d'images EC2 avec
Ansible et Packer.

Modèles de données SQL (PostgreSQL via SQLAlchemy Core) et NoSQL (DynamoDB).
*Backend* principal en Python / FastAPI.

Tests automatisés couvrant l'ensemble des flux métier. Automatisation
complète du *pipeline* CI/CD avec Azure Pipelines et promotion des bonnes
pratiques DevOps. Migration depuis une version antérieure avec gestion de la
rétrocompatibilité.

Bénéfices : haute disponibilité, sécurité renforcée, gestion optimisée des
coûts et accélération significative des déploiements et de la maintenance.

## :simple-linux: Gestionnaire de dépôts Linux haute disponibilité avec intégration CI/CD et API

!!! abstract "Octobre 2021 – mars 2022 &middot; Accelize"

    **Stack :** AWS (S3, Lambda, CloudFront), Python, CI/CD, GPG

Solution de distribution de paquets DEB et RPM hautement disponible,
intégrant des flux d'ajout depuis la CI/CD et via une API web dédiée.

L'architecture repose entièrement sur des composants *serverless* AWS :
stockage des artefacts sur S3, distribution via CloudFront, traitements
déclenchés par S3 Event Notifications et exécution des scripts métier dans
AWS Lambda.

Une bibliothèque Python optimisée pour Lambda a été développée, en charge
de la modification dynamique des métadonnées de paquets et de la gestion
automatisée des signatures cryptographiques.

Les paquets internes Accelize sont ajoutés via intégration continue ; les
paquets clients et partenaires sont gérés en toute sécurité via une API REST.

Bénéfices : haute disponibilité, automatisation complète du flux d'ajout et
de validation des paquets, intégrité et sécurité assurées par une signature
systématique, et facilité d'intégration via API et CI/CD.

## :material-docker: Service d'exécution d'applications FPGA conteneurisées en cloud hybride

!!! abstract "Juin 2021 – octobre 2021 &middot; Accelize"

    **Stack :** AWS (Lambda, CloudFront, S3, EC2), OpenStack, Docker, Python

Service cloud d'exécution à la demande d'applications conteneurisées sur
des instances FPGA, déclenché directement depuis les pages produit web.

L'architecture repose sur un *backend* et un orchestrateur 100% *serverless*
exploitant AWS Lambda, S3, SQS, CloudFront et ECR. Cette infrastructure
pilote le déploiement d'applications sur des instances d'exécution
hétérogènes, en environnement multi-cloud incluant Amazon EC2 et OpenStack
Nova.

Plusieurs contraintes techniques majeures ont été levées : maîtrise des
coûts par provisionnement et arrêt automatiques des instances FPGA ;
compatibilité multi-cloud via une couche d'abstraction logicielle ;
configurations Linux spécifiques permettant l'interaction conteneur-matériel
FPGA ; sécurité et confidentialité d'exécution, y compris pour des sessions
publiques sans authentification.

Bénéfices : forte évolutivité et optimisation des coûts grâce à
l'automatisation complète du cycle de vie des instances. Infrastructure
sécurisée et flexible permettant des démonstrations produit publiques
directement depuis des pages web.

## :fontawesome-brands-microsoft: ACID — agents cloud dynamiques pour Azure Pipelines

!!! abstract "Juin 2021 &middot; Accelize"

    **Stack :** Azure Pipelines, AWS EC2, Azure VM, Terraform, Ansible

Exécution de *jobs* Azure Pipelines sur des agents éphémères provisionnés
à la demande sur AWS EC2 et Azure VM.

Un utilitaire a été développé pour permettre l'exécution des *jobs* Azure
Pipelines sur des agents *self-hosted* créés sur des instances cloud
temporaires. L'outil exploite **Terraform** pour automatiser le
provisionnement et la suppression des ressources sur AWS EC2 et Azure
Virtual Machines. La configuration logicielle des agents est gérée par des
*playbooks* **Ansible**, offrant une personnalisation complète de
l'environnement.

Le cycle de vie de l'agent est entièrement géré au sein du *pipeline* :
une instance est démarrée juste avant le *job* qui en a besoin et est
détruite automatiquement à la fin. Le système prend en charge des images
OS génériques et a été initialement conçu pour permettre l'accès à des
configurations matérielles spécifiques et coûteuses telles que les instances
FPGA AWS F1. L'utilisation d'instances *spot* est intégrée pour réduire les
coûts.

Bénéfices : réduction drastique des coûts d'infrastructure par élimination
des agents permanents, et flexibilité accrue permettant d'utiliser des
configurations matérielles spécialisées uniquement lorsque nécessaire.

## :fontawesome-brands-microsoft: Migration et administration de l'infrastructure cloud Microsoft

!!! abstract "Avril 2021 – juin 2021 &middot; Accelize"

    **Stack :** Microsoft Azure, AAD, MS365, AWS, GitHub, PowerShell

Refonte complète de l'infrastructure informatique suite à la séparation de
l'entreprise, incluant migration des services, mise en place du SSO et
modernisation de la chaîne d'outils CI/CD.

Dans le cadre de la séparation du groupe PLDA, ce projet a permis de
constituer un environnement informatique entièrement autonome. L'opération
centrale a été la migration stratégique de l'écosystème Google Workspace
vers Microsoft 365, avec transition d'identité vers Azure Active Directory
comme annuaire central.

Pour sécuriser et fluidifier les accès, une **fédération d'identité SSO**
a été mise en place pour des services critiques tels que Jira, Lucca et
Google. Sur le plan DevOps, la chaîne d'outils a été rationalisée en
remplaçant Jenkins et AWS CodeBuild par **Azure DevOps**, créant ainsi une
plateforme CI/CD unifiée.

La gestion du parc informatique a été modernisée via **Microsoft Intune**
pour le provisionnement et l'application des politiques de sécurité sur
postes Windows et Linux (Fedora).

Bénéfices : autonomie informatique complète, posture de sécurité renforcée
par une gestion centralisée des identités et des accès, et amélioration des
processus CI/CD.

## :simple-ansible: Ansible Home — collection Ansible pour l'auto-hébergement de logiciels libres

!!! abstract "Octobre 2019 – présent &middot; Open source"

    **Stack :** Ansible, Fedora Linux, GitHub Actions, PostgreSQL, Nginx

Collection Ansible pour l'auto-hébergement de logiciels libres avec
sécurité renforcée.

La collection inclut des rôles spécialisés pour l'installation et la
configuration automatisées de services *open source* tels que **Nextcloud**
pour le stockage cloud, **Squid** comme proxy cache, **Kodi** pour le
*media center* et **MPD** pour la lecture audio.

Des rôles de dépendance modulaires couvrent **Nginx**, **PostgreSQL**,
**PHP-FPM** et **Valkey** pour une architecture décentralisée. Un rôle
*common* centralise l'initialisation système : pare-feu, durcissement
SELinux, mises à jour automatiques et durcissement SSH.

Fedora a été retenu comme système d'exploitation de base pour ses versions
logicielles récentes et ses fonctionnalités de sécurité avancées. Un
*workflow* CI/CD avec GitHub Actions assure validation et déploiement. Une mise à jour en 2026 a ajouté
la journalisation d'audit et renforcé les réglages du noyau, de la base de
données et du serveur web.

Bénéfices : réduction drastique du temps de déploiement, standardisation
des configurations et maintenance simplifiée.

## :simple-terraform: Modernisation de l'infrastructure cloud et de la sécurité AWS avec Terraform

!!! abstract "Janvier 2019 – janvier 2020 &middot; Accelize"

    **Stack :** AWS (VPC, EC2, RDS, S3, Lambda, Security Hub), Terraform

Refonte complète de la plateforme AWS via Infrastructure as Code, en
préparation d'un audit de sécurité externe.

Le projet a modernisé l'infrastructure de la plateforme Accelize V1 sur AWS
en abandonnant la gestion manuelle au profit d'une approche Infrastructure
as Code et GitOps. L'environnement complet a été redéfini avec **Terraform**
pour garantir reproductibilité, traçabilité et auditabilité.

Une attention particulière a été portée à la sécurité : revue stricte des
politiques IAM AWS, segmentation réseau via VPC et intégration de **Security
Hub** pour la supervision centralisée des menaces. Les services applicatifs
existants ont été structurés autour d'Elastic Beanstalk, EC2, RDS,
Application Load Balancer, S3, Lambda et Route 53.

Bénéfices : infrastructure entièrement gérée et versionnée via Terraform,
éliminant la dérive de configuration. Le projet a permis de réussir l'audit
de sécurité externe avec d'excellents résultats.

## :material-chip: Accelpy — déploiement d'applications FPGA

!!! abstract "Juillet 2019 – octobre 2019 &middot; Accelize"

    **Stack :** Python, AWS, OpenStack, FPGA, CLI

Outil d'automatisation du provisionnement et du déploiement d'applications
FPGA sur infrastructures cloud et *on-premise*.

Cet outil en ligne de commande, intégré à la plateforme Accelize, orchestre
le déploiement de solutions matérielles accélérées par FPGA. Il interagit
avec les API de la plateforme pour gérer le cycle de vie d'un *design* FPGA,
de la sélection du *bitstream* à la configuration finale de la cible
matérielle.

Accelpy automatise le provisionnement des ressources, qu'il s'agisse
d'instances FPGA dans le cloud ou de serveurs *on-premise*. Le processus
inclut le téléchargement sécurisé du *bitstream*, la programmation de la
puce FPGA et la configuration de l'environnement logiciel hôte. La gestion
des artefacts de déploiement repose sur du stockage objet cloud dans la
même région que les instances afin de réduire la latence.

## :fontawesome-brands-aws: Environnement de développement AWS interne

!!! abstract "Juin 2019 – juillet 2019 &middot; Accelize"

    **Stack :** AWS (IAM, EC2, CloudWatch, Lambda, EventBridge, DLM),
    Terraform, Python

Mise en place d'un environnement de développement AWS sécurisé, automatisé
et maîtrisé en coût.

L'architecture repose sur un VPC isolé. La sécurité a été renforcée par un
modèle à deux niveaux : en complément des politiques IAM au moindre
privilège, un système de **propriété des ressources** a été développé pour
assurer une attribution claire et un contrôle des accès.

L'automatisation est au cœur de la maîtrise des coûts et de la maintenance.
Des fonctions **Lambda**, orchestrées par **EventBridge**, détectent et
suppriment automatiquement les ressources orphelines telles que les volumes
EBS non rattachés ou les instances EC2 inutilisées. Le service **DLM** a
été configuré pour automatiser les sauvegardes des instances EC2, et le
chiffrement KMS est activé par défaut pour EBS.

Bénéfices : posture de sécurité renforcée, réduction significative des
coûts par élimination du gaspillage de ressources, et pérennité des données.

## :material-chip: Apyfal — déploiement d'applications FPGA dans le cloud

!!! abstract "Avril 2018 – avril 2019 &middot; Accelize"

    **Stack :** Python, AWS, OpenStack, FPGA, REST API

Orchestration de l'exécution d'applications matérielles sur des instances
FPGA distantes via une API Python.

Apyfal facilite l'accélération de calcul sur des FPGA disponibles dans le
cloud grâce à un client Python simple d'usage, capable de piloter à
distance le cycle de vie complet de l'application, du déploiement à
l'exécution.

L'architecture repose sur une API RESTful pour la communication entre le
client et le serveur d'orchestration. Ce dernier gère dynamiquement les
ressources FPGA, y compris la programmation des *bitstreams* et l'allocation
d'instances.

La solution réduit considérablement la complexité d'accès aux accélérateurs
FPGA en abstrayant l'hétérogénéité des plateformes cloud et en automatisant
le provisionnement des ressources, rendant l'accélération matérielle aussi
accessible qu'une bibliothèque logicielle.

## :simple-python: Airfs (Pycosio) — bibliothèque Python unifiée pour le stockage cloud

!!! abstract "Juillet 2018 – février 2021 &middot; Open source"

    **Stack :** Python, AWS S3, Azure Storage, OpenStack Swift

Accès unifié au stockage cloud et aux systèmes de fichiers locaux via une
API Python standard, modelée sur les API standard de Python pour la
manipulation de fichiers locaux.

Le cœur technique repose sur l'implémentation des classes abstraites
`io.RawIOBase` et `io.BufferedIOBase`, garantissant une compatibilité
directe avec des modules tels que `io`, `os`, `os.path` et `shutil`. La
manipulation d'objets cloud devient ainsi transparente et interchangeable
avec celle de fichiers locaux.

Les fonctionnalités avancées pour les objets bufferisés incluent l'écriture
asynchrone et le *prefetching*, des mécanismes de verrouillage basés sur
l'utilisation mémoire, et des connexions parallèles pour maximiser la bande
passante. Fournisseurs supportés : **AWS S3**, **Azure Blob Storage**,
**Azure Files**, **OpenStack Swift** et HTTP/HTTPS.

Initialement créé sous le nom *Pycosio*, le projet a été *forké* pour être
étendu et maintenu.

Bénéfices : abstraction de haut niveau simplifiant le code applicatif et le
rendant agnostique à la source de données, améliorant la portabilité et la
maintenabilité tout en garantissant des transferts de données performants.

## :material-waveform: Évolution logicielle d'un banc de test pour cartes électroniques

!!! abstract "Octobre 2017 – avril 2018 &middot; SuperSonic Imagine"

    **Stack :** Python, Debian, NumPy, communication série / TCP

Développement de fonctionnalités critiques pour un banc de test industriel
en Python sous Debian.

Ce projet a porté sur l'amélioration du logiciel de test utilisé en
contexte de fabrication industrielle. Les développements ont inclus
l'instrumentation logicielle pour la commande et la communication avec
divers équipements de mesure. Une évolution majeure a été la mise en place
d'une architecture **client/serveur** pour améliorer la supervision et la
collecte des données de test.

L'optimisation des performances a été un axe central, avec l'utilisation
de NumPy pour accélérer les calculs sur de grands volumes de données. De
nouveaux scénarios de test ont étendu la couverture de validation des
cartes électroniques. Un démonstrateur a également été développé pour
intégrer la méthode d'analyse **SPC** (*Statistical Process Control*),
fournissant des outils statistiques facilitant l'interprétation des mesures
et la détection précoce de dérives du procédé.

## :simple-python: Compilertools — création de paquets binaires Python haute performance

!!! abstract "Février 2017 – décembre 2017 &middot; Open source"

    **Stack :** Python, C / C++, SIMD, PyPI

Bibliothèque Python pour la création et la distribution de paquets binaires
haute performance tirant parti des architectures CPU modernes.

La bibliothèque détecte et exploite les jeux d'instructions avancés des
processeurs (**SIMD : AVX, SSE**) pour générer des binaires optimisés pour
la machine cible. Le système gère la complexité des différentes chaînes de
compilation et architectures matérielles, en offrant un processus de *build*
transparent. Il s'intègre aux outils standard de *packaging* Python pour
faciliter la distribution sur des dépôts comme PyPI.

Cette approche permet de distribuer des applications Python offrant un
maximum de performance dès l'installation, sans compilation manuelle de la
part de l'utilisateur final.

## :material-chart-scatter-plot: Fazpy — logiciel d'analyse de mesures optiques et de pilotage de production

!!! abstract "Octobre 2014 – septembre 2017 &middot; Thales SESO"

    **Stack :** Python, Qt, NumPy, SciPy, Cython, Windows

Solution logicielle complète pour le traitement des données de métrologie
optique et la génération des réglages des équipements de production.

Cette application de bureau pour Windows est développée en Python avec une
interface utilisateur Qt, dédiée aux ingénieurs opticiens et mécaniciens
analysant des mesures complexes (notamment d'interférométrie). Le cœur
logiciel s'appuie sur des modules avancés de calcul optique et de
traitement d'images.

Une attention particulière a été portée à la performance, nécessitant
l'optimisation d'algorithmes et des solutions spécifiques au traitement de
grands volumes de données. L'architecture a été pensée modulaire et
évolutive, intégrant plus de **70 modules fonctionnels distincts**, de
l'acquisition à la visualisation des résultats.

Bénéfices : automatisation et fiabilisation de l'analyse des mesures, avec
un lien direct entre contrôle qualité et fabrication — pour des cycles de
développement raccourcis et une précision accrue des pièces produites.
