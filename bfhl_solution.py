import requests


generate_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

payload = {
    "name": "Palak Yadav",             
    "regNo": "0827AL221094",            
    "email": "palakyadav220463@acropolis.in" 
}

response = requests.post(generate_url, json=payload)


if response.status_code == 200:
    data = response.json()
    webhook_url = data['webhook']
    access_token = data['accessToken']
    print("Webhook URL:", webhook_url)
    print("Access Token:", access_token)
else:
    print("Failed to get webhook. Status code:", response.status_code)
    print(response.text)
    exit()

    
final_query = """
SELECT 
    p.AMOUNT AS SALARY,
    e.FIRST_NAME || ' ' || e.LAST_NAME AS NAME,
    FLOOR((JULIANDAY('2025-05-11') - JULIANDAY(e.DOB)) / 365.25) AS AGE,
    d.DEPARTMENT_NAME
FROM PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE CAST(STRFTIME('%d', p.PAYMENT_TIME) AS INTEGER) != 1
ORDER BY p.AMOUNT DESC
LIMIT 1;
""".strip()


headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

submission_payload = {
    "finalQuery": final_query
}

submit_response = requests.post(webhook_url, headers=headers, json=submission_payload)


if submit_response.status_code == 200:
    print("Query submitted successfully!")
else:
    print(" Submission failed. Status Code:", submit_response.status_code)
    print("Response:", submit_response.text)
