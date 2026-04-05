# job-search-mcp

MCP server that searches 100K+ remote job listings via the [Himalayas](https://himalayas.app) public API.

## what it does
$ python3 search.py "devops"
Found 604 jobs. Showing 10:
Senior DevOps Engineer at SomeCompany
Salary: USD 120,000 - 160,000
Type: Full Time
Apply: https://himalayas.app/companies/...
## setup
```bash
git clone https://github.com/ritw237/job-search-mcp.git
cd job-search-mcp
python3 -m venv venv && source venv/bin/activate
pip install mcp httpx
```

## usage
```bash
python3 search.py "devops"
python3 search.py "business analyst"
python3 search.py "cloud engineer"
```

Also works as an MCP server (`python3 server.py`) for any MCP-compatible client.

## how this got built

Started by trying to scrape Naukri.com for Indian job listings. Didn't go well:

1. **httpx + BeautifulSoup** -> Naukri is a Next.js app, so httpx got an empty HTML shell with `jobDetails: []`. The actual jobs load via JavaScript after page render.
2. **Naukri's internal API** (`/jobapi/v3/search`) -> returned `"recaptcha required"` with a 406 status.
3. **Playwright with headless Chromium** -> Akamai bot detection returned "Access Denied" before the page even loaded.
4. **Himalayas public API** -> free, no auth, 100K+ listings, clean JSON. Done in 20 lines.

Lesson: don't fight bot detection for a portfolio project. Find a public API.

## stack

- Python 3.12
- [FastMCP](https://github.com/jlowin/fastmcp) (MCP server framework)
- httpx (async HTTP)
- [Himalayas API](https://himalayas.app/api) (job data, free, no auth)

## future

- Aggregate more sources (Remotive, Arbeitnow, RemoteOK)
- Country/region filtering
- Host as HTTP server on homelab

## license

MIT
