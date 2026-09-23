---
title: "Can AI Co-Design Structures? An AI Agent for Early-Stage Structural Design"
venue: "IASS–IWSS 2026 Symposium · Turin, Italy"
authors: "Ricardo Maia Avelino<sup>1,2</sup>, Mennatallah El-Assady<sup>2</sup>, Tom Van Mele<sup>1</sup>, Philippe Block<sup>1</sup>"
affiliations: "<sup>1</sup>Block Research Group, Dept. of Architecture &middot; <sup>2</sup>IVIA Lab, Dept. of Computer Science &middot; ETH Zürich, Switzerland"
description: "Can AI Co-Design Structures? — An AI agent for early-stage structural design. Proceedings of the IASS–IWSS 2026 Symposium, Turin."
teaser: /images/papers/co-design.png
figure: /images/projects/can-ai-codesign/workflow.png
figure_caption: "Agentic structural modelling workflow. The designer prompts an AI agent, which uses tool calls on an MCP server to build and edit a COMPAS-based, graph-based structural model made of joints, columns and slabs. The model can then be exported to and imported from downstream AEC tools."
paper: https://pub-12d7216700584ed7a1b50eac1448d179.r2.dev/IASS_2026_-_IWSS_2026_paper_666.pdf
bibtex: |
  @inproceedings{avelino2026canai,
    author    = {Maia Avelino, R. and El-Assady, M. and Van Mele, T. and Block, P.},
    title     = {Can {AI} Co-Design Structures? An {AI} Agent for Early-Stage Structural Design},
    booktitle = {Proceedings of the IASS Symposium 2026},
    address   = {Turin, Italy},
    year      = {2026},
  }
---

## Abstract

Recent advances in large language models and agentic workflows offer a new paradigm to early-stage structural design translating design intent into structural models. Although text-to-3D approaches have demonstrated that natural language can be used to produce visual, mesh-based geometric models, structural design requires domain-specific geometric arrangements and semantically rich data types. This paper introduces a proof-of-concept workflow for prompt-to-structure generation using an AI agent connected to a COMPAS-based structural modelling API through a Model Context Protocol (MCP) server. Through controlled modelling operations, the agent creates and modifies a graph-based structural data model composed of explicit building elements. The resulting artifacts can be inspected, modified, serialised, and further connected to downstream AEC workflows. The approach is demonstrated through selected prompt-to-structure examples and by progressive and editable design sequences that resemble typical iterative structural design workflows. The results are preliminary, but demonstrate the possibility of combining natural language, agentic workflows, and domain-specific structural data structures as a first step toward AI-assisted structural co-design.
