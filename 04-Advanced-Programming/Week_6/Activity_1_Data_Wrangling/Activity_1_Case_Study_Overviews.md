# Activity 1 – Case Studies: Personal Overviews

**Chosen case studies:** Bias in Algorithms + Driverless Cars  
**Activity:** ~200-word overview and personal perspective on each, with supporting sources.

---

## Case Study 1: Bias in Algorithms (~200 words)

Algorithmic bias occurs when machine learning systems produce systematically discriminatory outputs — not because of malicious intent, but because the data they were trained on reflects historical inequalities. This issue extends far beyond academic concern: it affects who gets a job interview, who is flagged as a criminal risk, and whose medical symptoms are taken seriously.

The most striking example remains the COMPAS recidivism tool used in US criminal sentencing, which ProPublica (2016) found was twice as likely to falsely label Black defendants as high-risk. Similarly, Amazon's internal hiring algorithm, trained on historical CVs from a male-dominated industry, systematically downgraded CVs from women before being scrapped in 2018.

From my perspective as someone building machine learning systems professionally, this issue is not abstract. In the construction inspection tool I am developing, training data collected under specific lighting and camera conditions will inevitably perform less reliably on inputs outside that distribution. The principle is identical: biased input data produces biased output. The difference is that in my context the bias causes missed defect detections; in a justice system, it destroys lives.

I believe responsibility lies primarily with the engineers and organisations deploying these tools — not with the data itself. Bias must be tested for, measured, and mitigated before deployment, as required by EU AI Act principles and the ACM Code of Ethics.

**Supporting sources:**
- Angwin, J. et al. (2016). 'Machine Bias', ProPublica.
- Buolamwini, J. and Gebru, T. (2018). 'Gender Shades', Proceedings of Machine Learning Research, 81, pp. 77–91.
- ACM (2018). Code of Ethics and Professional Conduct.

---

## Case Study 2: Driverless Cars (~200 words)

Autonomous vehicles represent one of the most consequential intersections of software engineering and public safety. The technology promises to eliminate the 94% of road accidents attributed to human error (NHTSA, 2018), but it introduces a new set of ethical and legal dilemmas that the existing framework was not designed to handle.

The 2018 Uber fatality in Arizona is the case that most clearly illustrates the gap between technological capability and legal/ethical readiness. The vehicle's sensors detected the pedestrian six seconds before impact, but the emergency braking system had been deliberately disabled. The question of who bore responsibility — Uber, the safety driver, the software team — exposed fundamental inadequacies in existing liability law.

What I find most compelling about driverless car ethics is the encoding of moral decisions into algorithms. The system must, implicitly or explicitly, assign a priority order to lives. This is not hypothetical: any real collision avoidance algorithm contains values. The question is whether those values are made explicit, tested, and democratically agreed upon, or simply embedded silently by an engineer working to a deadline.

From my engineering background, I believe transparency is non-negotiable: these decision-making algorithms should be publicly auditable, similar to how pharmaceutical clinical trials are peer-reviewed.

**Supporting sources:**
- BBC News (2018). 'Uber halts self-driving car tests after death'. Available at: https://www.bbc.co.uk/news/business-43459156
- NHTSA (2018). *Automated Driving Systems 2.0: A Vision for Safety*. US Dept. of Transportation.
- Goodall, N.J. (2014). 'Ethical Decision Making During Automated Vehicle Crashes', *Transportation Research Record*, 2424(1), pp. 58–65.
