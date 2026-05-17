# AI Agent Systems Lab

This repository documents my local AI agent development setup while working through the Hugging Face Agents Course.

## Current Stack

- Ollama
- Qwen2 7B
- Python 3.14
- smolagents
- LiteLLM
- Hugging Face Agents Course

## Current Status

I successfully created a local model bridge:

Python 3.14 -> smolagents -> LiteLLM -> Ollama -> Qwen2 7B -> Terminal response

## Completed Work

- Installed Ollama
- Pulled qwen2:7b
- Tested local model response with ollama run qwen2:7b
- Installed Python 3.14
- Installed smolagents with LiteLLM support
- Created test_agent.py
- Successfully called the local model from Python

## Run Test

Run:

python3.14 test_agent.py

## Roadmap

- [x] Install Ollama
- [x] Pull Qwen2 7B
- [x] Install Python 3.14
- [x] Install smolagents with LiteLLM
- [x] Run local Python-to-Ollama test
- [ ] Complete Hugging Face Agents Course Unit 1
- [ ] Build first tool-using agent
- [ ] Add calculator tool
- [ ] Add local file-reading tool
- [ ] Build maintenance diagnostic agent prototype

## Strategic Purpose

This lab documents a local-first AI agent development workflow. The long-term goal is to build practical AI systems for diagnostics, documentation, automation, learning, and technical problem-solving.
