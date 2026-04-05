from mcp.server.fastmcp import FastMCP
import httpx
import json

mcp = FastMCP("job-search-mcp")

@mcp.tool(name="search_jobs")
async def search_jobs(query: str, limit: int=10) ->str:
    """Search for remote jobs worldwide by keyword. Returns job title, company, salary and application link."""

    url = "https://himalayas.app/jobs/api/search"
    params = {"q": query, "limit": limit}

    async with  httpx.AsyncClient() as client:
        response = await client.get(url, params=params)


    data = response.json()
    
    jobs = data.get("jobs",[])

    if not jobs:
        return f"No jobs found for '{query}'"

    results = []
    for job in jobs:
        salary = "Not Listed"
        if job.get("minSalary"):
            salary = f"{job.get('currency', 'USD')} {job['minSalary']:,} - {job['maxSalary']:,}"

        results.append(
                f"**{job['title']}** at {job['companyName']}\n"
                f" Salary: {salary}\n"
                f" Type: {job.get('employmentType', 'N/A')}\n"
                f" Seniority: {', '.join(job.get('seniority', ['N/A']))}\n"
                f" Apply: {job.get('applicationLink', 'N/A')}"
        )

    header = f"Found {data.get('totalCount',0)} total jobs for '{query}' Showing {len(jobs)}:\n\n"

    return header + "\n\n".join(results)

if __name__ == "__main__":
    mcp.run()

