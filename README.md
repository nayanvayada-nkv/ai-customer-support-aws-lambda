<<<<<<< HEAD
# 🤖 AI-Powered Customer Support Assistant (AWS Lambda + Claude 3 via Bedrock)

This project is a **serverless AI chatbot** that uses **AWS Lambda**, **Amazon API Gateway**, and **Amazon Bedrock** to deliver intelligent customer support powered by **Claude 3 Haiku** from Anthropic.

It’s built for the [AWS Lambda Hackathon 2025](https://devpost.com/) and demonstrates real-world usage of GenAI in customer service automation.

---

## 🚀 Features

- ⚡ Serverless architecture using AWS Lambda
- 🌐 Exposed via API Gateway (HTTP endpoint)
- 🧠 GenAI backend using Claude 3 (Bedrock API)
- 💬 Accepts real-time customer queries and returns smart responses
- 🔐 IAM-secured access to Bedrock APIs
- 📦 Easy to test with JSON payloads

---

## 🛠️ Architecture

```text
Client (Postman / Website / App)
        ↓ (HTTP Request)
  API Gateway (HTTP API)
        ↓
  AWS Lambda (Python Runtime)
        ↓
Amazon Bedrock → Claude 3 Haiku
        ↓
  Lambda returns AI response
        ↓
     Client receives reply
=======
# ai-customer-support-aws-lambda
This project is a serverless AI-powered customer support assistant built using AWS Lambda, Amazon API Gateway, and Amazon Bedrock (Claude 3 Haiku). It enables natural language interaction via HTTP API and leverages Anthropic's Claude model for real-time responses. Designed for hackathons and cloud-native learning.
>>>>>>> 1f6f332cfb19497dbb8217e95e6a4e999c740c09
