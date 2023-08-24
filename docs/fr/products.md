---
title: Produits
description: Solutions logicielles disponibles sur l'AWS Marketplace — stdapi.ai, passerelle IA
keywords: produits, logiciels, AWS Marketplace, stdapi, passerelle IA, compatibilité API, OpenAI, Anthropic, Bedrock, Claude, LLM
---

# Produits

JGoutin-dev SARL développe des solutions logicielles disponibles sur l'AWS
Marketplace.

## :material-rocket-launch: stdapi.ai — passerelle compatible OpenAI, Anthropic et Cohere pour Amazon Bedrock

![Logo stdapi.ai](../assets/stdapi_ai_logo.svg){ width=200 }

!!! tip "Exploitez plus de 100 modèles IA sur Amazon Bedrock via des API compatibles OpenAI, Anthropic et Cohere"

    Un essai gratuit de 14 jours est inclus sur l'AWS Marketplace.

`stdapi.ai` est une passerelle API *drop-in* qui s'exécute dans votre propre
compte AWS et connecte vos outils compatibles OpenAI, Anthropic et Cohere à
Amazon Bedrock. Une seule ligne à modifier — votre URL de base — et vos outils
se connectent via le SDK qu'ils utilisent déjà : LangChain, Open WebUI, Claude
Code, OpenCode, n8n, et des centaines d'autres applications.

### Pourquoi stdapi.ai ?

<div class="grid cards" markdown>

-   :material-power-plug:{ .lg } &nbsp; __Remplacement *drop-in*__

    ---

    *Chat*, *embeddings*, *reranking*, images, vidéo, audio, fichiers et
    modération — plus de 50 points d'accès sur trois protocoles. Les SDK
    standard OpenAI, Anthropic et Cohere se connectent avec la seule URL de
    base.

-   :material-brain:{ .lg } &nbsp; __100+ modèles__

    ---

    Claude, OpenAI GPT, xAI Grok, Kimi, DeepSeek, Qwen, GLM, Nova, Llama, et
    bien d'autres — de la part d'Anthropic, OpenAI, xAI, Moonshot, DeepSeek,
    Alibaba, Zhipu, Amazon et Meta. Bedrock, Bedrock Mantle, Polly, Transcribe
    et Comprehend forment un catalogue unique, découvert automatiquement.
    Changez de modèle à la volée — sans verrouillage fournisseur.

-   :material-shield-lock:{ .lg } &nbsp; __Aucun tiers entre vos utilisateurs et vos modèles__

    ---

    La passerelle s'exécute dans votre propre compte AWS, et Amazon Bedrock ne
    partage pas vos *prompts* avec les fournisseurs de modèles et ne les
    utilise pas pour l'entraînement. Configurez les régions autorisées selon
    vos exigences de résidence des données — les certifications de conformité
    AWS s'appliquent aux services et aux régions que vous choisissez, et ne
    sont pas héritées par stdapi.ai.

-   :material-earth:{ .lg } &nbsp; __Un quota par région, et reprise inter-régions__

    ---

    Chaque région AWS dispose de son propre quota Bedrock, et chaque région
    que vous activez ajoute le sien. Les erreurs de limitation de débit et
    d'indisponibilité éligibles sont réessayées dans une autre région activée —
    le *streaming* ne peut être réessayé qu'avant l'ouverture du flux, et les
    traitements asynchrones restent dans la région qui les a acceptés.

-   :material-cash-multiple:{ .lg } &nbsp; __Vous ne payez que ce que vous utilisez__

    ---

    0 % de marge sur l'usage des modèles — Amazon Bedrock vous est facturé
    directement par AWS, à ses tarifs. La licence de la passerelle est à
    0,10 $ par heure-conteneur sur l'AWS Marketplace (essai gratuit de
    14 jours, 0,09 $ via une offre privée), ou 0 $ avec l'édition Communauté
    AGPL-3.0. Par défaut, le module Terraform déploie une tâche par zone de
    disponibilité — environ 216 $/mois dans une région à trois zones.

-   :material-flash:{ .lg } &nbsp; __Fonctionnalités avancées de Bedrock__

    ---

    Modes de raisonnement, *prompt caching*, *guardrails*, profils
    d'inférence et *prompt routers* — le tout via les paramètres API
    standard.

</div>

**&lt;1 ms** de surcoût de la passerelle · **5 000+** cas de test automatisés · **12** suites clients et frameworks exécutées de
bout en bout sur un déploiement réel.

### Démarrer

=== "Édition Communauté"

    0 $, image conteneur AGPL-3.0 avec l'API complète — l'édition commerciale
    ajoute le durcissement, le support et les droits de licence, pas des
    points d'accès.

=== "Production"

    Module Terraform déployant ECS avec une image conteneur durcie,
    disponible sur l'AWS Marketplace à 0,10 $ par heure-conteneur (essai
    gratuit de 14 jours).

[Démarrer l'essai gratuit](https://stdapi.ai/operations_getting_started/){ .md-button .md-button--primary }
[Documentation](https://stdapi.ai/){ .md-button }
[:fontawesome-brands-github: GitHub](https://github.com/stdapi-ai/stdapi.ai){ .md-button }

### AWS Qualified Software

<a href="https://aws.amazon.com/marketplace/pp/prodview-su2dajk5zawpo">
![Badge AWS Qualified Software](../assets/aws_qualified_software_badge_light.png#only-light){ width="120" }
![Badge AWS Qualified Software](../assets/aws_qualified_software_badge_dark.png#only-dark){ width="120" }
</a>

stdapi.ai est une solution **AWS Qualified Software**, vérifiée par rapport aux exigences techniques et de sécurité AWS pour l'AWS Marketplace.

## :fontawesome-brands-github: Open source

JGoutin-dev contribue activement à des projets *open source*. Visitez notre
[:fontawesome-brands-github: profil GitHub](https://github.com/jgoutin) pour
découvrir nos travaux *open source*.

## :material-account-hard-hat: Solutions sur mesure

Besoin d'une solution adaptée à vos besoins spécifiques ? Découvrez nos
[services de conseil](services.md).
