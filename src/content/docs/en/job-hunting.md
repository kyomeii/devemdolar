---
title: Job hunting
description: "Boolean search, LinkedIn Posts, Google with site: and HiringCafe. Where the good jobs are."
---

When you're hitting on girls (or guys), you should never reject yourself, you let the other person decide whether to reject you or not. Same goes for jobs.

> "I already have the no. Now I'm going for the humiliation."

This is where the real battle begins. You'll probably apply to dozens of jobs before you get called for an interview, and that's fine. You're just one more fish in a sea full of people, but sooner or later you'll get hooked too. Personally, I only search in three ways: **LinkedIn, Google, and HiringCafe**.

## Boolean search

For both LinkedIn and Google, you'll use **boolean search**. You just build your search using logical operators to say exactly what you want and what you don't:

| Operator | What it does | Example |
|---|---|---|
| `"quotes"` | Searches for the exact phrase | `"Power BI"` (and not "power" and "BI" on their own) |
| `OR` | Any of the terms | `"Power BI" OR Tableau` |
| `AND` | All terms have to appear | `"Power BI" AND remote` |
| `NOT` (LinkedIn) or `-` (Google) | Excludes the term | `NOT India` / `-India` |
| `( )` | Groups things, like in math | `("Power BI" OR Tableau) AND remote` |

Rules everybody gets wrong:

- On LinkedIn, `AND`, `OR`, and `NOT` have to be in **UPPERCASE**. In lowercase it ignores them.
- On Google, `AND` doesn't exist (all terms are already required by default), and to exclude something you put a minus sign stuck to the word: `-India`.
- On LinkedIn, always use parentheses when you mix `OR` with `AND`, otherwise the results turn into a mess.
- Google ignores parentheses, but that's fine: there, `OR` already "sticks" to the neighboring terms, so `"Power BI" OR Tableau remote` works like `("Power BI" OR Tableau) remote`.

The structure that works is: **(your titles/stack) AND (remote) AND (where you can work from) NOT (what you don't want)**. Example for my stack:

```
("Power BI" OR "Analytics Engineer" OR "BI Developer" OR "BI Engineer") AND (remote OR "work from anywhere") AND (LATAM OR "Latin America" OR Brazil OR "South America") NOT (hybrid OR onsite OR "on-site")
```

Swap the terms in the first parentheses for your stack and you're done. It's worth saving 3 or 4 variations (a broader one, one with just your exact title, one with "contractor" instead of "remote") and rotating between them.

## LinkedIn

Now that you know your stuff, just copy and paste your boolean search into LinkedIn's search bar. Then you click on *Jobs*, right?

**WRONG!**

Most of what's in the jobs tab are ghost jobs, you'll apply to a shitload of them and never get called, only a few are legit. It's only worth applying there if it's one of those *Easy Apply* ones where you don't even waste time. These days there's probably some way to use AI to do that in bulk, but I never looked into it.

You're going to search **Posts** only. Whenever a recruiter has a legit opening, they also post about it, so it's a way to filter. Sort by **most recent**.

There's also a lot of garbage in posts, mainly because there are tons of Indians posting scam jobs or jobs just for India. You click on posts, read the name of whoever posted it, if it's Indian you can already skip it, and so on. Is it boring? As hell, but that's where the best jobs are. Look for clearly Anglo-Saxon, Latino, or maybe even Eastern European names. Then you actually read the text.

These days those also have a good chance of being scams. Signs it's a scam:

- Extremely generic text ("We are hiring! Multiple positions! DM me!").
- Contact via an `@gmail.com`, `@zohomail.com`, `@outlook.com` email, or worse, Telegram/WhatsApp.
- Salary way too good for way too few requirements.
- Company with no website, or with a website created last month.
- They ask you to pay for something (training, equipment, "processing fee"). A legit job **never** charges you.

Legit jobs will point either to LinkedIn itself or to the company's recruiting platform, which brings us to the next search option:

## Google

Here you keep the boolean search from LinkedIn (adapted for Google: no `AND`, no parentheses, and `-` instead of `NOT`), except at the beginning of the search you put the most common recruiting platforms (ATS). Your search will be:

```
site:greenhouse.io "Power BI" OR "Analytics Engineer" OR "BI Developer" OR "BI Engineer" remote OR "work from anywhere" LATAM OR "Latin America" OR Brazil OR "South America" -hybrid -onsite
```

Then you swap the `site:` for the other platforms:

| Platform | What to put in `site:` |
|---|---|
| Greenhouse | `site:greenhouse.io` (catches `boards.` and `job-boards.`) |
| Lever | `site:jobs.lever.co` |
| Ashby | `site:jobs.ashbyhq.com` |
| Workable | `site:apply.workable.com` |
| SmartRecruiters | `site:jobs.smartrecruiters.com` |
| Recruitee | `site:recruitee.com` |
| BambooHR | `site:bamboohr.com` |
| Breezy HR | `site:breezy.hr` |
| Workday | `site:myworkdayjobs.com` |
| Rippling | `site:ats.rippling.com` |
| Wellfound (startups) | `site:wellfound.com` |

Filter Google by the **past week** (or past 24 hours): *Tools → Any time → Past week*.

Then keep clicking through the sites and checking the jobs. When you've gone through everything that showed up, move on to the next site.

You'll do this LinkedIn and Google routine **every day**. On LinkedIn, twice a day, morning and night. Don't give up! If you see a fresh job post, your chances of getting called are way higher than for one that was posted a few days ago.

## HiringCafe

[HiringCafe](https://hiringcafe.com) is a platform built by a reddit user, and it's by far the best job platform I've ever seen. They aggregate straight from the sites you searched on Google, but one thing or another might not show up there.

Over there, you leave your search saved and check it every day. When you see a job that fits your profile, you don't just apply: you go to LinkedIn, search for the company's employees, and add them. **Especially the recruiters.**

## Companies that hire Brazilians

At some point I'll add companies to this site that hire Brazilians or Latin Americans remotely, whether they're consulting firms, recruiting agencies, or the company itself. I just have to scrape my emails to find the full list.

Meanwhile, there's a page of [companies and platforms](/en/companies/) that the community keeps filling in. If you work or have worked at a company that hires Brazilians remotely, send a pull request.
