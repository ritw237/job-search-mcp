import asyncio
import sys
from server import search_jobs
query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "devops"
result = asyncio.run(search_jobs(query,10))
print(result)
