from ddgs import DDGS

with DDGS() as ddgs:
    results = list(ddgs.text("Agentic AI", max_results=5))

print(results)
from ddgs import DDGS

results = DDGS().text("Agentic AI")
print(results[:5])
