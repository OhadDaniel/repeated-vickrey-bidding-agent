# Adaptive Truthfulness – Agent for Repeated Second‑Price (Vickrey) Auctions

This repo contains my submission for an **algorithmic game theory** style competition: a **repeated second‑price auction** (15 rounds) under a **hard budget constraint**.

In each round an item is auctioned, every team submits a sealed bid, the **highest bidder wins** and pays the **second‑highest bid**. Teams learn only the **winner identity** and **price paid** after each round, and must adapt online.

Alongside the agent, I keep a lightweight copy of the competition runner so anyone can reproduce validation and simulations locally.

## Paper / write‑up
If you want the full design rationale and thought process, see:

- `agt_paper/AGT_PAPER.pdf`

## Quickstart
### 1) Setup
Requirements: **Python 3.11+**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Validate my agent
My agent lives at `teams/my_team/bidding_agent.py`.

```bash
python main.py --mode validate --validate teams/my_team/bidding_agent.py
```

Expected: `Agent validation PASSED`.

### 3) Run simulations
Run a small tournament against the built‑in example agents:

```bash
python simulator.py --your-agent teams/my_team/bidding_agent.py --num-games 20
```

Run against a specific opponent:

```bash
python simulator.py --your-agent teams/my_team/bidding_agent.py \
  --opponent examples/truthful_bidder.py --num-games 20 --seed 6431
```

Verbose mode for a full round‑by‑round trace:

```bash
python simulator.py --your-agent teams/my_team/bidding_agent.py --num-games 1 --verbose
```

## Repository structure
- `teams/my_team/bidding_agent.py` – **my adaptive bidding agent**
- `src/` – competition engine (auction + game/tournament managers)
- `examples/` – baseline agents (truthful, budget‑aware, etc.)
- `agt_paper/` – the write‑up

## Notes
- Decisions must be computed fast (the original environment enforced a strict per‑bid time limit).
- Public feedback per round is limited to `(winner, price_paid)`; full bid vectors are not revealed.

---
If you use this repo as a starting point, please keep credit to the original competition framework authors/organizers.
