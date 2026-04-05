
import httpx
import json

url = "https://himalayas.app/jobs/api/search"
params = {"query": "devops", "limit": 5}

response = httpx.get(url, params=params)
data = response.json()

print(f"Total jobs found: {data['totalCount']}")
print(f"Returned: {len(data['jobs'])} jobs\n")

for job in data["jobs"]:
    print(f"Title: {job['title']}")
    print(f"Company: {job['companyName']}")
    salary = ""
    if job.get("minSalary"):
        salary = f"{job['currency']} {job['minSalary']:,} - {job['maxSalary']:,}"
    print(f"Salary: {salary or 'Not listed'}")
    print(f"Type: {job['employmentType']}")
    print(f"Link: {job['applicationLink']}")
    print("---")
