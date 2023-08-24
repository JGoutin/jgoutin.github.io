---
title: Products
description: Software solutions available on the AWS Marketplace - stdapi.ai AI Gateway
keywords: products, software, AWS Marketplace, stdapi, AI gateway, API compatibility, OpenAI, Anthropic, Bedrock, Claude, LLM
---

# Products

JGoutin-dev SARL develops software solutions available through the AWS
Marketplace.

## :material-rocket-launch: stdapi.ai — OpenAI-, Anthropic- & Cohere-compatible gateway for Amazon Bedrock

![stdapi.ai logo](../assets/stdapi_ai_logo.svg){ width=200 }

!!! tip "Run 100+ AI models on Amazon Bedrock through OpenAI-, Anthropic-, and Cohere-compatible APIs"

    A 14-day free trial is included on the AWS Marketplace.

`stdapi.ai` is a drop-in API gateway that runs in your own AWS account and
connects your existing OpenAI-, Anthropic-, and Cohere-compatible tools to
Amazon Bedrock. Change one line — your base URL — and your tools connect
through the SDK they already use: LangChain, Open WebUI, Claude Code, OpenCode,
n8n, and hundreds of other applications.

### Why stdapi.ai?

<div class="grid cards" markdown>

-   :material-power-plug:{ .lg } &nbsp; __Drop-in replacement__

    ---

    Chat, embeddings, reranking, images, video, audio, files, and moderation —
    50+ endpoints across three protocols. Standard OpenAI, Anthropic, and
    Cohere SDKs connect on the base URL alone.

-   :material-brain:{ .lg } &nbsp; __100+ models__

    ---

    Claude, OpenAI GPT, xAI Grok, Kimi, DeepSeek, Qwen, GLM, Nova, Llama, and
    more — from Anthropic, OpenAI, xAI, Moonshot, DeepSeek, Alibaba, Zhipu,
    Amazon, and Meta. Bedrock, Bedrock Mantle, Polly, Transcribe, and
    Comprehend surface as one catalogue, discovered automatically. Switch
    models on the fly — no vendor lock-in.

-   :material-shield-lock:{ .lg } &nbsp; __No third party between your users and your models__

    ---

    The gateway runs in your own AWS account, and Amazon Bedrock does not share
    prompts with model providers or use them for training. Configure region
    allow-lists to match your data-residency requirements — AWS compliance
    certifications apply to the AWS services and regions you choose, and are
    not inherited by stdapi.ai.

-   :material-earth:{ .lg } &nbsp; __One quota per region, and regional retry__

    ---

    Every AWS region has its own Bedrock quota, and each region you enable adds
    its own. Eligible throttling and availability failures retry in another
    enabled region — streaming retries only before the stream opens, and
    asynchronous jobs stay in the region that accepted them.

-   :material-cash-multiple:{ .lg } &nbsp; __Pay only for what you use__

    ---

    0% markup on model usage — Amazon Bedrock is billed to you directly by AWS,
    at AWS rates. The gateway licence is $0.10 per container-hour on the AWS
    Marketplace (14-day free trial, $0.09 through a private offer), or $0 with
    the AGPL-3.0 Community edition. The Terraform default runs one task per
    availability zone — about $216/month in a three-AZ region.

-   :material-flash:{ .lg } &nbsp; __Advanced Bedrock features__

    ---

    Reasoning modes, prompt caching, guardrails, inference profiles, and
    prompt routers — all through standard API parameters.

</div>

**&lt;1 ms** gateway overhead · **5,000+** automated test cases · **12** client and framework suites driven end to end against a live
deployment.

### Get started

=== "Community Edition"

    $0, AGPL-3.0 container image with the full API — the commercial edition
    adds hardening, support, and licence rights, not endpoints.

=== "Production"

    Terraform module deploying ECS with a hardened container image, available
    on the AWS Marketplace at $0.10 per container-hour (14-day free trial).

[Start the free trial](https://stdapi.ai/operations_getting_started/){ .md-button .md-button--primary }
[Documentation](https://stdapi.ai/){ .md-button }
[:fontawesome-brands-github: GitHub](https://github.com/stdapi-ai/stdapi.ai){ .md-button }

### AWS Qualified Software

<a href="https://aws.amazon.com/marketplace/pp/prodview-su2dajk5zawpo">
![AWS Qualified Software badge](../assets/aws_qualified_software_badge_light.png#only-light){ width="120" }
![AWS Qualified Software badge](../assets/aws_qualified_software_badge_dark.png#only-dark){ width="120" }
</a>

stdapi.ai is an **AWS Qualified Software** solution, verified against AWS technical and security requirements for AWS Marketplace.

## :fontawesome-brands-github: Open source

JGoutin-dev actively contributes to open-source projects. Visit our
[:fontawesome-brands-github: GitHub profile](https://github.com/jgoutin) to
explore our open-source work.

## :material-account-hard-hat: Custom solutions

Need a solution tailored to your specific requirements? Discover our
[consulting services](services.md).
