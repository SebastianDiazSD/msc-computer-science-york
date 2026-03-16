# Week 5 — Databases, Data Mining, and Cloud Security

## Topics Covered
- Database security threats
- SQL injection
- Data mining and inference attacks
- Cloud computing security model
- Shared responsibility in cloud environments

---

## Key Concepts

### Databases as High-Value Targets
Databases store the most critical assets: personal data, financial records, credentials, health information. They are subject to all CIA triad risks plus database-specific threats.

### SQL Injection
The most common database attack. Malicious SQL code is embedded in user input fields and executed by the database:
```sql
-- Normal query:
SELECT * FROM users WHERE username = 'sebastian';

-- Injected query (input: ' OR '1'='1):
SELECT * FROM users WHERE username = '' OR '1'='1';
-- Returns all users — authentication bypassed
```

Prevention: parameterised queries (never concatenate user input directly into SQL), ORMs (Object-Relational Mappers), input validation.

### Inference Attacks
Even well-designed databases can leak information through carefully constructed queries:
- **Negative queries** — what is NOT in the database can reveal information
- **Aggregate queries** — statistical summaries can reveal individual data when populations are small
- **Composite queries** — combining multiple legitimate queries to deduce protected information

This is why anonymisation of data is difficult — individual records can often be re-identified by combining fields.

### Cloud Security Considerations
Cloud = "somebody else's computer." Security considerations:
- **Data sovereignty** — where is data physically stored? Which jurisdiction's laws apply?
- **Multi-tenancy** — your data shares infrastructure with other organisations — isolation must be enforced
- **Access control** — cloud misconfiguration (publicly accessible storage buckets) is a leading cause of breaches
- **Vendor lock-in** — dependence on a single provider creates availability and resilience risk

### Shared Responsibility Model
| Responsibility | Cloud Provider | Customer |
|---|---|---|
| Physical infrastructure | ✅ | |
| Hypervisor / platform | ✅ | |
| OS configuration | Depends on model | ✅ (IaaS) |
| Application security | | ✅ |
| Access management | | ✅ |
| Data classification | | ✅ |

The customer remains responsible for configuration, access management, and data protection even when using managed cloud services.

---

## Connection to Summative Assessment
In my coursework, I identified cloud misconfiguration as a HIGH risk for the digital health platform — specifically publicly accessible storage buckets exposing user health data. The shared responsibility model justified requiring clear contractual obligations between the organisation and cloud provider defining who is responsible for each security layer.

---

## Week 5 Summary
Databases are essential but high-risk components of any system. SQL injection is the classic attack; inference attacks are more subtle. Cloud computing introduces new attack surfaces around configuration, access control, and data sovereignty. The shared responsibility model requires clarity about who owns which security obligations.
