"""Multi-strategy day-trading agent.

Every strategy runs as its own paper-money "sleeve" so they can be compared
honestly. A walk-forward meta-agent ("Agent") trades whichever
strategy/symbol pairs have been working recently. Real-money trading is off
unless it is explicitly enabled (see README).
"""

__version__ = "1.0.0"
