---
title: Resume
description: How to build a resume that beats the ATS and sells you. And how to lie responsibly.
---

By now you're a professional who has mastered your stack and speaks English. Time to start selling yourself. To me, "selling yourself" means the next 4 topics:

1. **Building your resume:** it's what opens the doors to hiring processes. It has to highlight your strengths and get past the ATS, that's it.
2. **LinkedIn:** another door into hiring processes. The most important thing is setting up your profile and building connections. Actively participating in the social network is secondary, but still has some relevance.
3. **Job hunting:** job hunting is selling yourself too, it's like being a door-to-door salesman, except you're the one filling in the same data 3,000 times.
4. **Interview:** the peak of everything we've done so far, so be ready.

Here we'll focus on the resume only.

## Design: there isn't any

Forget all those resumes with colors, photos, visual elements, etc. A tech resume is **content only**, and it has to get past the ATS (*Applicant Tracking System*, the robot that reads your resume before any human does).

I used resumake.io, which was just an interface that compiled your resume in LaTeX with a few predefined layouts. These days I recommend writing it in **Markdown** and generating the PDF from that. The ATS doesn't care whether it came from LaTeX, Markdown or Word: what matters is that the final PDF has **real text** (you can select and copy it), **a single column** and a standard font. Markdown is just way easier to edit, and the Skill further down generates the PDF for you.

This is what it looks like (all made up, obviously, Joana doesn't exist):

![Full example of a resume in the international format](../../../assets/resume/cv-full.png)

Now let's go piece by piece.

## Structure

### Header

Name, phone number (with +55, or your country code), email, and portfolio/GitHub if you have one. Nothing else. No address, no marital status, no photo, no date of birth, nothing.

![Example header: name, phone, e-mail, LinkedIn and GitHub](../../../assets/resume/cv-header.png)

### Title and summary

The title is your job title. In my current case, I use *Analytics Engineer*. Then a short professional summary of what you do, two or three lines.

![Example title and summary](../../../assets/resume/cv-summary.png)

### Experience

Split by company, always with your **latest title** at that company. Put the period you were there too.

![Example job entry: title, company, dates and bullets with metrics](../../../assets/resume/cv-experience.png)

Each tool you want to highlight should get its own bullet point, and if possible a **metric** attached to that bullet point. **EVEN IF YOU NEVER MEASURED IT, PULL IT OUT OF YOUR ASS, BUT PUT A METRIC THERE.**

For example:

> Built a Power BI report on customer churn that helped the board make decisions that reduced churn by 12%.

"Oh, but the board just wanted to look at the number." That's their problem. On your resume they were competent, they acted on it and improved the number, yes they did.

Another example:

> Optimized a data pipeline from 67 minutes to 5 minutes of runtime, cutting cloud processing costs from $420 to $10 per run.

This second one is much easier to measure, but it's worth exaggerating a bit too, just a **responsible exaggeration**.

### Skills

After your experience, list your skills split into categories (languages, tools, cloud, etc.). No soft skills, like leadership, proactivity, etc. The only people who like that crap are Brazilian managers.

![Example skills section, grouped by category](../../../assets/resume/cv-skills.png)

### Education

Last, your education. Depending on how much weight your education carries, you can put it earlier. If I'd graduated from MIT, that would go right after the summary.

![Example education section](../../../assets/resume/cv-education.png)

## How to create the resume

I left a **Claude Skill** in the repository to help you with this ([the `skills/curriculo-gringa` folder](https://github.com/kyomeii/devemdolar/tree/main/skills/curriculo-gringa)). It follows everything on this page: asks the right questions, turns your experience into bullet points with metrics, writes the resume in Markdown and spits out the finished PDF, just like the example above. Claude itself will walk you through setting it up.

## About lying on your resume

Lie, but **lie responsibly**. "Do I know how to do it? No, but I'll learn." And the recruiter doesn't need to know you don't know. Obviously you need some foundation so you don't talk shit, get past the HR recruiter, and have enough time to dig deeper and pass the technical interview too.

Have I ever done a professional project with dbt? Not yet, but I've done a few personal ones, and I know a lot already. My resume has a little piece of fiction where I took over and optimized the transformation layer using dbt. Today I've mastered the tool, and I know enough about that specific transformation layer to understand how the tool would fit into the process. That's lying responsibly.

Tell not only your story, but the story of who you want to become.
